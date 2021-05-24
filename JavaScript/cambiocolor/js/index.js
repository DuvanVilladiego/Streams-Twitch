let body = document.getElementById("body")
let header = document.getElementById("header")
let iframe = document.getElementById("iframe")
let boton = document.getElementById("boton")

let cambiocolor = (container,atributo,rojo,verde,azul) => {
    container.setAttribute("style",`${atributo}:rgb(${rojo},${verde},${azul});`);
}

let random = () => {
    return parseInt(Math.random() * (256 - 1) + 1)
}

function test(container,atributo) {
    cambiocolor(container,atributo,random(),random(),random())
}

function enableFrame() {
    iframe.setAttribute("style","display: unset !important")
    boton.setAttribute("style","display: none !important")
}

var inter = window.setInterval(test,1000,body,"background-color")
var interno = window.setInterval(test,500,header,"color")