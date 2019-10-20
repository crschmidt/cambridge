# Generated by Django 2.2.3 on 2019-10-20 22:33

from django.db import migrations, models


def set_endorsements_false(app, schema_editor):
    """update existing endorsements to be false"""
    Endorsement = app.get_model('overview.Endorsement')
    Endorsement.objects.update(display=False)


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0043_auto_20191020_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='endorsement',
            name='display',
            field=models.BooleanField(default=True),
        ),

        migrations.RunPython(set_endorsements_false, lambda *args, **kwargs: None)
    ]
