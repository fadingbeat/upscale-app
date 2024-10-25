# Upscale-App

Upscale-App is a web application that enhances the quality of images by improving their resolution. This project utilizes advanced deep learning models, namely **EDSR_x4** (Enhanced Deep Super-Resolution) and **LapSRN_x8** (Laplacian Pyramid Super-Resolution Network), to upscale images and provide users with high-resolution outputs. The app is built using Python for the backend, and HTML, JQuery, and Ajax for the frontend.

## Features

- **Image Upload**: Users can upload their images to the application.
- **Image Upscaling**: The app enhances the image resolution using two advanced models:
  - **EDSR_x4**: A model designed to provide a 4x resolution enhancement.
  - **LapSRN_x8**: A model designed for 8x resolution enhancement.
- **Ajax-Based Image Processing**: Asynchronous requests ensure a smooth user experience without needing to reload the page.

## Technologies Used

### Backend:

- **Python**: The core language used for model implementation and image processing.
- **OpenCV**: For image manipulation and preprocessing.

### Frontend:

- **HTML**: Used to create the structure of the web pages.
- **JQuery**: For dynamic interactions and triggering image upload and processing.
- **Ajax**: To send asynchronous requests to the backend for processing the images.

## Models Used

### 1. EDSR_x4 (Enhanced Deep Super-Resolution)

EDSR is a state-of-the-art super-resolution model that enhances image quality by learning high-frequency details from low-resolution images. The **x4** version of the model upscales images by a factor of 4, improving fine details and textures without introducing significant artifacts.

- **Paper**: https://arxiv.org/abs/1707.02921
- **Features**:
  - Better detail retention for sharp images.
  - Avoids unnecessary batch normalization, improving the final image quality.
  - Ideal for general use cases.

### 2. LapSRN_x8 (Laplacian Pyramid Super-Resolution Network)

LapSRN is a progressive super-resolution model that reconstructs high-resolution images using a pyramid framework. The **x8** version upscales images by a factor of 8, allowing for more extreme upscaling while maintaining visual fidelity.

- **Paper**: https://arxiv.org/abs/1710.01992
- **Features**:
  - Multi-level pyramid structure for progressive image upscaling.
  - Efficient memory usage with better sharpness for extreme resolutions.
  - Ideal for images requiring large-scale upscaling.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/fadingbeat/upscale-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd upscale-app
   ```
3. Create virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate virtual environment:
   ```bash
   venv\Scripts\activate
   ```
   or
   ```bash
   ./Scripts/activate.bat
   ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run the application:
   ```bash
   python upscale.py
   ```

## Usage

1. Open your browser and navigate to `http://localhost:5000`.
2. Upload an image using the file input.
3. Click on the "Upscale Image" button.
4. Download or view the enhanced image once processing is complete.

Note: The image processing could take up to 15 minutes if you're running on a low computational laptop.

## Project Structure

```bash
upscale-app/
│
├── models/                 # Contains pre-trained model weights for EDSR_x4 and LapSRN_x8
├── static/                 # Static files like CSS and JS
├── templates/              # HTML templates for rendering web pages
├── upscale.py              # Main application script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Future Improvements

- Support for additional super-resolution models.
- Batch image processing.
- Integration of GPU support for faster image upscaling.
- Mobile-friendly UI enhancements.

---

Feel free to contribute to this project by submitting pull requests or reporting issues!
