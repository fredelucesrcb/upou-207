# Generated by Django 4.2.11 on 2024-05-01 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_alter_email_deleted_at_alter_order_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]