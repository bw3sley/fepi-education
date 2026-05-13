async function fetchPokemon(pokemonId) {
    const API_URL = "https://pokeapi.co/api/v2/pokemon";

    try {
        const pokemon = await fetch(`${API_URL}/${pokemonId}`);
        const data = await pokemon.json();
  
        const newPokemon = {
          id: data.id,
          name: data.name,
          imageUrl: data["sprites"]["versions"]["generation-v"]["black-white"]["animated"]["front_default"],
        }

        createPokemon(newPokemon);
    }
  
    catch (error) {
        console.error("Failed to fetch Pokemon: ", error);
    }
} 

function createPokemon(newPokemon) {
    const pokemonId = document.querySelector(".pokemonNumber");
    pokemonId.textContent = newPokemon.id;

    const pokemonName = document.querySelector(".pokemonName");
    pokemonName.textContent = newPokemon.name;

    const pokemonImage = document.querySelector(".pokemonImage");
    pokemonImage.src = newPokemon.imageUrl;
}

const input = document.querySelector("input");

input.oninput = (event) => {
    if (input.value.length > 3) {
        setTimeout(() => {
            fetchPokemon(event.target.value);
        }, 1000)
    }
}

const nextButton = document.querySelector(".buttonNext");
const previousButton = document.querySelector(".buttonPrev");

nextButton.addEventListener("click", () => {
    const currentPokemonId = Number(document.querySelector(".pokemonNumber").textContent);
    const newPokemonId = currentPokemonId + 1;

    fetchPokemon(newPokemonId);
})

previousButton.addEventListener("click", () => {
    const currentPokemonId = Number(document.querySelector(".pokemonNumber").textContent);
    const newPokemonId = currentPokemonId - 1;

    fetchPokemon(newPokemonId);
})
