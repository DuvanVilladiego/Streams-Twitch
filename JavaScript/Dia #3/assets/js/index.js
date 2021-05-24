// Agregar elementos con eventos en el DOM (Document Object Model)
// const botones = document.getElementById("botones")

// function addButton() {
//     botones.innerHTML += `<button onclick="addButton()"> Click Aqui </button>`
// }

// CICLO while

// let bandera = true
// let botones = document.getElementById("botones")
// var intervalo = () =>{
//     setInterval(add,1000)
// } 
// function stop() {
//     bandera = false
// }
// var add = () => {
//     botones.innerHTML += `<button onclick="stop()"> Click Aqui </button>`
//     if (bandera == false) {
//         clearInterval(intervalo)
//     }
// }
// intervalo()

let botones = document.getElementById("botones")
let bandera = true
function pararBucle(){
        bandera = false
}
var CrearBotones = function(){
    botones.innerHTML += `<button onclick="pararBucle()"> Click Aquí </button>`
    if(bandera == false){
        clearInterval(intervalo)
    }
}

var intervalo = setInterval(CrearBotones, 1000)

intervalo