# Generated by Django 3.0.8 on 2020-08-27 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('checkout', '0002_auto_20200827_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_profiles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.UserProfiles'),
        ),
    ]