const Countries = document.getElementById("Countries")

async function Paises() {
    await fetch('https://restcountries.eu/rest/v2/all')
    .then(response => response.json()).then(res => agregar(res))
}

function agregar(pais){
    pais.map((pais)=> {
        Countries.innerHTML += `
        <div class="card">
            <div class="card-content">
                <div class="media">
                <div class="media-left">
                    <figure class="image flag">
                    <img src="${pais.flag}" alt="Placeholder image">
                    </figure>
                </div>
                <div class="media-content">
                    <p class="title is-4">${pais.name}</p>
                    <p class="subtitle is-6">${pais.region}</p>
                </div>
                </div>

                <div class="content">
                    Capital: ${pais.capital}
                <br>
                    Poblacion: ${pais.population}
                <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
                </div>
            </div>
        </div>
    `
    })
}

Paises()