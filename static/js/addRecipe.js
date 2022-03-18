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

            var button_html="<button type=\"button\" class=\"btn btn-outline-danger deleteIngredient value = Delete\"><svg xmlns=http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" fill=\"currentColor\" class=\"bi bi-trash3-fill\" viewBox=\"0 0 16 16\"><path d=\"M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5Zm-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5ZM4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06Zm6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528ZM8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5Z\"></path></svg></button>"

            $('#ingredientlist').append("<li class='list-group-item'>"+ ingredient+", "+quantity+button_html+"</li>"); 
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
        else if($('#imagefield').attr('src') == "static\images\blankimage.png") {
            alert("Need to upload an Image. (Click on the image box to upload an image)");
            return false;
        }

        else{

            var recipeName=$('#id_recipeName').val();
            var category=$('#id_category').val();
            var description=$('#id_description').val();
            var cookTime=$('#id_cookTime').val();
            var servings=$('#id_servings').val();
            var difficulty=$('#id_difficulty').val();
            var method=$('#id_method').val();

            var data= new FormData();
            data.append('recipeName', recipeName);
            data.append('category',category);
            data.append('description',description);
            data.append('cookTime',cookTime);
            data.append('servings',servings);
            data.append('difficulty',difficulty);
            data.append('method',method);
            data.append('image',document.querySelector('input[type=file]').files[0]);
            data.append('csrfmiddlewaretoken',$('input[name=csrfmiddlewaretoken]').val());
            
            var ingredients_arr=[];
            $('#ingredientlist li').each(function(n,v){
                var text=$(v).text()
                text=text.replace(/(\r\n|\n|\r)/gm, ""); //clear any return or newlines
                text=text.trim(); //remove whitespace from both ends
                ingredients_arr.push(text);
            });

            for (var i = 0; i < ingredients_arr.length; i++) {
                data.append('ingredients_arr[]', ingredients_arr[i]);
            }
              
      
            $.ajax({
                url: '',  //server script to process data
                type: 'POST',
                data: data,
                cache: false,
                contentType: false,
                processData: false
            }).done(function (data){

                if (data.success){
                    window.location.href = data.url;
                }
                else{
                    document.write(data.html);
                }
                
            });
        }
    });
});



