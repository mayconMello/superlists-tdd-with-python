# Generated by Django 3.1.4 on 2021-01-20 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_token_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='uid',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
