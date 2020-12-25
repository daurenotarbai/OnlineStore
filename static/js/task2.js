$(document).ready(function(){
    var form = $('.task1_form');
    console.log(form); 
        function update_comment_for_blog(date){
            var data = {};
            data.date = date;
            var csrf_token = $('.task1_form [name = "csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;

            var url = form.attr("action");
            console.log(data);  
            $.ajax({
                url:url,
                type:'POST',
                data: data,
                cache:true,
                success: function(data){
                    console.log("OK");
                    
                    $.each(data.task1_numbers, function(k,v){ 
                        $('.summa').html(parseInt(number2)+parseInt(number1))})
                    
                },
                error: function(data){
                    console.log("Error")
                },
            })
        }
        form.on('submit', function(e){
            e.preventDefault();
            console.log('123');
            var number1 = $('.number1').val();
            var number2 = $('.number2').val();
            var date = $('.date').val();


            update_comment_for_blog(number1,number2)
        
        });

});