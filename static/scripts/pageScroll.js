document.addEventListener("DOMContentLoaded", function () {
    "use strict";
    const button = document.getElementById("scroll-button");
    button.addEventListener("click", function (event) {
        const pageTop = 0;
        const moveTime = 900;
        const targetOffset = document.getElementById("graph-target").offsetTop;
        const currentPosition = window.pageYOffset;
        const distanceToMove = targetOffset - currentPosition;
        document.body.classList.add("in-transition");
        document.body.style.transform = `translate(0, -${distanceToMove}px)`;

        window.setTimeout(function () {
            document.body.classList.remove("in-transition");
            document.body.style.cssText = "";
            window.scrollTo(pageTop, targetOffset);
        }, moveTime);
        event.preventDefault();
    },
        false
    );
});
