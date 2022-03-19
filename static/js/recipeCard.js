$(document).ready(function() {
    
    $(".bookmarkButton").click(function() {
       
        var recipeIdVar;
        recipeIdVar = $(this).attr('data-recipeid'); //get the recipe id which was clicked

        var clickedBookmarkIcon=$(this); //save which bookark button was clicked 

        $.get('/recipes/bookmark/',
                {'recipe_id': recipeIdVar}, //send id to view
                
                function(data) { //after the function has been called 
                   
                    if (data == "Deleted"){
                        clickedBookmarkIcon.removeClass('btn-outline-warning').addClass('btn-outline-secondary'); //change the bookmark button to normal colour 
                    }
                    else if (data== "Bookmarked"){
                        clickedBookmarkIcon.removeClass('btn-outline-secondary').addClass('btn-outline-warning'); //change the bookmark button to highlighted colour 
                    }

                })
    })


    $(".btn-outline-danger").click(function() { //delete button on recipe card when the user is on the 'my recipes' page
       
        var recipeIdVar;
        recipeIdVar = $(this).attr('data-recipeid'); //get the recipe id which was clicked

        var clickedRecipe=$(this).closest('.col-md-4'); //get the closest div element for the card which contains the delete button
        
        $.get('/recipes/delete/',
        {'recipe_id': recipeIdVar}, //data sent to view 
        
        function(data) { //after the function has been called 
           
            clickedRecipe.remove(); //remove the recipe card from the user view
            
        })
    })


    $('.likeButton').click(function() { //like button on recipe card
        var recipeIdVar;
        recipeIdVar = $(this).attr('data-recipeid'); //get clicked recipe 

        var clickedLikeButton=$(this);

        $.get('/recipes/like/',
            {'recipe_id': recipeIdVar},
            function(data) {
                clickedLikeButton.children('.visually-hidden').text(data); //update the like number
                clickedLikeButton.removeClass('btn btn-outline-secondary').addClass('btn btn-outline-warning'); //changed the button from normal color to yellow
                clickedLikeButton.css("pointer-events","none"); //make the button non-clickable 
            })
    });
});


