document.querySelector('.upload-form').addEventListener('submit', function(event) {
  event.preventDefault();

  const imageFileInput = document.querySelector('input[name="file"]');
  const imageFile = imageFileInput.files[0];

  if (imageFile) {
    const formData = new FormData();
    formData.append('file', imageFile);

    // Send the image file to the backend server
    fetch('http://127.0.0.1:5000', {
      method: 'POST',
      body: formData
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Image to PDF conversion failed.');
      }
    })
    .then(data => {
      if (data.success) {
        const downloadLink = document.createElement('a');
        downloadLink.href = data.fileUrl;
        downloadLink.download = 'converted.pdf';
        downloadLink.textContent = 'Download PDF';
        document.querySelector('.download-container').appendChild(downloadLink);
      } else {
        throw new Error('Image to PDF conversion failed.');
      }
    })
    .catch(error => {
      console.error(error);
      alert('Image to PDF conversion failed. Please try again.');
    });
  } else {
    alert('Please select an image file.');
  }
});
