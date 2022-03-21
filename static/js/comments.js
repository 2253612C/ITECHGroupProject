$(document).ready(function() {
    
    


    $(".deleteComment").click(function() { //delete button for comments 
       
        var commentIdVar;
        commentIdVar = $(this).attr('data-commentid'); //get the comment which was clicked

        var clickedComment=$(this).closest('.commentParagraph'); //get the div element containing the comment
        
        $.get('/recipes/deleteComment/',
        {'comment_id': commentIdVar}, //data sent to view 
        
        function(data) { //after the function has been called 
           
            clickedComment.remove(); //remove the comment from the user view
            
        })
    })


    
});


