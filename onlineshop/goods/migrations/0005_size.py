# Generated by Django 4.2.11 on 2024-04-20 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_additionalimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Размер|количетсво',
                'verbose_name_plural': 'Размеры|количество',
            },
        ),
    ]