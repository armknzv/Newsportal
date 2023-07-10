# SF_News_Portal
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Русский (Russian)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

--------- DZ-1 (Итоговое задание 2.9 (HW-03)) ---------------------------------------------------------------------------------------------------------------

1 Модель Author
Модель, содержащая объекты всех авторов.
Имеет следующие поля:
 cвязь «один к одному» с встроенной моделью пользователей User;
 рейтинг пользователя. Ниже будет дано описание того, как этот рейтинг можно посчитать.

2 Модель Category
Категории новостей/статей — темы, которые они отражают (спорт, политика, образование и т. д.). Имеет единственное поле: название категории. Поле должно быть уникальным (в определении поля необходимо написать параметр unique = True).

3 Модель Post
Эта модель должна содержать в себе статьи и новости, которые создают пользователи. Каждый объект может иметь одну или несколько категорий.
Соответственно, модель должна включать следующие поля:
 связь «один ко многим» с моделью Author;
 поле с выбором — «статья» или «новость»;
 автоматически добавляемая дата и время создания;
 связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
 заголовок статьи/новости;
 текст статьи/новости;
 рейтинг статьи/новости.

4 Модель PostCategory
Промежуточная модель для связи «многие ко многим»:
 связь «один ко многим» с моделью Post;
 связь «один ко многим» с моделью Category.

5 Модель Comment
Под каждой новостью/статьёй можно оставлять комментарии, поэтому необходимо организовать их способ хранения тоже.
Модель будет иметь следующие поля:
 связь «один ко многим» с моделью Post;
 связь «один ко многим» со встроенной моделью User (комментарии может оставить любой пользователь, необязательно автор);
 текст комментария;
 дата и время создания комментария;
 рейтинг комментария.

Модели реализуют методы:

1 Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают рейтинг на единицу.

2 Метод preview() модели Post, который возвращает начало статьи (предварительный просмотр) длиной 124 символа и добавляет многоточие в конце.

3 Метод update_rating() модели Author, который обновляет рейтинг текущего автора (метод принимает в качестве аргумента только self).
Он состоит из следующего:
 суммарный рейтинг каждой статьи автора умножается на 3;
 суммарный рейтинг всех комментариев автора;
 суммарный рейтинг всех комментариев к статьям автора.

--------- DZ-2 (Итоговое задание 3.6 (HW-03)) --------------------------------------------------------------------------------------------------------------

В ходе работы с модулем вы должны были выполнить следующие задания:

1 Создать новую страницу с адресом /news/, на которой должен выводиться список всех новостей.

2 Вывести все статьи в виде заголовка, даты публикации и первых 20 символов текста.
Новости должны выводиться в порядке от более свежей к самой старой.

3 Сделать отдельную страницу для полной информации о статье /news/<id новости>.
На этой странице должна быть вся информация о статье. Название, текст и дата загрузки в формате день.месяц.год.

4 Написать собственный фильтр censor, который заменяет буквы нежелательных слов в заголовках и текстах статей на символ «*».

5 Все новые страницы должны использовать шаблон default.html как основу.

Дополнительно попробуйте сделать проверку, чтобы фильтр цензурирования применялся только к переменным строкового типа. Иными словами, если фильтр применяется не к строке, разработчик получает ошибку.

--------- DZ-3 (Итоговое задание 4.7 (HW-03)) --------------------------------------------------------------------------------------------------------------

Фильтры и пагинация

1 Добавьте постраничный вывод на /news/, чтобы на одной странице было не больше 10 новостей и видны номера лишь ближайших страниц, а также возможность 
перехода к первой или последней странице.

2 Добавьте страницу /news/search. На ней должна быть реализована возможность искать новости по определённым критериям. Критерии должны быть следующие:
	по названию;
	по категории;
	позже указываемой даты.

3 Убедитесь, что можно выполнить фильтрацию сразу по нескольким критериям.
Для вывода поля фильтрации по датам вам может понадобиться указать специальный тип в HTML.

Сложность в том, что форма за нас генерируется с помощью django-filter. Нам нужно сообщить ей о том, что мы хотим видеть на сайте календарь для выбора даты 
и времени. Браузер сможет отобразить автоматически сам интерфейс календаря (от нас не требуется его верстать). Для решения задачи правильного вывода формы 
нам поможет более сложная настройка класса с описанием фильтров.

Вам необходимо изучить информацию по следующим ссылкам и постараться реализовать выбор даты:

Посмотрите, как указан фильтр name.
Вам потребуется дополнительно указать правильный тип поля формы в атрибуте widget.

Создание, редактирование и удаление объектов

Запрограммируйте страницы создания, редактирования и удаления новостей и статей. Предлагаем вам расположить страницы по следующим ссылкам:
	/news/create/
	/news/<int:pk>/edit/
	/news/<int:pk>/delete/
	/articles/create/
	/articles/<int:pk>/edit/
	/articles/<int:pk>/delete/
Если вы немного запутались, ввиду того, что модель у нас одна, а страницы под создание статей и новостей должны быть отдельно, то прочитайте подсказку.

При этом не бойтесь сначала поискать информацию в интернете и пробовать разные подходы к решению задачи!

--------- DZ-4 (Итоговый проект 5.8.1 (HW-03)) --------------------------------------------------------------------------------------------------------------

Задание
1 Добавьте форму регистрации на сайте с возможностью зарегистрироваться с помощью почты и пароля или через Yandex-аккаунт. Для этого используйте пакет 
django-allauth. После того как пользователь войдёт, его должно перенаправить на страницу с новостями.

2 Настройте проверки у представлений создания и редактирования новостей и статей. Создайте группу authors, выдайте ей права на создание и изменение новых 
записей в разделах «Статьи» и «Новости».

3 Проверьте работу прав.

-------------------------------------------------------------------------------------------------------------------------------------------------------------
English (Английский)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

--------- DZ-1 (Final Task 2.9 (HW-03)) ---------------------------------------------------------------------------------------------------------------------

1 Author Model
A model containing objects of all authors.
It has the following fields:
one-to-one relationship with the built-in user model;
user rating. Below is a description of how this rating can be calculated.

2 Model Category
Categories of news/articles — the topics they reflect (sports, politics, education, etc.). Has a single field: the name of the category. The field must be 
unique (the unique = True parameter must be written in the field definition).

3 Post Model
This model should contain articles and news that users create. Each object can have one or more categories.
Accordingly, the model should include the following fields:
one-to-many relationship with the Author model;
a field with a choice — "article" or "news";
automatically added creation date and time;
the many-to-many relationship with the Category model (with an additional PostCategory model);
article title/news;
the text of the article/news;
rating of the article/news.

4 PostCategory model
Intermediate model for a many-to-many
relationship: a one-to-many relationship with the Post model;
one-to-many relationship with the Category model.

5 Comment Model
You can leave comments under each news/article, so you need to organize their storage method too.
The model will have the following fields:
one-to-many relationship with the Post model;
one-to-many relationship with the built-in User model (any user can leave comments, not necessarily the author);
comment text;
date and time the comment was created;
comment rating.

Models implement methods:

1 Like() and dislike() methods in the Comment and Post models, which increase/decrease the rating by one.

2 The preview() method of the Post model, which returns the beginning of the article (preview) with a length of 124 characters and adds an ellipsis at the 
end.

3 The update_rating() method of the Author model, which updates the rating of the current author (the method takes only self as an argument).
It consists of the following:
the total rating of each author's article is multiplied by 3;
the total rating of all the author's comments;
the total rating of all comments to the author's articles.

--------- DZ-2 (Final task 3.6 (HW-03)) ---------------------------------------------------------------------------------------------------------------------

While working with the module, you had to complete the following tasks:

1 Create a new page with the address /news/, which should display a list of all the news.

2 Display all articles in the form of a title, publication date and the first 20 characters of the text.
The news should be displayed in order from the most recent to the oldest.

3 Make a separate page for full information about the article /news/<news id>.
This page should contain all the information about the article. Title, text, and upload date in day format.month. year.

4 Write your own censor filter, which replaces the letters of unwanted words in the titles and texts of articles with the "*" symbol.

5 All new pages must use the template default.html as a basis.

Additionally, try to make sure that the censoring filter is applied only to string-type variables. In other words, if the filter is not applied to a row, the developer gets an error.

--------- DZ-3 (Final task 4.7 (HW-03)) ---------------------------------------------------------------------------------------------------------------------

Filters and pagination

1 Add a page-by-page output to /news/ so that there are no more than 10 news on one page and only the numbers of the nearest pages are visible, as well as 
the ability to go to the first or last page.

2 Add the /news/search page. It should be able to search for news by certain criteria. The criteria should be as follows:
by name;
by category;
later than the specified date.

3 Make sure that you can filter by several criteria at once.
To display the date filtering field, you may need to specify a special type in HTML.

The difficulty is that the form is generated for us using django-filter. We need to inform her that we want to see a calendar on the site for choosing the 
date and time. The browser will be able to display the calendar interface itself automatically (we do not need to make it up). To solve the problem of the 
correct output of the form, a more complex configuration of the class with a description of filters will help us.

You need to study the information on the following links and try to implement the date selection:

See how the name filter is specified.
You will need to additionally specify the correct type of form field in the widget attribute.

Creating, editing, and deleting objects

Program pages for creating, editing, and deleting news and articles. We suggest you to place the pages on the following links:
    /news/create/
    /news/<int:pk>/edit/
    /news/<int:pk>/delete/
    /articles/create/
    /articles/<int:pk>/edit/
    /articles/<int:pk>/delete/
If you are a little confused, due to the fact that we have one model, and the pages for creating articles and news should be separate, then read the hint.

At the same time, do not be afraid to first search for information on the Internet and try different approaches to solving the problem!

--------- DZ-4 (Final draft 5.8.1 (HW-03)) ------------------------------------------------------------------------------------------------------------------

Task
1 Add a registration form on the website with the ability to register using email and password or through a Yandex account. To do this, use the 
django-allauth package. After the user logs in, he should be redirected to the news page.

2 Set up checks for the views of creating and editing news and articles. Create the authors group, grant it the rights to create and edit new entries in the "Articles" and "News" sections.

3 Check the operation of the rights.
