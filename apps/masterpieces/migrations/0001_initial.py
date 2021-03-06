# Generated by Django 3.0.8 on 2020-08-14 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Masterpiece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('customer_rate', models.IntegerField(choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Normal'), (4, 'Good'), (5, 'Very good')], null=True, verbose_name='Customer rate')),
                ('decline_message', models.TextField(max_length=255, null=True, verbose_name='Decline message')),
                ('visible', models.BooleanField(default=True, help_text='Is masterpiece visible for other users.', verbose_name='Visible')),
            ],
            options={
                'verbose_name': 'Masterpiece',
                'verbose_name_plural': 'Masterpieces',
                'db_table': 'masterpieces',
                'ordering': ('-created_at',),
            },
        ),
    ]
