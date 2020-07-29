
//Burger menu when clicked open side bar for phone
const navslide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-element');
    const navLinks = document.querySelectorAll('nav-element li');

    //toggle nav bar
    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active')
    });
}


//calling the function
navslide();



// saving the position in the form
document.addEventListener("DOMContentLoaded", function (event) {
    var scrollpos = sessionStorage.getItem('scrollpos');
    if (scrollpos) {
        window.scrollTo(0, scrollpos);
        sessionStorage.removeItem('scrollpos');
    }
});

window.addEventListener("beforeunload", function (e) {
    sessionStorage.setItem('scrollpos', window.scrollY);
});

// alert - saved!
function show_alert(){
    const txt = "ENTRY SAVED :), PRESS ENTER TO DISMISS";
    alert(txt);
}
