# Generated by Django 4.0.5 on 2022-07-01 19:08

from django.db import migrations, models

import radiogrid.db


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Octodex",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                (
                    "categories",
                    radiogrid.db.RadioGridField(
                        require_all_fields=True,
                        rows=((1, "First"), (2, "Second"), (3, "Third")),
                        values=(
                            ("pyha", "Pyha"),
                            ("work", "Work"),
                            ("happy", "Happy"),
                            ("food", "Food"),
                        ),
                    ),
                ),
                (
                    "week",
                    radiogrid.db.RadioGridField(
                        require_all_fields=True,
                        rows=(
                            (1, "Monday"),
                            (2, "Tuesday"),
                            (3, "Wednesday"),
                            (4, "Thursday"),
                            (5, "Friday"),
                            (6, "Saturday"),
                            (7, "Sunday"),
                        ),
                        values=(
                            (1, "2-3 hours"),
                            (2, "3-4 hours"),
                            (3, "5-7 hours"),
                            (4, "8 hours"),
                            (5, "Never"),
                        ),
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Octoduck",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                (
                    "week",
                    radiogrid.db.RadioGridField(
                        require_all_fields=True,
                        rows=(
                            (1, "Monday"),
                            (2, "Tuesday"),
                            (3, "Wednesday"),
                            (4, "Thursday"),
                            (5, "Friday"),
                            (6, "Saturday"),
                            (7, "Sunday"),
                        ),
                        values=(
                            (1, "2-3 hours"),
                            (2, "3-4 hours"),
                            ("3", "5-7 hours"),
                            (4, "8 hours"),
                            (5, "Never"),
                        ),
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OptionalGridModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                (
                    "week",
                    radiogrid.db.RadioGridField(
                        require_all_fields=False,
                        rows=(
                            (1, "Monday"),
                            (2, "Tuesday"),
                            (3, "Wednesday"),
                            (4, "Thursday"),
                            (5, "Friday"),
                            (6, "Saturday"),
                            (7, "Sunday"),
                        ),
                        values=(
                            (1, "2-3 hours"),
                            (2, "3-4 hours"),
                            (3, "5-7 hours"),
                            (4, "8 hours"),
                            (5, "Never"),
                        ),
                    ),
                ),
            ],
        ),
    ]
