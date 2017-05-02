document.addEventListener("DOMContentLoaded", function() {
        var x = document.getElementsByClassName('navlink')
        for (var i = 0; i < x.length; i++) {
                x[i].addEventListener("click", function(){
                        var selectedEl = document.querySelector(".current");
                        if(selectedEl){
                                selectedEl.classList.remove("current");
                        }
                        this.classList.add("current");
                }, false);;
        }
});
