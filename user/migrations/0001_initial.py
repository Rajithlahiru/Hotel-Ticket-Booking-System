# Generated by Django 4.1.7 on 2023-03-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=20)),
                ("firstname", models.CharField(max_length=20)),
                ("lastname", models.CharField(max_length=20)),
                ("nic", models.CharField(max_length=20)),
                ("address", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=20)),
                ("mobile_no", models.CharField(max_length=10)),
                (
                    "email",
                    models.EmailField(max_length=60, unique=True, verbose_name="email"),
                ),
                ("nationality", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
    ]
