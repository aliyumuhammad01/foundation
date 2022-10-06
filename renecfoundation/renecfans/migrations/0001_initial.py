# Generated by Django 4.1 on 2022-09-24 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=60, unique=True)),
                ('lga', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Peoples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('nin', models.IntegerField(unique=True, verbose_name=11)),
                ('email', models.CharField(max_length=60, unique=True)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locality', to='renecfans.states')),
            ],
        ),
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trx_wallet', models.CharField(max_length=60, unique=True)),
                ('amount', models.IntegerField(default=0)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributor', to='renecfans.peoples', to_field='nin')),
                ('reciever_phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to='renecfans.peoples', to_field='phone_number')),
            ],
        ),
    ]
