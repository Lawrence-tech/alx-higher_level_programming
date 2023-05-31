$(function () {
  $('div#add_item').bind('click', (e) => {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('div#remove_item').bind('click', () => {
    $('ul.my_list > li').last().remove();
  });

  $('div#clear_list').bind('click', () => {
    $('ul.my_list').empty();
  });
});
