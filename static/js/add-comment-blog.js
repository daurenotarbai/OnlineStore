$(document).ready(function(){
    var form = $('.adding_blog_comment');
    console.log(form); 


        function update_comment_for_blog(blog_id,comment_text,username,comment_id,parent){
            var data = {};
            data.blog_id = blog_id;
            data.comment_text = comment_text;
            data.comment_id = comment_id
            data.username = username;
            data.parent = parent

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
                        $('.block-for-ul ul').append('<li class="comment-product-li"><div class="flex-w flex-t p-b-68"><div class="wrap-pic-s size-109 bor0 of-hidden m-r-18 m-t-6"><img src="/static/images/avatar-01.jpg" alt="AVATAR"></div><div class="size-207"><div class="flex-w flex-sb-m p-b-17"><span class="user_in_product_comment mtext-107 cl2 p-r-20">'+v.username+'</span><span class="fs-15 cl11"><a class="answer_comment" style="color: #888;" data-comment_id="'+comment_id+'">Answer</a></span><span class="fs-18 cl11"><form action="delete/'+comment_id+'" method="POST"><button type="submit" data-comment_id = "'+comment_id+'" class="delete-comment-for-blog fs-18 cl11" ><i style="color: #f9ba48;" class="zmdi zmdi-delete"></i></button></form></span></div><p class="stext-102 cl6">'+v.comment_text+'</p></div></div></li>')})
                        // <div class="flex-w flex-t p-b-68 p-l-28"><div class="wrap-pic-s size-109 bor0 of-hidden m-r-18 m-t-6"><img src="/static/images/avatar-01.jpg" alt="AVATAR"></div><div class="size-207"><div class="flex-w flex-sb-m p-b-17"><span class="user_in_blog_comment_{{el.id}} mtext-107 cl2 p-r-20">'+v.username+'</span><span class="fs-15 cl11"><a class="answer_commentt" style="color: #888;" onclick="addReview('+v.username+','+comment_id+')" data-comment_idd = "{{el.id}}" href="#formBlogComment">Answer</a></span><span class="fs-18 cl11">{%if request.user == el.user%}<form action="/blog/delete-comment/{{el.id}}" method="POST"><button type="submit"  class="delete-comment-for-blog fs-18 cl11" ><i style="color: #f9ba48;" class="zmdi zmdi-delete"></i></button></form>{%endif%}</span></div><p class="comment_text_for_blog stext-102 cl6">{{el.comment_text}}</p></div></div>
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
            var comment_text = $('.review_in_blog_comment').val();
            var blog_id = $('.blog_id_for_blog_comment').val();
            var comment_id 
            var username =$('.user_for_product_comment').text();
            var parent =$('.parent_comment').val();

            console.log("Parent",parent)

            update_comment_for_blog(blog_id,comment_text,username,comment_id,parent)
        
        });


        // $(document).on('click','.answer_comment',function(e){
        //     e.preventDefault();
        //     comment_id = $(this).data("comment_id")
        //     console.log("CommentID",comment_id)
        //     var username =$('.user_in_blog_comment_'+comment_id+'').text();

        //     $('.review_in_blog_comment').val("@"+username)
        //     $('#blog_review').focus();



    
        // })


    
        // $(".comment_text_for_blog ").each(function() {
        //     var text = $(this).text();
        //     var first = $('<span>'+text.charAt(0)+'</span>').addClass('caps');
        //     $(this).html(text.substring(1)).prepend(first);
        //     });


});