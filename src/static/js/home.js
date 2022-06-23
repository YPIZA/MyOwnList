const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");
const themeToggler = document.querySelector(".theme-toggler");
const inputs = document.querySelectorAll(".input-field");
var Abrirpopup = document.getElementById("lola"), overlay = document.getElementById("overlay"), popup = document.getElementById("popup"), btncerrarpopup = document.getElementById("cpop");


menuBtn.addEventListener('click', () => {
    sideMenu.style.display = 'block';
})

closeBtn.addEventListener('click', () => {
    sideMenu.style.display = 'none';
})

themeToggler.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme-variables');
    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');
})

inputs.forEach(inp => {
    inp.addEventListener("focus", () => {
        inp.classList.add("active");
    });
    inp.addEventListener("blur", () => {
        if (inp.value != "") return;
        inp.classList.remove("active");
    });
})

Abrirpopup.addEventListener('click', () => {
    overlay.classList.add("active");
})

btncerrarpopup.addEventListener('click', () => {
    overlay.classList.remove("active");
})