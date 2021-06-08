// CONTENEDOR DE IMAGENES
const imageContent = document.getElementById("imageContent")
const ingredients = document.getElementById("ingredients")

let boton = document.getElementById("boton");

// BOTONES DE INGREDIENTES - seran implementados luego
// let lechuga = document.getElementById("lechuga")
// let carne = document.getElementById("carne")
// let cebolla = document.getElementById("cebolla")
// let pepinillos = document.getElementById("pepinillos")
// let queso = document.getElementById("queso")
// let tomate = document.getElementById("tomate")

function ImageCreate() {
  html2canvas([imageContent], {
    onrendered: function (canvas) {
      let img = canvas.toDataURL("image/png"); //o por 'image/jpeg'
      //display 64bit imag
      let a = document.createElement("a");
      a.download = true;
      a.target = "_blank";
      a.href = img;
      a.click();
    },
  });
}

function addIngredient(ingrediente) {
	ingredients.innerHTML += `
	<img src="./assets/img/png/${ingrediente}.png" alt="">
	`
}


boton.addEventListener("click", () => {
  ImageCreate();
});
