# Generated by Django 4.1 on 2024-04-25 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BookCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_id", models.CharField(max_length=10)),
                ("category_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="BookCode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code_id", models.CharField(max_length=1)),
                ("code_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="BookData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100, null=True)),
                ("publisher", models.CharField(max_length=100, null=True)),
                ("publish_date", models.DateField(null=True)),
                ("summary", models.CharField(max_length=40, null=True)),
                ("price", models.IntegerField()),
                ("keeper_id", models.IntegerField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="book.bookcategory",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        max_length=24,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="book.bookcode",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookLendRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("borrow_date", models.DateField(null=True)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="book.bookdata"
                    ),
                ),
                (
                    "borrower",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
