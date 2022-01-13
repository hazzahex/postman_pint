# Generated by Django 4.0.1 on 2022-01-13 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Taphouse', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bartender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bartender.institution')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customer')),
            ],
        ),
    ]