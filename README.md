﻿# ProjectResourceManager
Технічне завдання:

Тема: Веб-додаток для управління ресурсами проекту.

Технічне завдання:

Загальний опис: Веб-додаток , який допоможе команді проекту ефективно управляти ресурсами, включаючи людей, обладнання, бюджет та час, для забезпечення успішного завершення проекту вчасно та з відповідністю до поставлених завдань.

Основні функції: 
- Управління проектами:
	Створення, редагування та видалення проектів.
	Призначення менеджерів для проектів.
	Відстеження статусу та прогресу проектів.
-Управління завданнями:
	Додавання та редагування завдань в рамках проектів.
	Встановлення термінів та пріоритетів для завдань.
	Призначення виконавців для завдань.
	Відстеження статусу та прогресу завдань.
-Управління ресурсами:
Реєстрація користувачів з відповідними ролями (адміністратори, менеджери проекту, виконавці).
Планування та використання людських та матеріальних ресурсів.
Відстеження бюджету та витрат.

Допоміжні функції: 
- Звітність та аналітика
Додаток повинен надавати можливість генерувати звіти та аналізи щодо використання ресурсів, продуктивності користувачів і статусу проектів.
-  Повідомлення та сповіщення
Додаток повинен мати систему повідомлень та сповіщень для інформування користувачів про оновлення, нагадування про завдання та іншу важливу інформацію.

Функціональні вимоги: 
-Управління проектами:
-Створення нового проекту з вказанням назви, опису та інших характеристик.
-Редагування існуючих проектів, включаючи зміну назви, опису, статусу тощо.
-Видалення проектів з можливістю відновлення (софт-джерело).
-Управління завданнями:
-Додавання завдань в межах проекту з вказанням назви, опису, терміну виконання, пріоритету тощо.
-Редагування існуючих завдань, включаючи зміну деталей та відстеження статусу.
-Призначення виконавців для кожного завдання та можливість зміни виконавця.
-Відображення списку завдань та їх статусів для кожного проекту.
-Управління ресурсами:
-Реєстрація користувачів з вказанням інформації про їх ролі та права доступу (адміністратор, менеджер проекту, виконавець).
-Планування та відстеження використання людських ресурсів, включаючи введення інформації про доступність та робочий час користувачів.
-Відстеження використання матеріальних ресурсів та бюджету для кожного проекту.
-Зберігання інформації про обладнання та інші ресурси, що використовуються в проектах.
-Повідомлення та сповіщення:
-Система повідомлень для сповіщення користувачів про оновлення та нагадування щодо завдань та проектів.
-Внутрішні повідомлення між користувачами для комунікації та обговорення завдань.
-Звітність та аналітика:
-Генерація звітів щодо використання ресурсів, включаючи зведені дані про витрати, використання людських ресурсів та прогрес проектів.
-Аналіз продуктивності користувачів та команд, включаючи показники ефективності та завдань.
-Система авторизації та аутентифікації:
-Можливість авторизації та аутентифікації користувачів за допомогою ім'я користувача та пароля.
-Керування рівнями доступу для кожного користувача залежно від їхньої ролі.
-Імпорт та експорт даних:
-Можливість імпорту та експорту даних (наприклад, списку завдань чи інших ресурсів) у форматі, який зручний для обміну даними з іншими системами або сторонніми додатками.

Нефункціональні вимоги: 
- Додаток повинен бути стійким до навантаження та має гарантувати високу доступність.
- Веб-інтерфейс повинен бути адаптивним та підтримувати роботу на різних браузерах.
- Система авторизації повинна забезпечувати безпеку даних та контроль доступу до функцій на різних рівнях доступу.
- Шифрування даних повинно бути використане для захисту конфіденційної інформації.
- Додаток повинен підтримувати можливість резервного копіювання та відновлення даних.

Вимоги до бази даних: 
- Зберігання даних про користувачів, проекти, завдання та ресурси.
- Можливість швидкого пошуку та фільтрації завдань та ресурсів.

Макети інтерфейсу: 
- Головна сторінка (Dashboard).
- Сторінка проекту.
- Сторінка завдання.
- Сторінка ресурсів.
- Особистий кабінет користувача.

Технології: 
- Python, MongoDB тощо.
