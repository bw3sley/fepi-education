import { API_KEY, BASE_URL, IMG_URL, language } from "./api.js";

const findMovieButton = document.querySelector("#find-movie");

async function FindRandomMovie() {
    const randomMovieNumber = Math.floor(Math.random() * 1000);
    
    const url = `${BASE_URL}${randomMovieNumber}?${API_KEY}&${language}`;
    
    const requestStatus = await fetch(url).then(res => res.status);

    const movie = await fetch(url).then(res => res.json());

    const moviePoster = movie.poster_path;

    container_initial.classList.remove("initial");
    content.classList.remove("not-found");

    if(requestStatus == 404 || movie.overview == "" || moviePoster == "") {
        movie_title.innerHTML = "Ops, hoje não é dia de assistir filme. </br> Bora codar! 🚀";
        movie_poster.setAttribute("src", "./assets/code-screen.png");
        
        return content.classList.add("not-found");
    }

    const movieImage = await fetch(`${IMG_URL}${moviePoster}`);

    movie_overview.textContent = movie.overview;
    movie_title.textContent = movie.title;
    movie_poster.setAttribute("src", movieImage.url);
}

findMovieButton.addEventListener("click", FindRandomMovie);