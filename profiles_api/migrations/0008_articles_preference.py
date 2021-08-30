# Generated by Django 2.2 on 2021-08-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0007_auto_20210829_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='preference',
            field=models.CharField(choices=[('business', 'business'), ('entertainment', 'entertainment'), ('general', 'general'), ('health', 'health'), ('science', 'science'), ('sports', 'sports'), ('technology', 'technology')], default='general', max_length=13),
        ),
    ]