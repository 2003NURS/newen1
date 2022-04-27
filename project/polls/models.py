from django.db import models
from datetime import datetime,date

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=250, verbose_name='taqyryp')
    is_published = models.BooleanField(default='True', verbose_name='shygarylym')
    pictute = models.ImageField(default= 'default value')
    email = models.EmailField(blank = True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_urls(self):
        return reverse('post', kwargs={'post_slag':self.slag})

    class Meta:
        verbose_name = 'Maqala'
        verbose_name_plural = 'maqalalar'
        ordering =['title', 'pictute']

class Categories(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank= True)
    picture = models.ImageField(default='default value')
    describe = models.TextField(default='DataFlair Django tutorials')



    def __str__(self):
        return self.title

class Registration(models.Model):
    name = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    username = models.CharField(max_length=15)
    patronymic = models.CharField(max_length=15)
    email  = models.EmailField(blank=True, unique=True)
    telnumber = models.IntegerField(max_length=11, unique=True)
    password = models.CharField(max_length=10)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрация'
        ordering = ['name', 'lastname']