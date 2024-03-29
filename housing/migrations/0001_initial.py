# Generated by Django 5.0 on 2024-01-25 11:47

import django.db.models.deletion
import lib.custom_id
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=lib.custom_id.custom_id,
                        editable=False,
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("state", models.CharField(max_length=20, verbose_name="state")),
                ("city", models.CharField(max_length=20, verbose_name="city")),
                ("town", models.CharField(max_length=20, verbose_name="town")),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=lib.custom_id.custom_id,
                        editable=False,
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=20, verbose_name="category")),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Features",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=lib.custom_id.custom_id,
                        editable=False,
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "bedrooms",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="number of bedrooms"
                    ),
                ),
                (
                    "bathrooms",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="number of bathrooms"
                    ),
                ),
                (
                    "packing_space",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="number of packing space"
                    ),
                ),
                ("balcony", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="HouseType",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=lib.custom_id.custom_id,
                        editable=False,
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("type", models.CharField(max_length=20, verbose_name="type of house")),
            ],
        ),
        migrations.CreateModel(
            name="House",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=lib.custom_id.custom_id,
                        editable=False,
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=50, verbose_name="title of the house"),
                ),
                (
                    "banner",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="listings",
                        verbose_name="main image",
                    ),
                ),
                (
                    "description",
                    models.TextField(verbose_name="description of the house"),
                ),
                ("price", models.FloatField()),
                ("is_available", models.BooleanField(default=True)),
                ("is_sold", models.BooleanField(default=False)),
                ("is_negotiable", models.BooleanField(default=False)),
                ("slug", models.SlugField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="house_address",
                        to="housing.address",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category",
                        to="housing.category",
                    ),
                ),
                (
                    "features",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="house_features",
                        to="housing.features",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="house_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="housing.housetype",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Houses",
            },
        ),
        migrations.CreateModel(
            name="Images",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=lib.custom_id.custom_id,
                        editable=False,
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to="listings", verbose_name="image"),
                ),
                (
                    "house",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="house_images",
                        to="housing.house",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "House Images",
            },
        ),
    ]
