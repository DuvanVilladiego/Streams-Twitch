const FileSaver = require('file-saver')
let boton = document.getElementById("boton")

function ImageCreate(){
	html2canvas([document.getElementById('imageContent')], {
		onrendered: function (canvas) {
			var img = canvas.toDataURL('image/png'); //o por 'image/jpeg' 
			//display 64bit imag
            FileSaver.saveAs(img, "Hamburguesa personal.png")
        }
	})
}

boton.addEventListener('click', () =>{
    ImageCreate()
})