Тестовое задание – дополнительный способ для нас убедиться в вашей квалификации и понять, какого рода задачи вы выполняете эффективнее всего. Расчётное время на выполнение тестового задания: 3-4 часа, время засекается нестрого. Приступить к выполнению тестового задания можно в любое удобное для вас время.

У текущего тестового задания есть только общее описание требований, конкретные детали реализации остаются на усмотрение разработчика.

### Задача: спроектировать и разработать API для системы опросов пользователей. 

 #### Функционал для администратора системы:

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов
  Атрибуты опроса: 
  1) название
  2) дата старта (после создания, поле "дата старта" у опроса менять нельзя)
  3) дата окончания
  4) описание
    

- добавление/изменение/удаление вопросов в опросе. 
  Атрибуты вопросов: 
    1) текст вопроса
    2) тип вопроса:
        1) ответ текстом
        2) ответ с выбором одного варианта
        3) ответ с выбором нескольких вариантов
    
#### Функционал для пользователей системы:

- получение списка активных опросов

- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся 
 числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

Использовать следующие технологии: 
- Django 2.2.10
- Django REST framework.

### Результат выполнения задачи:

#### - исходный код приложения в github (только на github, публичный репозиторий)
#### - инструкция по разворачиванию приложения (в docker или локально)
#### - документация по API