$(document).ready(function() {
    
    var user_upload=false;

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

        user_upload=true;
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
            $('#ingredientlist').append("<li class='list-group-item'>"+ ingredient+", "+quantity+'<input type="button" class="deleteIngredient" value="Delete"/></li>'); 
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


    $('#submitRecipe').click(function(){

        if (!$("#recipeForm")[0].checkValidity()){
            $('#recipeForm')[0].reportValidity();
        }
        else if ($('#ingredientlist').children().length === 0 ){
            alert("Need to add at least 1 Ingredient to the recipe.");
            $('#IngredientNameField').css({'border' : '1px solid red'}); //add a red line to show user error
            $('#IngredientQuantityField').css({'border' : '1px solid red'}); //add a red line to show user error
            return false;
        }
        else if (!user_upload){
            alert("Need to upload an Image. (Click on the image box to upload an image)");
            return false;
        }

        else{
            $('#recipeForm').submit();
        }
        
        
    
    });
});



