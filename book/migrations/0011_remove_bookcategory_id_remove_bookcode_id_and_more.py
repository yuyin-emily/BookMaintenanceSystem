# Generated by Django 4.1 on 2024-05-08 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0010_auto_20240502_1622"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bookcategory",
            name="id",
        ),
        migrations.RemoveField(
            model_name="bookcode",
            name="id",
        ),
        migrations.AlterField(
            model_name="bookcategory",
            name="category_id",
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="bookcode",
            name="code_id",
            field=models.CharField(max_length=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="bookdata",
            name="author",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="bookdata",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="bookdata",
            name="keeper_id",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bookdata",
            name="price",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bookdata",
            name="publish_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bookdata",
            name="publisher",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="bookdata",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="book.bookcode"
            ),
        ),
        migrations.AlterField(
            model_name="bookdata",
            name="summary",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="booklendrecord",
            name="borrow_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="booklendrecord",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
