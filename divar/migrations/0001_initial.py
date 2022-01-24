# Generated by Django 3.2.7 on 2021-10-03 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertising', models.CharField(choices=[('private', 'شخصی'), ('مشاور املاک', 'مشاور املاک')], default='private', max_length=50, verbose_name='نوع آگهی')),
                ('image', models.ImageField(null=True, upload_to='image/', verbose_name='عکس آگهی')),
                ('title', models.CharField(db_index=True, max_length=250, verbose_name='تیتر')),
                ('slug', models.SlugField(max_length=250)),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='سال ساخت آپارتمان')),
                ('metrazh', models.IntegerField(verbose_name='متراژ')),
                ('tedad_room', models.IntegerField(null=True, verbose_name='تعداد اتاق ها')),
                ('price_to_metrazh', models.IntegerField(verbose_name='قیمت هر متر')),
                ('price', models.IntegerField(null=True, verbose_name='قیمت کل')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='divar.Category')),
                ('center', models.ManyToManyField(to='divar.Center', verbose_name='شهر | محل آگهی')),
            ],
        ),
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('brand', models.CharField(max_length=250)),
                ('esalat', models.CharField(choices=[('orginal', 'اصل'), ('Copies', 'کپی'), ('tarh', 'طرح')], max_length=50)),
                ('description', models.TextField()),
                ('hard', models.CharField(choices=[('a', 'گیگابایت 16'), ('b', 'گیگابایت 32'), ('c', 'گیگابایت 64'), ('d', 'گیگابایت 128'), ('e', 'گیگابایت 256'), ('f', 'گیگابایت 542')], max_length=50)),
                ('ram', models.IntegerField()),
                ('color', models.CharField(max_length=100)),
                ('price', models.IntegerField(default='توافقی')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='divar.Category')),
                ('center', models.ManyToManyField(to='divar.Center')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(db_index=True, max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField()),
                ('price', models.IntegerField(default='توافقی')),
                ('bime_time', models.CharField(choices=[('1month', 'ماه 1'), ('2month', 'ماه 2'), ('3month', 'ماه 3'), ('4month', 'ماه 4'), ('5month', 'ماه 5'), ('6month', 'ماه 6'), ('7month', 'ماه 7'), ('8month', 'ماه 8'), ('9month', 'ماه 9'), ('10month', 'ماه 10'), ('11month', 'ماه 11'), ('12month', 'ماه 12')], max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='divar.Category')),
                ('center', models.ManyToManyField(to='divar.Center')),
            ],
        ),
    ]
