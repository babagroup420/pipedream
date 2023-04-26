from flask import Flask, request, send_file
import os

app = Flask(__name__)

# Route for uploading a file
@app.route('/upload', methods=['POST'])
def upload():
    # Check if file was uploaded
    if 'file' not in request.files:
        return 'No file uploaded.', 400

    file = request.files['file']
    filename = file.filename

    # Save file to uploads directory
    file.save(os.path.join('uploads', filename))

    return 'File uploaded successfully!'

# Route for downloading a file
@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    try:
        # Get the file path from the uploads directory
        file_path = os.path.join('uploads', filename)
        # Send the file as a download attachment
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return str(e), 404

if __name__ == '__main__':
    # Create the uploads directory if it doesn't exist
    if not os.path.exists('uploads'):
        os.mkdir('uploads')

    app.run(debug=True)
