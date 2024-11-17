# Image Captioning, Translation, and Audio Narration Web Application

A Flask-based web application that performs image captioning, translates the captions into various Indian languages, and generates audio narrations for both English and translated captions.

## Features

- 🖼️ **Image Captioning**: Generates descriptive captions for uploaded images using ViT-GPT2
- 🔄 **Translation**: Translates captions into multiple Indian languages using AI4Bharat's IndicTrans2 model
- 🔊 **Audio Narration**: Converts both English and translated captions into speech
- 🌐 **Supported Languages**:
  - Hindi (hi)
  - Bengali (bn)
  - Telugu (te)
  - Tamil (ta)
  - Marathi (mr)

## Technical Stack

- **Backend Framework**: Flask
- **Machine Learning Libraries**: 
  - PyTorch
  - Transformers
- **Models**:
  - Image Captioning: `nlpconnect/vit-gpt2-image-captioning`
  - Translation: `ai4bharat/indictrans2-en-indic-1B`
- **Text-to-Speech**: gTTS (Google Text-to-Speech)

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create required directories:
```bash
mkdir -p static/uploads
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open a web browser and navigate to `http://localhost:5000`

3. Upload an image and select your desired translation language

4. The application will:
   - Generate a caption for your image
   - Translate the caption to your selected language
   - Create audio files for both versions
   - Display results on the webpage

## API Endpoints

### POST /process
Processes an uploaded image and returns captions, translations, and audio paths.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Parameters:
  - `image`: Image file
  - `language`: Target language code (e.g., 'hi' for Hindi)

**Response:**
```json
{
    "caption": "English caption",
    "translation": "Translated caption",
    "image_path": "path/to/saved/image",
    "en_audio_path": "path/to/english/audio",
    "trans_audio_path": "path/to/translated/audio"
}
```

## Configuration

The application includes the following configurations:
- Maximum file size: 16MB
- Upload folder: `static/uploads`
- Debug mode: Enabled in development

## Error Handling

The application includes error handling for:
- Missing image uploads
- Unsupported file types
- File size limits
- Processing errors

## Model Details

1. **Image Captioning Model**
   - Model: ViT-GPT2
   - Source: nlpconnect/vit-gpt2-image-captioning
   - Features: Combines Vision Transformer for image processing with GPT-2 for caption generation

2. **Translation Model**
   - Model: IndicTrans2
   - Source: ai4bharat/indictrans2-en-indic-1B
   - Features: Specialized for English to Indian language translations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Troubleshooting

Common issues and solutions:

1. **ModuleNotFoundError**:
   - Ensure you've activated the virtual environment
   - Run `pip install -r requirements.txt`

2. **Memory Issues**:
   - Reduce the maximum file size in app.config
   - Consider using model quantization

3. **Audio Generation Fails**:
   - Ensure you have write permissions in the uploads directory
   - Check internet connectivity for gTTS

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing the transformer models
- [AI4Bharat](https://ai4bharat.org/) for the translation model
- [Google Text-to-Speech](https://cloud.google.com/text-to-speech) for audio generation capabilities
