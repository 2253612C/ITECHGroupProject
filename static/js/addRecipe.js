$(document).ready(function() {
    
    $("#uploadImage").change(function() {
        const preview = document.querySelector('#imagefield');
  const file = document.querySelector('input[type=file]').files[0];
  const reader = new FileReader();

  reader.addEventListener("load", function () {
    // convert image file to base64 string
    preview.src = reader.result;
  }, false);

  if (file) {
    reader.readAsDataURL(file);
  }
    }
    )
});

