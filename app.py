from PIL import Image
import os
from flask import Flask, request, send_file, send_from_directory, render_template


app = Flask(__name__)

def combine_images_to_pdf(image_file_paths, pdf_file_path):
    c = canvas.Canvas(pdf_file_path, pagesize=letter)

    for image_path in image_file_paths:
        img = Image.open(image_path)
        img_width, img_height = img.size
        c.setPageSize((img_width, img_height))
        c.drawImage(image_path, 0, 0, width=img_width, height=img_height)
        c.showPage()

    c.save()

def convert_images_to_pdf(image_file_paths, output_directory):
    num_images = len(image_file_paths)
    if num_images > 0:
        if num_images == 1:
            # Convert single image to PDF
            image_path = image_file_paths[0]
            image_name = os.path.splitext(os.path.basename(image_path))[0]
            pdf_file_path = os.path.join(output_directory, image_name + ".pdf")

            # Open the image and convert it to PDF
            image = Image.open(image_path)
            image.save(pdf_file_path, "PDF", resolution=100.0)

            return pdf_file_path
        else:
            # Convert multiple images to a combined PDF
            output_pdf_name = "combined.pdf"
            pdf_file_path = os.path.join(output_directory, output_pdf_name)

            # Create a new PDF document
            pdf = Image.new("RGB", (100, 100))  # Adjust the dimensions as per your requirement

            for image_path in image_file_paths:
                # Open each image and append it to the PDF document
                image = Image.open(image_path)
                pdf_page = Image.new("RGB", image.size)
                pdf_page.paste(image)
                pdf.paste(pdf_page)

            # Save the combined PDF
            pdf.save(pdf_file_path, "PDF", resolution=100.0)

            return pdf_file_path
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def convert_to_pdf():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename != '':
            # Save the uploaded image file
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image_path)

            # Convert image to PDF
            pdf_file_path = convert_images_to_pdf([image_path], app.config['OUTPUT_FOLDER'])
            if pdf_file_path:
                return send_file(pdf_file_path, as_attachment=True)

    return render_template('index.html')


@app.route('/output/<filename>')
def serve_pdf(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)




if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'C:\\Users\\saiad\\OneDrive\\Documents\\509\\db\\uploads'  # Specify the folder to store uploaded files
    app.config['OUTPUT_FOLDER'] = 'C:\\Users\\saiad\\OneDrive\\Documents\\509\\db\\output'  # Specify the folder to store the generated PDF file
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)
    app.run()
