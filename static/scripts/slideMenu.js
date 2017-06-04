document.addEventListener("DOMContentLoaded", function () {
    "use strict";
    const slideMenu = document.getElementById("slider");
    const slideButton = document.getElementById("menu-title");
    const currText = slideButton.innerText;
    slideButton.addEventListener("click", function () {
        slideMenu.focus();
        slideMenu.classList.toggle("slide");
        slideButton.classList.toggle("slide-title");
        document.body.classList.toggle("slide-body");
        if (slideButton.innerText === currText) {
            slideButton.innerText = "Close";
        } else {
            slideButton.innerText = currText;
        }
    }, false);
});
