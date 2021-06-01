# Generated by Django 2.2.4 on 2021-03-31 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('users_added', models.ManyToManyField(related_name='film_list', to='first_app.User')),
                ('users_watched', models.ManyToManyField(related_name='watched', to='first_app.User')),
            ],
        ),
    ]