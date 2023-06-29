from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextField


# Создавайте свои модели здесь.
class Author(models.Model):
    """
    Метод update_rating() вычисляет суммарный рейтинг каждой статьи автора,
    умножает его на 3, а затем складывает с суммарным рейтингом всех комментариев автора
    и комментариев к статьям автора.
    Результат сохраняется в поле rating объекта Author
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        self.rating = sum([post.rating * 3 for post in self.posts.all()]) \
                      + sum([comment.rating for comment in self.comments.all()])
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    """
    Метод preview() возвращает начало статьи длиной 124 символа с многоточием в конце
    Методы like() и dislike() увеличивают/уменьшают рейтинг на единицу.
    """
    CHOICES = (
        ('article', 'Article'),
        ('news', 'News'),
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    type = models.CharField(max_length=10, choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    content: TextField = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        if len(self.content) > 124:
            return self.content[:124] + '...'
        return self.content


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    """
    Методы like() и dislike() увеличивают/уменьшают рейтинг на единицу.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
