
        $("#started button").mouseover(function(){
            $("#started object:nth-child(2)").css("opacity", 0);
            $("#started object:nth-child(3)").css("opacity", 1);
        });
        $("#started button").mouseout(function(){
            $("#started object:nth-child(2)").css("opacity", 1);
            $("#started object:nth-child(3)").css("opacity", 0);
        });


        $(".page1").hide()
        $('.page2').fadeOut()
        $('.page3').fadeOut()
        $("body #skeleton").show()
        $(document).ready(function(){
            $(".page1").show()
            $("#welcome1").css("opacity", "1")
            $("body #skeleton").hide()
        });

