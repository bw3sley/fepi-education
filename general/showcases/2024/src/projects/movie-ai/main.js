const options = {
    method: 'GET',
    headers: {
      accept: 'application/json',
      Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NDk2NzJmZmJhNjc2ZTY3M2I0NThhNjRhNTlmM2ViMSIsInN1YiI6IjY0ZDFjNjlhOTQ1ZDM2MDEzOTRlZGVkYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.d9VbTvwI3A-5us7FALA2cAgaAWFd7XE_ieXJKKwADPQ'
    }
}

async function getMovies() {
    try {
      return fetch('https://api.themoviedb.org/3/movie/popular', options)
        .then(response => response.json())
    }
    
    catch (error) {
      console.error(error)
    }
}
  
  // https://api.themoviedb.org/3/movie/{movie_id}
async function getMoreInfo(id) {
    try {
      return fetch('https://api.themoviedb.org/3/movie/' + id, options)
        .then(response => response.json())
    } 
    
    catch (error) {
      console.log(error)
    }
}
  
  // https://api.themoviedb.org/3/movie/{movie_id}/videos
async function watch(e) {
    const movie_id = e.currentTarget.dataset.id
    
    try {
      const data = await fetch(`https://api.themoviedb.org/3/movie/${movie_id}/videos`, options)
        .then(response => response.json())
  
      const { results } = data
  
      const youtubeVideo = results.find(video => video.type === "Trailer")
  
      window.open(`https://youtube.com/watch?v=${youtubeVideo.key}`, 'blank')
  
    } 
    
    catch (error) {
      console.error(error)
    }
}
  
function createMovieLayout({
    id,
    title,
    stars,
    image,
    time,
    year
}) {
    return `
        <div class="movie">
          <div class="title">
              <span title="${title}">${title}</span>
      
              <div>
                <img src="./assets/icons/Star.svg" alt="">
      
                <p>${stars}</p>
              </div>
          </div>
    
          <div class="poster">
              <img src="https://image.tmdb.org/t/p/w500${image}" alt="Imagem de ${title}">
          </div>
    
          <div class="info">
              <div class="duration">
                <img src="./assets/icons/Clock.svg" alt="">
        
                <span>${time}</span>
              </div>
      
              <div class="year">
                <img src="./assets/icons/CalendarBlank.svg" alt="">
        
                <span>${year}</span>
              </div>
          </div>
    
          <button onclick="watch(event)" data-id="${id}">
              <img src="./assets/icons/Play.svg" alt="">
      
              <span>Assistir Trailer</span>
          </button>
        </div>
    `
}
  
function select3Videos(results) {
    const random = ()=> Math.floor(Math.random() * results.length);

    let selectedVideos = new Set();

    while (selectedVideos.size < 3) {
        selectedVideos.add(results[random()].id);
    }

    return [...selectedVideos];
}

function minutesToHourMinutesAndSeconds(minutes) {
    const date = new Date(null);
    
    date.setMinutes(minutes);
    
    return date.toISOString().slice(11, 19);
}
  
async function start() {
    const { results } = await getMovies();

    const best3 = select3Videos(results).map(async movie => {
        const info = await getMoreInfo(movie);

        const props = {
            id: info.id,
            title: info.title,
            stars: Number(info.vote_average).toFixed(1),
            image: info.poster_path,
            time: minutesToHourMinutesAndSeconds(info.runtime),
            year: info.release_date.slice(0, 4)
        }

        return createMovieLayout(props);
    })

    const output = await Promise.all(best3);

    document.querySelector('.movies').innerHTML = output.join("");
}
  
start()