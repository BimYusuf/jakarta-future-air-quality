
        function openStatistic(){
            removeHome($("#started"), "right")
            removeHome($("#definition"), "left")
            removeHome($("#future"), "right")
            removeHome($("#welcome1"), "left")
            setTimeout(function(){
                $(".page2").fadeIn()
            }, 3000)
        }

        function removeHome(elem, dir){
            setTimeout(function(){
                if(dir === "left"){
                    elem.addClass("slideLeft")
                }else if(dir == "right"){
                    elem.addClass("slideRight")
                }
                elem.fadeOut()
                setTimeout(function(){
                    elem.hide();
                }, 2000);
            }, 2000);
        }
