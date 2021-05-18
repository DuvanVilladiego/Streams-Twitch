// eventos con botones
const boton = document.getElementById("boton");

boton.addEventListener("click", () => {
    operacion()
});

// Operaciones con numeros enteros y decimales
operacion = () => {
    let num1 = parse(prompt("Digite un numero para sumar: "));
    let num2 = parse(prompt("Digite otro numero para sumar: "));
  
    incluir(num1 + " + " + num2 + " es igual a = " + (num1 + num2))
  }
  function parse(numero) {
    return parseFloat(parseFloat(numero).toFixed(2));
  }

// incluir operación en el DOM
const test = document.getElementById("test")

incluir = (pintar) => {
    test.innerHTML += "</br>" + pintar;
}
