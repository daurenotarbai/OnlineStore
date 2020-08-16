$(document).ready(function(){

    $('.js-addwish-b2').on('click', function(e){
        e.preventDefault();
    });

    $('.js-addwish-b2').each(function(){
        var nameProduct = $(this).parent().parent().find('.js-name-b2').html();
        $(this).on('click', function(){
            swal(nameProduct, "is added to wishlist !", "success");

            $(this).addClass('js-addedwish-b2');
            $(this).off('click');
        });
    });

    $('.js-deletewish-b2').on('click', function(e){
        e.preventDefault();
    });

    $('.js-deletewish-b2').each(function(){
        var nameProduct = $(this).parent().parent().find('.js-name-b2').html();
        $(this).on('click', function(){
            swal(nameProduct, "is deleted from wishlist !", "success");

            $(this).addClass('js-deletedwish-b2');
            $(this).off('click');
        });
    });

    $('.js-addwish-detail').each(function(){
        var nameProduct = $(this).parent().parent().parent().find('.js-name-detail').html();

        $(this).on('click', function(){
            swal(nameProduct, "is added to wishlist !", "success");

            $(this).addClass('js-addedwish-detail');
            $(this).off('click');
        });
    });



    // /---------------------------------------------/


        $(document).on('click','.wishlist_btn',function(e){
            e.preventDefault();
            var product_id = $(this).data("product_id")

            var data = {};
            data.product_id = product_id;
            is_delete = false;
            if (is_delete){
                data["is_delete"] = true; 
            }

            
            var csrf_token = $('.wishlist_btn [name = "csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;
            url = $('.wishlist_btn').attr("href")

            console.log(data);  
            $.ajax({
                url:url,
                type:'POST',
                data: data,
                cache:true,
                success: function(data){
                    console.log("OK");
                    console.log(data.wishlist_total_nmb);
                    $('.wishlist_total_number').text(data.wishlist_total_nmb);
                        console.log(data.products)

                    
                    

                },
                error: function(data){
                    console.log("Error")

                },
            })




    })

    $(document).on('click','.wishlist_btn_for_delete',function(e){
        e.preventDefault();
        var product_id = $(this).data("product_id")
        var is_delete = true;
        var data = {};
        data.product_id = product_id;
        
        if (is_delete){
            data["is_delete"] = true; 
        }

        
        var csrf_token = $('.wishlist_btn_for_delete [name = "csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        url = $('.wishlist_btn_for_delete').attr("href")

        console.log(data);  
        $.ajax({
            url:url,
            type:'POST',
            data: data,
            cache:true,
            success: function(data){
                console.log("OK");
                console.log(data.wishlist_total_nmb);
                $('.wishlist_total_number').text(data.wishlist_total_nmb);
                    console.log(data.products)

                
                

            },
            error: function(data){
                console.log("Error")

            },
        })




})
    


});












