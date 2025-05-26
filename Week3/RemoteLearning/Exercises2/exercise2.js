var i = 0;
var isClicked = false;

const myMove = () => {
    const anime = document.getElementById("animate");
    
    if (isClicked) {
        clearInterval(interval);
        isClicked = false;
        return;
    }
    
    isClicked = true;
    interval = setInterval(() => {
        if (i <= 8) {
            if (i === 8)
                i = 0;
            anime.style.marginLeft = 50 * i + "px";
            i++;
        } else 
            i = 0;
    }, 150);
};
