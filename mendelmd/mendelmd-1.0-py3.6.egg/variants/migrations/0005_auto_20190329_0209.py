# Generated by Django 2.1.1 on 2019-03-29 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variants', '0004_variant_snpeff_aa_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='snpeff_biotype',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='snpeff_exon_rank',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='snpeff_gene_coding',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='snpeff_transcript_id',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
    ]
