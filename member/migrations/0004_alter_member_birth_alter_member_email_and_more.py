# Generated by Django 4.0.1 on 2022-01-27 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_member_birth_alter_member_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='nick',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='pw',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='tel',
            field=models.CharField(max_length=20),
        ),
    ]
