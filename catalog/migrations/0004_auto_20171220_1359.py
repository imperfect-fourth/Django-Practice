# Generated by Django 2.0 on 2017-12-20 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20171220_1134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'), ('is_staff_member', 'Check if viewing member is staff'))},
        ),
    ]
