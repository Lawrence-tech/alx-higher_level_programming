$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: (translation) => {
      $('div#hello').text(translation.hello);
    }
  });
});
