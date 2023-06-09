# Generated by Django 4.1.5 on 2023-01-27 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
