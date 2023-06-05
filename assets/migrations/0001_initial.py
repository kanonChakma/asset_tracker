# Generated by Django 4.2.1 on 2023-06-05 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("location", models.CharField(max_length=150)),
                ("about", models.TextField(blank=True, null=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Device",
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
                ("identifier", models.CharField(max_length=100, unique=True)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("join_date", models.DateField()),
                ("address", models.TextField()),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="assets.company"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeviceCheck",
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
                (
                    "log_type",
                    models.CharField(
                        choices=[
                            ("CO", "Check Out"),
                            ("RT", "Returned"),
                            ("NC", "Not Checked Out"),
                        ],
                        default="NC",
                        max_length=2,
                    ),
                ),
                ("checked_out_date", models.DateTimeField()),
                ("returned_date", models.DateTimeField(blank=True, null=True)),
                (
                    "condition_out",
                    models.CharField(
                        choices=[("Good", "Good"), ("Fair", "Fair"), ("Poor", "Poor")],
                        max_length=10,
                    ),
                ),
                (
                    "condition_in",
                    models.CharField(
                        choices=[("Good", "Good"), ("Fair", "Fair"), ("Poor", "Poor")],
                        max_length=10,
                    ),
                ),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="device_checks",
                        to="assets.device",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeviceAllocation",
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
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="device_allocation",
                        to="assets.device",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="device_allocation",
                        to="assets.employee",
                    ),
                ),
            ],
        ),
    ]
