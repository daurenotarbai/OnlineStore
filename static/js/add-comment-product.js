$(document).ready(function(){
    var form = $('.adding_product_comment');
    console.log(form); 


        function update_comment_for_product(product_id,review,rating,username,comment_id){
            var data = {};
            data.product_id = product_id;
            data.review = review;
            data.rating = rating;
            data.comment_id = comment_id

            data.username = username;

            var csrf_token = $('.adding_product_comment [name = "csrfmiddlewaretoken"]').val();
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

                        $('.block-for-ul ul').append('<li class="comment-product-li-'+v.comment_id+' comment-product-li-'+v.rating+'"><div class="flex-w flex-t p-b-68"><div class="wrap-pic-s size-109 bor0 of-hidden m-r-18 m-t-6"><img src="/static/images/avatar-01.jpg" alt="AVATAR"></div><div class="size-207"><div class="flex-w flex-sb-m p-b-17"><span class="user_in_product_comment mtext-107 cl2 p-r-20">'+v.username+'</span><span class="fs-18 cl11"><i id="star_1"></i><i id="star_2"></i><i id="star_3"></i><i id="star_4"></i><i id="star_5"></i></span><span class="fs-18 cl11"></span><a href="delete/'+v.comment_id+'"><span data-comment_id="'+v.comment_id+'" class="delete-comment-for-product fs-18 cl11"> <i style="color: #f9ba48;" class="zmdi zmdi-delete"></i></span></a></div><p class="stext-102 cl6">'+v.review+'</p></div></div></li>');
  
                    })

                    //$('.wrap-rating').html("<span class='wrap-rating fs-18 cl11 pointer'></i><i class='item-rating pointer zmdi zmdi-star-outline'></i></i><i class='item-rating pointer zmdi zmdi-star-outline'></i></i><i class='item-rating pointer zmdi zmdi-star-outline'></i></i><i class='item-rating pointer zmdi zmdi-star-outline'></i></i><i class='item-rating pointer zmdi zmdi-star-outline'></i><input required class='rating_in_comment dis-none' type='number' name='rating'></span>")
                    $('.review_in_comment').val(" ")


                

                    
                },
                error: function(data){
                    console.log("Error")

                },
            })
        }

        form.on('submit', function(e){
            e.preventDefault();
            console.log('123');
            var i;
            var review = $('.review_in_comment').val();
            var rating = $('.rating_in_comment').val();
            var product_id = $('.product_id_for_product_comment').val();
            var comment_id
            var username =$('.user_for_product_comment').text();
            console.log("product_id",product_id)
            update_comment_for_product(product_id,review,rating,username,comment_id)
        
        });
    
        // $(document).on('click','.delete-comment-for-product',function(e){
        //     e.preventDefault();
        //     var username_req =$('.user_for_product_comment').text();
        //     var username_commment = $('.user_in_product_comment').text();



    
        // })



});