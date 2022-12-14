# Generated by Django 4.1.4 on 2022-12-19 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("dms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chattingroom",
            name="users",
            field=models.ManyToManyField(
                related_name="chattingrooms", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="chattingrooms",
                to="dms.chattingroom",
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="massages",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
