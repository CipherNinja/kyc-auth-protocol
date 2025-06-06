# Generated by Django 5.2 on 2025-04-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_organizationcustomer_shared_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'verbose_name': 'Business Organization', 'verbose_name_plural': 'Business Organizations'},
        ),
        migrations.AlterModelOptions(
            name='organizationcustomer',
            options={'verbose_name': 'Customer of Organization', 'verbose_name_plural': 'Customers of Organization'},
        ),
        migrations.AddField(
            model_name='organization',
            name='official_domain',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
