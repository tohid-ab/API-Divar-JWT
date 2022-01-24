from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name


class TestModel(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Center(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name


class Home(models.Model):
    STATUS_CHOICES = (
        ('private', 'شخصی'),
        ('مشاور املاک', 'مشاور املاک'),
    )
    center = models.ManyToManyField(Center, verbose_name='شهر | محل آگهی')
    category = models.ManyToManyField(Category)
    advertising = models.CharField(max_length=50, default='private', choices=STATUS_CHOICES, verbose_name='نوع آگهی')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/', verbose_name='عکس آگهی', null=True)
    title = models.CharField(max_length=250, db_index=True, verbose_name='تیتر')
    slug = models.SlugField(max_length=250)
    description = models.TextField(verbose_name='توضیحات')
    date_created = models.DateTimeField(default=timezone.now, verbose_name='سال ساخت آپارتمان')
    metrazh = models.IntegerField(verbose_name='متراژ')
    tedad_room = models.IntegerField(null=True,verbose_name='تعداد اتاق ها')
    price_to_metrazh = models.IntegerField(verbose_name='قیمت هر متر')
    price = models.IntegerField(null=True,verbose_name='قیمت کل')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])

    def __str__(self):
        return self.title


class Car(models.Model):
    STAUS_CHOICE = (
        ('1month', 'ماه 1'),
        ('2month', 'ماه 2'),
        ('3month', 'ماه 3'),
        ('4month', 'ماه 4'),
        ('5month', 'ماه 5'),
        ('6month', 'ماه 6'),
        ('7month', 'ماه 7'),
        ('8month', 'ماه 8'),
        ('9month', 'ماه 9'),
        ('10month', 'ماه 10'),
        ('11month', 'ماه 11'),
        ('12month', 'ماه 12'),
    )
    center = models.ManyToManyField(Center)
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    date_created = models.DateTimeField()
    price = models.IntegerField(default='توافقی')
    bime_time = models.CharField(max_length=100, choices=STAUS_CHOICE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Electronic(models.Model):
    STAUS_CHOICE = (
        ('orginal', 'اصل'),
        ('Copies', 'کپی'),
        ('tarh', 'طرح')
    )
    STAUS_CHOICE_HARD = (
        ('a', 'گیگابایت 16'),
        ('b', 'گیگابایت 32'),
        ('c', 'گیگابایت 64'),
        ('d', 'گیگابایت 128'),
        ('e', 'گیگابایت 256'),
        ('f', 'گیگابایت 542'),
    )
    center = models.ManyToManyField(Center)
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    brand = models.CharField(max_length=250)
    esalat = models.CharField(max_length=50, choices=STAUS_CHOICE)
    description = models.TextField()
    hard = models.CharField(max_length=50, choices=STAUS_CHOICE_HARD)
    ram = models.IntegerField()
    color = models.CharField(max_length=100)
    price = models.IntegerField(default='توافقی')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
