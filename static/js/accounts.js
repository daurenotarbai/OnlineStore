$("#check_name").click(function(){
  
  $.ajax({
    type: "GET",
    url: "check-username/",
    data:{
      'user_name': $("#username_input").val(),
    },
    dataType:"text",

    cache: false,

    success: function(data){
      if (data =='Ok') {
        console.log("Yes");
      }
      else if (data =='No'){
        console.log("No");

      }
    
    }

  });

})
