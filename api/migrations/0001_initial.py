# Generated by Django 3.1.2 on 2020-12-26 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('custid', models.IntegerField()),
                ('custname', models.CharField(max_length=66)),
                ('ordervalue', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stuid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=55)),
                ('classname', models.CharField(max_length=55)),
                ('rollno', models.IntegerField()),
                ('eng', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('comp', models.IntegerField()),
                ('science', models.IntegerField()),
            ],
        ),
    ]
