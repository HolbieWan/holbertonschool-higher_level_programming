document.addEventListener('DOMContentLoaded', function () {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then((response) => response.json())
    .then((data) => {
      const movieList = document.getElementById('list_movies');
      for (let i = 0; i < data.results.length; i++) {
        let listItem = document.createElement('li');
        listItem.textContent = data.results[i].title;
        movieList.appendChild(listItem);
      }
    });
});
