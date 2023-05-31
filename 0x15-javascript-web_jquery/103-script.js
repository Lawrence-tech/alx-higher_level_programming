$(function () {
  $('input#btn_translate').bind('click', (e) => {
    $.ajax({
      type: 'GET',
      url:
        'https://fourtonfish.com/hellosalut/?lang=' +
        $('input#language_code').val(),
      success: (translation) => {
        $('div#hello').text(translation.hello);
      }
    });
  });

  $('input#language_code').bind('keypress', (e) => {
    if (e.which === 13) {
      $('input#btn_translate').click();
    }
  });
});
