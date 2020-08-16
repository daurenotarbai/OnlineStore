$(document).ready(function(){
    var form = $('.adding_blog_comment');
    console.log(form); 


        function update_comment_for_blog(blog_id,blog_review,username,comment_id){
            var data = {};
            data.blog_id = blog_id;
            data.blog_review = blog_review;
            data.comment_id = comment_id
            data.username = username;

            var csrf_token = $('.adding_blog_comment [name = "csrfmiddlewaretoken"]').val();
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
                    
                    $.each(data.comments, function(k,v){ 
                        $('.block-for-ul ul').append('<li class="comment-product-li"><div class="flex-w flex-t p-b-68"><div class="wrap-pic-s size-109 bor0 of-hidden m-r-18 m-t-6"><img src="/static/images/avatar-01.jpg" alt="AVATAR"></div><div class="size-207"><div class="flex-w flex-sb-m p-b-17"><span class="user_in_product_comment mtext-107 cl2 p-r-20">'+v.username+'</span><span class="fs-15 cl11"><a class="answer_comment" style="color: #888;" data-comment_id="'+comment_id+'">Answer</a></span><span class="fs-18 cl11"><form action="delete/'+comment_id+'" method="POST"><button type="submit" data-comment_id = "'+comment_id+'" class="delete-comment-for-blog fs-18 cl11" ><i style="color: #f9ba48;" class="zmdi zmdi-delete"></i></button></form></span></div><p class="stext-102 cl6">'+v.blog_review+'</p></div></div></li>')
                    })

                    $('.review_in_blog_comment').val(" ")
                    $('.name_in_comment').val(" ")
                    $('.email_in_comment').val(" ")

                

                    
                },
                error: function(data){
                    console.log("Error")

                },
            })
        }

        form.on('submit', function(e){
            e.preventDefault();
            console.log('123');
            var blog_review = $('.review_in_blog_comment').val();
            var blog_id = $('.blog_id_for_blog_comment').val();
            var comment_id 
            var username =$('.user_for_product_comment').text();
            console.log("blog_id",blog_id)

            update_comment_for_blog(blog_id,blog_review,username,comment_id)
        
        });


        $(document).on('click','.answer_comment',function(e){
            e.preventDefault();
            comment_id = $(this).data("comment_id")
            console.log("CommentID",comment_id)
            var username =$('.user_in_blog_comment_'+comment_id+'').text();

            $('.review_in_blog_comment').val("@"+username)
            $('#blog_review').focus();



    
        })


    
        // $(".comment_text_for_blog ").each(function() {
        //     var text = $(this).text();
        //     var first = $('<span>'+text.charAt(0)+'</span>').addClass('caps');
        //     $(this).html(text.substring(1)).prepend(first);
        //     });


});