# Generated by Django 2.1.1 on 2019-03-28 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variants', '0003_variant_snpeff_codon_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='snpeff_aa_change',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
    ]
