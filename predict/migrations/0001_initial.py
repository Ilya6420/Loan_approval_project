# Generated by Django 3.0.5 on 2020-04-10 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_history', models.FloatField()),
                ('applicant_income', models.FloatField()),
                ('coapplicant_income', models.FloatField()),
                ('dependents', models.FloatField()),
                ('loan_amount', models.FloatField()),
                ('loan_amount_term', models.FloatField()),
                ('classification', models.CharField(max_length=30)),
            ],
        ),
    ]