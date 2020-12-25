$(document).ready(function(){
    var form = $('.task1_form');
    console.log(form); 
        function update_comment_for_blog(number1,number2,date,height,gender,fio,email,phone){
            var data = {};
            data.number1 = number1;
            data.number2 = number2;
            data.date = date
            data.height = height
            data.gender = gender
            data.fio = fio
            data.email = email
            data.phone = phone
        
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
                    
             
                        $('.summa').html(parseInt(number2)+parseInt(number1))
                        $('.age').html(date)
                        $('.ideal_weight').html("80")
                        $('.message').html("Successful!!!")
                        
                    
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
            var height = $('.height').val();
            var fio = $('.fio').val();
            var email = $('.email').val();
            var phone = $('.phone').val();
            update_comment_for_blog(number1,number2,date,height,fio,email,phone)
        
        });

});