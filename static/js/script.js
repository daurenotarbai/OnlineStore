$(document).ready(function(){

    

    $('.js-addcart-detail').each(function(){
        var nameProduct = $(this).parent().parent().parent().parent().parent().find('.js-name-detail').html();
        $(this).on('click', function(){
            swal(nameProduct, "is added to cart !", "success");
            console.log("it's w")
        });
    });

    $('.js-proceed-to-checkout').each(function(){
        
        $(this).on('click', function(){
            nameProduct = "Your order has been accepted!"
            swal(nameProduct, "Managers will contact you !", "success");
            console.log("it's w")
        });
    });

    var form = $('.form_buying_product');
    console.log(form); 

    function basketUpdating(product_id,product_size,product_color,nmb,is_delete,sum){
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        data.product_size = product_size;
        data.product_color = product_color;
        data.sum = sum;
         var csrf_token = $('.form_buying_product [name = "csrfmiddlewaretoken"]').val();
         data["csrfmiddlewaretoken"] = csrf_token;
        

        if (is_delete){
            data["is_delete"] = true; 
        }
         var url = form.attr("action");

        console.log(data);  
        $.ajax({
            url:url,
            type:'POST',
            data: data,
            cache:true,
            success: function(data){
                console.log("OK");
                console.log(data.products_total_nmb);
                $('.basket_total_number').text(data.products_total_nmb);
                 console.log(data.products)

                $('.header-cart-content ul').html('');
                var total_price_in_minibasket = 0;
                $.each(data.products, function(k,v){
                $('.header-cart-content ul').append('<li class="header-cart-item flex-w flex-t m-b-12"><div data-product_id = "'+v.id+'" class="delete-item header-cart-item-img"><img src="'+v.product_img +'" alt="IMG"></div><div class="header-cart-item-txt p-t-8"><a href="#" class="header-cart-item-name m-b-18 hov-cl1 trans-04">'+v.product_name+'</a><span class="color-size-in-minibasket header-cart-item-info">'+v.product_size+'<br>'+v.product_color+'<br></span><span class="price-in-minibasket header-cart-item-info"><span class="nmb_per_product">'+v.nmb+'</span>x<span class="price_per_product">'+v.product_price+'тг</span> тг</span></div></li>');
                
                // var current_nmb = parseFloat($('.header-cart-item').find('.nmb_per_product').text()).toFixed(2); 
                // var current_price = parseFloat($('.header-cart-item').find('.price_per_product').text()).toFixed(2);
                // var current_sum = current_nmb * current_price;
                total_price_in_minibasket +=sum;
                console.log("total_price_in_minibasket");
                console.log(total_price_in_minibasket);

                console.log("currrent_sum");
                console.log(sum);   
                $('.total_price_in_minibasket').text(total_price_in_minibasket);
                })







            },
            error: function(data){
                console.log("Error")

            },
        })


    }

    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');
        var nmb = $('.number').val();
        var current_nmb = parseFloat($('.header-cart-item').find('.nmb_per_product').text()).toFixed(2); 
        var product_size = $(this).closest('form').find('.pr_size').children("option:selected").val();
        var product_color = $(this).closest('form').find('.pr_color').children("option:selected").val();
    
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("name");
        var product_price = submit_btn.data("price");
        var product_category = submit_btn.data("category");
        var product_img = submit_btn.data("img");
        var sum = nmb * product_price;


        basketUpdating(product_id,product_size,product_color,nmb,is_delete = false,sum)
        
    });
    

    

    $('.icon-header-item').on('click', function(e){
        e.preventDefault();
    });


    $(document).on('click','.filter-link',function(e){

    
    })
    //deleting product in  mini-basket, basket  
    $(document).on('click','.delete-item',function(e){
        e.preventDefault();
        product_id = $(this).data("product_id")
        nmb = 0;
        var product_size = $(this).closest('form').find('.pr_size').children("option:selected").val();
        var product_color = $(this).closest('form').find('.pr_color').children("option:selected").val();
        var sum
        basketUpdating(product_id,product_size,product_color,nmb,is_delete = true,sum)

    })

    //updating total price in  basket 
    function calculatingnBasketAmount(){
        var total_order_amount = 0;
        $('.total-price-for-this-product').each(function(){
            total_order_amount +=parseFloat($(this).text());

        });
        $('.total_order_amount').html(parseFloat(total_order_amount).toFixed(2))
        $('.total_order_amount_input').val(parseFloat(total_order_amount).toFixed(2))
        
    };
    //button + and -
    $(document).on('click',".product-in-basket-nmb",function(){
        var current_input_nmb = parseFloat($(this).closest('tr').find('input').val()).toFixed(2);
        var current_tr = $(this).closest('tr');
        var current_price  = parseFloat(current_tr.find('.product_price').text());
        var total_price = parseFloat(current_input_nmb * current_price).toFixed(2);
        current_tr.find('.total-price-for-this-product').text(parseFloat(total_price).toFixed(2))
        console.log(total_price)
        calculatingnBasketAmount();
    });

    calculatingnBasketAmount();












});












