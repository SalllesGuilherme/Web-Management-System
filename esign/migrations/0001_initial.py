# Generated by Django 4.0.4 on 2022-04-14 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='changerequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('edescription', models.CharField(max_length=100)),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'changerequest',
            },
        ),
    ]
