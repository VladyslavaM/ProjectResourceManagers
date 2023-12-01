$(document).ready(function() {
  // Переключення між вкладками
  $('.tab a').on('click', function(e) {
    e.preventDefault();
    $(this).parent().addClass('active');
    $(this).parent().siblings().removeClass('active');
    var target = $(this).attr('href');
    $('.tab-content > div').not(target).hide();
    $(target).fadeIn(600);
  });

  // Підсвічування та анімація міток полів вводу
  $('.form').find('input, textarea').on('keyup blur focus', function(e) {
    var $this = $(this);
    var label = $this.prev('label');

    if (e.type === 'keyup') {
      if ($this.val() === '') {
        label.removeClass('active highlight');
      } else {
        label.addClass('active highlight');
      }
    } else if (e.type === 'blur') {
      if ($this.val() === '') {
        label.removeClass('active highlight');
      } else {
        label.removeClass('highlight');
      }
    } else if (e.type === 'focus') {
      if ($this.val() === '') {
        label.removeClass('highlight');
      } else if ($this.val() !== '') {
        label.addClass('highlight');
      }
    }
  });

  // Обробка форми реєстрації
   $('#signup-form').submit(function(event) {
    event.preventDefault();

    // Збір CSRF токену
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();

    $.ajax({
      url: '/signup/',  // Замініть це на ваш URL для реєстрації
      type: 'POST',
      data: $(this).serialize(),
      headers: {'X-CSRFToken': csrftoken},  // Додайте CSRF токен у заголовки
      success: function(response) {
        // Обробка успішного виконання
        console.log(response);
      },
      error: function(error) {
        // Обробка помилок
        console.log(error);
      }
    });
  });

  // Обробка форми входу
  $('#login-form').submit(function(event) {
    event.preventDefault();

    // Збір CSRF токену
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();

    $.ajax({
      url: '/login/',  // Замініть це на ваш URL для входу
      type: 'POST',
      data: $(this).serialize(),
      headers: {'X-CSRFToken': csrftoken},  // Додайте CSRF токен у заголовки
      success: function(response) {
        // Обробка успішного виконання
        console.log(response);
      },
      error: function(error) {
        // Обробка помилок
        console.log(error);
      }
    });
  });
});