# app.py
from flask import Flask, request, jsonify, render_template
import torch
from PIL import Image
from io import BytesIO
import base64
from transformers import (
    VisionEncoderDecoderModel, 
    ViTImageProcessor, 
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)
from gtts import gTTS
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load models
def load_models():
    # Image captioning model
    caption_model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    caption_tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

    # Translation model
    trans_model = AutoModelForSeq2SeqLM.from_pretrained("ai4bharat/indictrans2-en-indic-1B")
    trans_tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indictrans2-en-indic-1B")

    return {
        'caption_model': caption_model,
        'feature_extractor': feature_extractor,
        'caption_tokenizer': caption_tokenizer,
        'trans_model': trans_model,
        'trans_tokenizer': trans_tokenizer
    }

models = load_models()

# Supported languages
SUPPORTED_LANGUAGES = {
    'hi': 'Hindi',
    'bn': 'Bengali',
    'te': 'Telugu',
    'ta': 'Tamil',
    'mr': 'Marathi'
}

def generate_caption(image):
    # Preprocess image
    pixel_values = models['feature_extractor'](images=image, return_tensors="pt").pixel_values
    
    # Generate caption
    output_ids = models['caption_model'].generate(
        pixel_values,
        max_length=16,
        num_beams=4
    )
    
    caption = models['caption_tokenizer'].decode(output_ids[0], skip_special_tokens=True)
    return caption

def translate_text(text, target_lang):
    # Prepare input
    inputs = models['trans_tokenizer'](
        text,
        return_tensors="pt",
        padding=True,
        truncation=True
    )
    
    # Generate translation
    outputs = models['trans_model'].generate(
        **inputs,
        max_length=256,
        num_beams=5
    )
    
    translation = models['trans_tokenizer'].decode(outputs[0], skip_special_tokens=True)
    return translation

def generate_audio(text, lang):
    tts = gTTS(text=text, lang=lang)
    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp3')
    tts.save(audio_path)
    return audio_path

@app.route('/')
def index():
    return render_template('index.html', languages=SUPPORTED_LANGUAGES)

@app.route('/process', methods=['POST'])
def process_image():
    try:
        # Get image and target language
        image_file = request.files['image']
        target_lang = request.form['language']
        
        if not image_file:
            return jsonify({'error': 'No image uploaded'}), 400
        
        # Save and process image
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image_file.filename))
        image_file.save(image_path)
        image = Image.open(image_path)
        
        # Generate caption
        caption = generate_caption(image)
        
        # Translate caption
        translation = translate_text(caption, target_lang)
        
        # Generate audio files
        en_audio_path = generate_audio(caption, 'en')
        trans_audio_path = generate_audio(translation, target_lang)
        
        return jsonify({
            'caption': caption,
            'translation': translation,
            'image_path': image_path,
            'en_audio_path': en_audio_path,
            'trans_audio_path': trans_audio_path
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)