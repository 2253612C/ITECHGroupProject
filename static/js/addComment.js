$(document).ready(function() {
    $('#submitComment').click(function(){

        if (!$("#CommentsForm")[0].checkValidity())
        {
            $('#CommentsForm')[0].reportValidity();
        }
        else
        {
    
            var content=$('#id_content').val();
            // var submissionDateTime=$('#id_submissionDateTime').val();
            var data= new FormData();
            data.append('content', content);
            // data.append('content', submissionDateTime);
            data.append('csrfmiddlewaretoken',$('input[name=csrfmiddlewaretoken]').val());
            
      
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