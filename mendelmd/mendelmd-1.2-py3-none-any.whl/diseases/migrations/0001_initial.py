# Generated by Django 2.1.4 on 2018-12-27 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('omim_id', models.CharField(max_length=255)),
                ('chr_location', models.CharField(max_length=255)),
                ('gene_names', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_name', models.CharField(max_length=255)),
                ('chromossome', models.CharField(blank=True, max_length=255, null=True)),
                ('names', models.TextField(blank=True, null=True)),
                ('strand', models.CharField(blank=True, max_length=255, null=True)),
                ('chr_location', models.CharField(blank=True, max_length=255, null=True)),
                ('transcription_start', models.IntegerField(blank=True, null=True)),
                ('transcription_end', models.IntegerField(blank=True, null=True)),
                ('cds_start', models.IntegerField(blank=True, null=True)),
                ('cds_end', models.IntegerField(blank=True, null=True)),
                ('exons_count', models.CharField(blank=True, max_length=500, null=True)),
                ('exons_start', models.TextField(blank=True, null=True)),
                ('exons_end', models.TextField(blank=True, null=True)),
                ('diseases', models.ManyToManyField(to='diseases.Disease')),
            ],
        ),
        migrations.CreateModel(
            name='HGMDGene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=255)),
                ('aliases', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_aliases', models.TextField(blank=True, null=True)),
                ('location', models.CharField(max_length=255)),
                ('n_mutations', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HGMDMutation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mutation_type', models.CharField(blank=True, max_length=255, null=True)),
                ('acession', models.CharField(blank=True, max_length=255, null=True)),
                ('reference', models.TextField(blank=True, null=True)),
                ('extras', models.TextField(blank=True, null=True)),
                ('rsid', models.CharField(blank=True, max_length=255, null=True)),
                ('dm_mutation', models.BooleanField(default=False)),
                ('coordinate', models.CharField(blank=True, max_length=100, null=True)),
                ('chromossome', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('codon_change', models.CharField(blank=True, max_length=255, null=True)),
                ('aa_change', models.CharField(blank=True, max_length=255, null=True)),
                ('hgvs_nucleotide', models.CharField(blank=True, max_length=100, null=True)),
                ('hgvs_protein', models.CharField(blank=True, max_length=100, null=True)),
                ('splicing_mutation', models.CharField(blank=True, max_length=255, null=True)),
                ('regulatory_sequence', models.TextField(blank=True, null=True)),
                ('deletion_sequence', models.TextField(blank=True, null=True)),
                ('insertion_sequence', models.TextField(blank=True, null=True)),
                ('dna_level', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('insertion_duplication', models.CharField(blank=True, max_length=255, null=True)),
                ('amplified_sequence', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('normal_range', models.CharField(blank=True, max_length=255, null=True)),
                ('pathological_range', models.CharField(blank=True, max_length=255, null=True)),
                ('gene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diseases.HGMDGene')),
            ],
        ),
        migrations.CreateModel(
            name='HGMDPhenotype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='hgmdmutation',
            name='phenotype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diseases.HGMDPhenotype'),
        ),
        migrations.AddField(
            model_name='hgmdgene',
            name='diseases',
            field=models.ManyToManyField(to='diseases.HGMDPhenotype'),
        ),
    ]
