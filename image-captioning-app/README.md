# Image Captioning Web Application

This is a Flask-based web application that generates captions for uploaded images using a Vision Transformer (ViT) and GPT-2 model.

## Features

- Image upload functionality
- Real-time image preview
- Automatic caption generation
- Responsive web design using Tailwind CSS
- Error handling and user feedback

## Technical Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, JavaScript, Tailwind CSS
- **Machine Learning**: PyTorch, Transformers
- **Model**: ViT-GPT2 for image captioning
- **Deployment**: Render (or similar platform)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd image-caption-app
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Locally

1. Start the Flask application:
```bash
python app.py
```

2. Open a web browser and navigate to `http://localhost:5000`

## Deployment

The application can be deployed to Render using the following steps:

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

## Usage

1. Access the web application
2. Click "Upload a file" to select an image
3. Preview the selected image
4. Click "Generate Caption" to get the AI-generated caption
5. View the generated caption or any error messages

## Model Details

The application uses the `nlpconnect/vit-gpt2-image-captioning` model, which combines:
- Vision Transformer (ViT) for image feature extraction
- GPT-2 for caption generation

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

MIT License

## Acknowledgments

- Thanks to the Hugging Face team for the transformers library
- Thanks to the creators of the ViT-GPT2 model