# Image to PDF Converter

This project is a web application that allows users to convert image files (JPG, JPEG, PNG) to PDF format. The app uses Flask for the backend and JavaScript for the frontend interactions.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)
- [Customization](#customization)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/adityacheruku/image-to-pdf-converter.git
    cd image-to-pdf-converter
    ```

2. Create a virtual environment and install the required Python packages:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Install the necessary system packages for handling images:
    - **Pillow**: Used for image manipulation
    - **ReportLab**: Used for creating PDF files

4. Run the Flask application:
    ```sh
    python app.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Open the application in your browser.
2. Use the file input to select an image file (JPG, JPEG, or PNG).
3. Click the "Convert to PDF" button to upload the image and convert it to PDF.
4. If the conversion is successful, a download link for the PDF file will appear.

## File Structure


- **static/**: Contains static files such as JavaScript.
- **templates/**: Contains HTML templates.
- **app.py**: Flask application file.
- **main.py**: Contains additional functions for image processing.
- **requirements.txt**: Python dependencies.
- **README.md**: Documentation for the project.

## Dependencies

The project relies on the following external libraries and resources:

- [Flask](https://flask.palletsprojects.com/): A lightweight WSGI web application framework.
- [Pillow](https://python-pillow.org/): Python Imaging Library.
- [ReportLab](https://www.reportlab.com/): A software library that lets you directly create documents in Adobe's Portable Document Format (PDF).
- [JavaScript Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API): For handling HTTP requests on the client side.

## Customization

### HTML

The main structure of the converter application is defined in the `index.html` file. You can customize the appearance and layout by modifying the HTML elements and their attributes.

### CSS

Add styles to your application by creating a CSS file and linking it in the `index.html`.

### JavaScript

The core functionality for handling form submissions and interacting with the backend is implemented in `script.js`. You can enhance the app's capabilities or modify its behavior by updating the JavaScript code.

### Python

The backend logic is implemented in `app.py` and `main.py`. You can extend the functionality by adding more routes or modifying the existing ones.

#### Configuration

Update the paths for the upload and output directories in `app.py`:

```python
app.config['UPLOAD_FOLDER'] = 'path/to/uploads'
app.config['OUTPUT_FOLDER'] = 'path/to/output'
