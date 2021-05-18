// Operaciones con numeros enteros y decimales
function llamar() {
  let num1 = parse(prompt("Digite un numero para sumar: "));
  let num2 = parse(prompt("Digite otro numero para sumar: "));
  alert(num1 + " + " + num2 + " es igual a = " + (num1 + num2));
}

function parse(numero) {
    return parseFloat(parseFloat(numero).toFixed(2));
}

// eventos con botones
const boton = document.getElementById("boton");

boton.addEventListener("click", () => {
    llamar()
});
