window.onload=function(){ 
    // 初始化内容 
  $("#auto-height-0").css("height",$(window).height()-126 + 'px')
  $("#auto-height-1").css("height",$(window).height()-126 + 'px')
  



  var scrolled = $(window).scrollTop();
   
  if(scrolled > 10){
    $("#nav").removeClass("flat")
    $("#nav").addClass("float")
   }else{
      $("#nav").removeClass("float")
      $("#nav").addClass("flat")
   }

   if(scrolled > 373){
    $("#sidebar1").removeClass("affix-top")
    $("#sidebar1").addClass("affix")
   }else{
      $("#sidebar1").removeClass("affix")
      $("#sidebar1").addClass("affix-top")
   }



  if($('.postListsModel').width() != $('#article_big').width()){

      $("#sidebar1").css("width",$('.postListsModel').width() - $('#article_big').width() +'px');
      $(".custom-scrollbar-content").css("width",$('.postListsModel').width() - $('#article_big').width() +'px');
      
  }






}


$(window).resize(function () {          //当浏览器大小变化时
  // alert($(window).height());          //浏览器时下窗口可视区域高度
  // alert($(document).height());        //浏览器时下窗口文档的高度
  // alert($(document.body).height());   //浏览器时下窗口文档body的高度
  // alert($(document.body).outerHeight(true)); //浏览器时下窗口文档body的总高度 包括border padding margin 
  // console.log($(window).width() + "   haahahahh")
  // $("#auto-height-0").css("height",$(window).height()-126 + 'px')
  // $("#auto-height-1").css("height",$(window).height()-126 + 'px')
    $("#auto-height-0").css("height",$(window).height()-126 + 'px')
    $("#auto-height-1").css("height",$(window).height()-126 + 'px')






    var width_windows = $(window).width() + 17
    var isphone = false
    if(width_windows <= 991){
      isphone = true
    }

    if(isphone){
       $("#nav").removeClass("flat")
       $("#nav").addClass("float")
    }else{
        $(window).on('scroll',function(){
          "use strict";
           var scrolled = $(window).scrollTop();
          if(scrolled > 10){
            $("#nav").removeClass("flat")
            $("#nav").addClass("float")
           }else{
              $("#nav").removeClass("float")
              $("#nav").addClass("flat")
           }

           if(scrolled > 373){
            $("#sidebar1").removeClass("affix-top")
            $("#sidebar1").addClass("affix")
           }else{
              $("#sidebar1").removeClass("affix")
              $("#sidebar1").addClass("affix-top")
           }

        });
    }





  if($('.postListsModel').width() != $('#article_big').width()){

      $("#sidebar1").css("width",$('.postListsModel').width() - $('#article_big').width() +'px')
      $(".custom-scrollbar-content").css("width",$('.postListsModel').width() - $('#article_big').width() +'px')

  }






});







      $(window).on('scroll',function(){
        "use strict";

        var width_windows = $(window).width() + 17
        var isphone = false
        if(width_windows <= 991){
          isphone = true
        }

        if(isphone){
           $("#nav").removeClass("flat")
           $("#nav").addClass("float")
        }else{
            var scrolled = $(window).scrollTop();
            if(scrolled > 10){
              $("#nav").removeClass("flat")
              $("#nav").addClass("float")
             }else{
                $("#nav").removeClass("float")
                $("#nav").addClass("flat")
             }

            if(scrolled > 373){
            $("#sidebar1").removeClass("affix-top")
            $("#sidebar1").addClass("affix")
           }else{
              $("#sidebar1").removeClass("affix")
              $("#sidebar1").addClass("affix-top")
           }

        }



      });
  

	$(".tuijian-2").click(function(){
		$(".menu .anchor").css("left","43px")
		$("#sidebar-1").css("display","none")
		$("#sidebar-2").css("display","")
    $("#menu-id1").removeClass("active")
    $("#menu-id2").addClass("active")
		
	})
	$(".about-me-2").click(function(){
		$(".menu .anchor").css("left","1px")
		$("#sidebar-2").css("display","none")
		$("#sidebar-1").css("display","")
    $("#menu-id2").removeClass("active")
    $("#menu-id1").addClass("active")
	})

  $(".tuijian-3").click(function(){
    $(".menu .anchor").css("left","85px");
    $("#sidebar-0").css("display","none");
    $("#sidebar-1").css("display","none");
    $("#sidebar-2").css("display","");
    $("#menu-id0").removeClass("active");
    $("#menu-id1").removeClass("active");
    $("#menu-id2").addClass("active");
  })
  $(".about-me-3").click(function(){
    $(".menu .anchor").css("left","43px");
    $("#sidebar-0").css("display","none");
    $("#sidebar-2").css("display","none");
    $("#sidebar-1").css("display","");
    $("#menu-id0").removeClass("active");
    $("#menu-id2").removeClass("active");
    $("#menu-id1").addClass("active");
  })
  $(".directory-3").click(function(){
    $(".menu .anchor").css("left","1px");
    $("#sidebar-1").css("display","none");
    $("#sidebar-2").css("display","none");
    $("#sidebar-0").css("display","");
    $("#menu-id1").removeClass("active");
    $("#menu-id2").removeClass("active");
    $("#menu-id0").addClass("active");
  })

















  $(".phone-tuijian").click(function(){
    $(".phone-menu .anchor").css("left","43px")
    $("#phone-sidebar-1").css("display","none")
    $("#phone-sidebar-2").css("display","")
    $("#phone-menu-id1").removeClass("active")
    $("#phone-menu-id2").addClass("active")
    
  })
  $(".phone-about-me").click(function(){
    $(".phone-menu .anchor").css("left","1px")
    $("#phone-sidebar-2").css("display","none")
    $("#phone-sidebar-1").css("display","")
    $("#phone-menu-id2").removeClass("active")
    $("#phone-menu-id1").addClass("active")
  })


  // 手机端菜单栏点击事件
  $(".menuIcon").click(function(){

    if($('#wrapper-all').hasClass('menu-wrap-visible')){
        $("#wrapper-all").removeClass("menu-wrap-visible")
    }else{
        $("#wrapper-all").addClass("menu-wrap-visible")
    }


  })

  $("#phone-sider").click(function(){

    if($('#wrapper-all').hasClass('sidebar-visible')){
        $("#wrapper-all").removeClass("sidebar-visible")
    }else{
        $("#wrapper-all").addClass("sidebar-visible")
    }


  })

  $("#main").click(function(){
    if($('#wrapper-all').hasClass('sidebar-visible')){
        $("#wrapper-all").removeClass("sidebar-visible")
    }
  })




//最大化
  $(".toggle_sidebar").click(function(){
    if($('#article_big').hasClass('col-lg-9_5')){
      $("#article_big").removeClass("col-md-9");
      $("#article_big").removeClass("col-lg-9_5");
      $("#article_big").addClass("col-xs-12");
      $("#article_big").addClass("no-sidebar");
      $("#article_hidden").css("display","none");
      $("#bi-chevron-left").css("display","initial");
      $("#bi-chevron-right").css("display","none");
    }else{
      $("#article_big").addClass("col-md-9");
      $("#article_big").addClass("col-lg-9_5");
      $("#article_big").removeClass("no-sidebar");
      $("#article_big").removeClass("col-xs-12");
      $("#article_hidden").css("display","");
      $("#bi-chevron-left").css("display","none");
      $("#bi-chevron-right").css("display","");

    }
  })


  //评论区
  $(".nick-name").click(function(){


    $('#popover_guests').css('top',($('.nick-name').offset().top - 194) + 'px');
    $('#popover_guests').css('left',($('.nick-name').offset().left) + 'px');


    if($('#popover_guests').hasClass('hidden')){
      $("#popover_guests").removeClass("hidden");
    }else{
       $("#popover_guests").addClass("hidden");
    }
  })

























