# Generated by Django 3.2 on 2021-08-23 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Strain', '0003_auto_20210518_0752'),
        ('Taxonomy', '0008_alter_species_rna_gene'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species_Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Taxonomy.species')),
                ('strain_child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Strain.strain')),
            ],
            options={
                'verbose_name_plural': 'Species_Children',
            },
        ),
    ]