$(document).ready(function() {
    
    $("#imagefield").click(function() {
        $("#uploadImage").click(); //run the function to execute the upload image button when clicking the image frame
    })

    //based on example at https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsDataURL
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

    var list_items=[];
    $("#addIngredientButton").click(function() {
        $('#ingredientlist').append("<li class='list-group-item'> test </li>"); 
    })

});



