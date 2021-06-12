// CONTENEDOR DE IMAGENES
let imageContent = document.getElementById("imageContent")
const ingredients = document.getElementById("ingredients")


//BOTONES DE INGREDIENTES - seran implementados luego
let lechuga = document.getElementById("lechuga")
let carne = document.getElementById("carne")
let cebolla = document.getElementById("cebolla")
let pepino = document.getElementById("pepino")
let queso = document.getElementById("queso")
let tomates = document.getElementById("tomates")

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

// generear imagen
imageContent.addEventListener("click", () => {
  ImageCreate();
});

// ingredientes
lechuga.addEventListener('click', () => {
  addIngredient('lechuga')
})

carne.addEventListener('click', () => {
  addIngredient('carne')
})

cebolla.addEventListener('click', () => {
  addIngredient('cebolla')
})

pepino.addEventListener('click', () => {
  addIngredient('pepino')
})

queso.addEventListener('click', () => {
  addIngredient('queso')
})

tomates.addEventListener('click', () => {
  addIngredient('tomates')
})