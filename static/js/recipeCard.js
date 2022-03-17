$(document).ready(function() {
    
    $(".bi-bookmark-plus-fill").click(function() {
       
        var recipeIdVar;
        recipeIdVar = $(this).attr('data-categoryid');

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
});


