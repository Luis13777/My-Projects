# Generated by Django 4.1.3 on 2023-08-31 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_INOA", "0008_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="email",
            name="id_email",
            field=models.IntegerField(default=1),
        ),
    ]