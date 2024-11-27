from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    pages = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    # в моей упрощенной системе у книги есть только один автор
    # (сделаем вид что это publisher, а не author)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Collection(models.Model):
    """Подборки книг"""
    title = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='collections')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
