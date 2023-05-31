$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: (movies) => {
      const moviesList = movies.results;
      $.each(moviesList, (i, movie) => {
        $('ul#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});
