# Generated by Django 3.1.2 on 2022-08-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_remove_produto_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
