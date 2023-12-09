var nav_dropDownMenu = document.getElementById("DownArrow");

var downArrow = false;

nav_dropDownMenu.addEventListener("click", function (){
    if(downArrow){
        var ul_nav = document.getElementById("ul_nav");
        ul_nav.classList.add("hidden");
        ul_nav.classList.add("overflow-hidden");
        downArrow = false;
    }else{
        var ul_nav = document.getElementById("ul_nav");
        ul_nav.classList.remove("hidden");
        ul_nav.classList.remove("overflow-hidden");
        downArrow = true;
    }

});

