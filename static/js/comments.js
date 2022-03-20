$(document).ready(function() {
    
    


    $(".deleteComment").click(function() { //delete button on recipe card when the user is on the 'my recipes' page
       
        var commentIdVar;
        commentIdVar = $(this).attr('data-commentid'); //get the recipe id which was clicked

        var clickedComment=$(this).closest('.commentParagraph'); //get the closest div element for the card which contains the delete button
        
        $.get('/recipes/deleteComment/',
        {'comment_id': commentIdVar}, //data sent to view 
        
        function(data) { //after the function has been called 
           
            clickedComment.remove(); //remove the recipe card from the user view
            
        })
    })


    
});


