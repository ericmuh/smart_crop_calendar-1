# Generated by Django 3.2.8 on 2021-11-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyPrecipitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=20)),
                ('jan', models.FloatField()),
                ('feb', models.FloatField()),
                ('mar', models.FloatField()),
                ('apr', models.FloatField()),
                ('may', models.FloatField()),
                ('jun', models.FloatField()),
                ('jul', models.FloatField()),
                ('aug', models.FloatField()),
                ('sept', models.FloatField()),
                ('oct', models.FloatField()),
                ('nov', models.FloatField()),
                ('dec', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SeasonalPrecipitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=20)),
                ('dec_jan_feb', models.FloatField()),
                ('mar_apr_may', models.FloatField()),
                ('jun_jul_aug', models.FloatField()),
                ('sep_oct_nov', models.FloatField()),
            ],
        ),
    ]
