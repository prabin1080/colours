# Generated by Django 3.2.25 on 2024-07-28 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('combos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comboeffect',
            old_name='colour',
            new_name='visible_colour',
        ),
        migrations.RenameModel(
            old_name='ColourProject',
            new_name='Project',
        ),
        migrations.CreateModel(
            name='Paint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='combos.project')),
            ],
        ),
        migrations.AddField(
            model_name='comboeffect',
            name='paint_colour',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='combo_effect', to='combos.paint'),
            preserve_default=False,
        ),
    ]
