// для секции
function show_hide(id){
    var node = document.getElementById(id);
    var parentNode = node.parentNode;
    var ch = parentNode.children[1];

    display = ch.style.display;
    if (display == "block"){
        ch.style.display = "none";
    } 
    else{
        ch.style.display = "block";
    }
}

// раскрыть/собрать все секции
function show_hide_all(id){
    var val = document.getElementById(id).innerText;
    console.log(val);
    var divs = document.querySelectorAll("div.container[style^='display']");
    console.log(divs);
    document.getElementById(id).innerText = "show all";''

    var target = "none";
    if (val == "show all"){
        target = "block";
        document.getElementById(id).innerText = "hide all";
    }
    
    for (var i = 0; i < divs.length; i++){
        divs[i].style.display = target;
    }
}