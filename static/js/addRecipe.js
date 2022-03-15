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

    $("#addIngredientButton").click(function() {

        var ingredient = $("#IngredientNameField").val();
        var quantity = $("#IngredientQuantityField").val();

        $("#IngredientNameField").val( "" );
        $("#IngredientQuantityField").val( "" );
        
        if (ingredient!="" && quantity!=""){
            $('#IngredientNameField').css({'border' : ''}); //reset the border back to default
            $('#IngredientQuantityField').css({'border' : ''}); //reset the border back to default
            $('#ingredientlist').append("<li class='list-group-item'>"+ ingredient+", "+quantity+'<input type="button" class="deleteIngredient style="text-align: right" value="Delete"/></li>'); 
            $('#deleteIngredient').addClass("deleteIngredient")

        }
        else{
            $('#IngredientNameField').css({'border' : '1px solid red'}); //add a red line to show user error
            $('#IngredientQuantityField').css({'border' : '1px solid red'}); //add a red line to show user error

        }
    })

    $(document).on('click', '.deleteIngredient', function() {
        $(this).parent().remove();
    });

});



