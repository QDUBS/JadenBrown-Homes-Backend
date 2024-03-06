# Generated by Django 5.0 on 2024-01-25 11:47

import django.db.models.deletion
import lib.custom_id
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
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
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("state", models.CharField(max_length=20, verbose_name="State")),
                ("city", models.CharField(max_length=20, verbose_name="city")),
                ("street", models.CharField(max_length=20, verbose_name="street")),
                (
                    "description",
                    models.CharField(max_length=100, verbose_name="Description"),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=lib.custom_id.custom_id,
                        editable=False,
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("phone_one", models.CharField(max_length=15)),
                ("phone_two", models.CharField(blank=True, max_length=15, null=True)),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="Business Email",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Account",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "id",
                    models.CharField(
                        default=lib.custom_id.custom_id,
                        editable=False,
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="Email Adress"
                    ),
                ),
                ("username", models.CharField(max_length=255, verbose_name="Username")),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_oauth", models.BooleanField(blank=True, default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AccountProfile",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=lib.custom_id.custom_id,
                        editable=False,
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=255, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=255, verbose_name="Last Name"),
                ),
                (
                    "nickname",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Nick Name"
                    ),
                ),
                (
                    "accout_type",
                    models.CharField(
                        choices=[("regualar", "regular"), ("agent", "agent")],
                        default="regular",
                        max_length=15,
                    ),
                ),
                (
                    "avata",
                    models.ImageField(
                        blank=True, default="", null=True, upload_to="profile"
                    ),
                ),
                ("slug", models.SlugField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="address",
                        to="account.address",
                    ),
                ),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact",
                        to="account.contact",
                    ),
                ),
            ],
        ),
    ]
