$(document).ready(function() {
    
    $(".bi-bookmark-plus-fill").click(function() {
       
        var recipeIdVar;
        recipeIdVar = $(this).attr('data-recipeid');

        var clickedBookmarkIcon=$(this);

        $.get('/recipes/bookmark/',
                {'recipe_id': recipeIdVar}, //data sent to view 
                
                function(data) { //after the function has been called 
                   
                    if (data == "Deleted"){
                        clickedBookmarkIcon.css({'fill' : "currentColor"});
                    }
                    else if (data== "Bookmarked"){
                        clickedBookmarkIcon.css({'fill' : "gold"});
                    }

                })
    })


    $(".btn-outline-danger").click(function() {
       
        var recipeIdVar;
        recipeIdVar = $(this).attr('data-recipeid');

        var clickedRecipe=$(this).closest('.col-md-4'); //get the closest div element for the card which contains the delete button
        
        $.get('/recipes/delete/',
        {'recipe_id': recipeIdVar}, //data sent to view 
        
        function(data) { //after the function has been called 
           
            clickedRecipe.remove();
            
        })
    })


    $('#like_btn').click(function() {
        var recipeIdVar;
        recipeIdVar = $(this).attr('data-recipeid');
        $.get('/recipes/like/',
            {'recipe_id': recipeIdVar},
            function(data) {
                $('#like_count').html(data);
                $('#like_btn').hide();
            })
    });
});


