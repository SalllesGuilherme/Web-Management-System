# Generated by Django 4.0.4 on 2022-04-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esign', '0002_remove_changerequest_econtact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('area', models.CharField(choices=[('Mixing', 'Mixing'), ('Hot Prep', 'Hot Prep'), ('Cold Prep', 'Cold Prep'), ('Tire Building', 'Tire Building'), ('Curing', 'Curing'), ('Final Finishing', 'Final Finishing')], max_length=100, null=True)),
                ('plant', models.CharField(choices=[('PLT', 'PLT'), ('TT', 'TT'), ('SHARED', 'SHARED')], max_length=100, null=True)),
                ('dept', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tbl_client',
            },
        ),
        migrations.RenameField(
            model_name='changerequest',
            old_name='edescription',
            new_name='request',
        ),
        migrations.RenameField(
            model_name='changerequest',
            old_name='ename',
            new_name='requestedby',
        ),
        migrations.RenameField(
            model_name='changerequest',
            old_name='estatus',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='changerequest',
            name='eemail',
        ),
        migrations.RemoveField(
            model_name='changerequest',
            name='erequestedby',
        ),
        migrations.AddField(
            model_name='changerequest',
            name='description',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
