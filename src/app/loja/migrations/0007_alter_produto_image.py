# Generated by Django 4.1 on 2022-08-22 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_alter_produto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
