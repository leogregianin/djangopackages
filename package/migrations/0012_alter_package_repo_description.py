# Generated by Django 4.0.3 on 2022-03-07 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("package", "0011_package_date_repo_archived"),
    ]

    operations = [
        migrations.AlterField(
            model_name="package",
            name="repo_description",
            field=models.TextField(
                blank=True, max_length=500, verbose_name="Repo Description"
            ),
        ),
    ]
