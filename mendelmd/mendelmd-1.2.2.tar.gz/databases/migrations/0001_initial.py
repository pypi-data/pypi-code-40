# Generated by Django 2.1.4 on 2018-12-27 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dbnfsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chr', models.TextField(blank=True, null=True)),
                ('pos_1_based', models.TextField(blank=True, null=True)),
                ('ref', models.TextField(blank=True, null=True)),
                ('alt', models.TextField(blank=True, null=True)),
                ('aaref', models.TextField(blank=True, null=True)),
                ('aaalt', models.TextField(blank=True, null=True)),
                ('rs_dbSNP150', models.TextField(blank=True, null=True)),
                ('hg19_chr', models.TextField(blank=True, null=True)),
                ('hg19_pos_1_based', models.TextField(blank=True, null=True)),
                ('hg18_chr', models.TextField(blank=True, null=True)),
                ('hg18_pos_1_based', models.TextField(blank=True, null=True)),
                ('genename', models.TextField(blank=True, null=True)),
                ('cds_strand', models.TextField(blank=True, null=True)),
                ('refcodon', models.TextField(blank=True, null=True)),
                ('codonpos', models.TextField(blank=True, null=True)),
                ('codon_degeneracy', models.TextField(blank=True, null=True)),
                ('Ancestral_allele', models.TextField(blank=True, null=True)),
                ('AltaiNeandertal', models.TextField(blank=True, null=True)),
                ('Denisova', models.TextField(blank=True, null=True)),
                ('Ensembl_geneid', models.TextField(blank=True, null=True)),
                ('Ensembl_transcriptid', models.TextField(blank=True, null=True)),
                ('Ensembl_proteinid', models.TextField(blank=True, null=True)),
                ('aapos', models.TextField(blank=True, null=True)),
                ('SIFT_score', models.TextField(blank=True, null=True)),
                ('SIFT_converted_rankscore', models.TextField(blank=True, null=True)),
                ('SIFT_pred', models.TextField(blank=True, null=True)),
                ('Uniprot_acc_Polyphen2', models.TextField(blank=True, null=True)),
                ('Uniprot_id_Polyphen2', models.TextField(blank=True, null=True)),
                ('Uniprot_aapos_Polyphen2', models.TextField(blank=True, null=True)),
                ('Polyphen2_HDIV_score', models.TextField(blank=True, null=True)),
                ('Polyphen2_HDIV_rankscore', models.TextField(blank=True, null=True)),
                ('Polyphen2_HDIV_pred', models.TextField(blank=True, null=True)),
                ('Polyphen2_HVAR_score', models.TextField(blank=True, null=True)),
                ('Polyphen2_HVAR_rankscore', models.TextField(blank=True, null=True)),
                ('Polyphen2_HVAR_pred', models.TextField(blank=True, null=True)),
                ('LRT_score', models.TextField(blank=True, null=True)),
                ('LRT_converted_rankscore', models.TextField(blank=True, null=True)),
                ('LRT_pred', models.TextField(blank=True, null=True)),
                ('LRT_Omega', models.TextField(blank=True, null=True)),
                ('MutationTaster_score', models.TextField(blank=True, null=True)),
                ('MutationTaster_converted_rankscore', models.TextField(blank=True, null=True)),
                ('MutationTaster_pred', models.TextField(blank=True, null=True)),
                ('MutationTaster_model', models.TextField(blank=True, null=True)),
                ('MutationTaster_AAE', models.TextField(blank=True, null=True)),
                ('MutationAssessor_UniprotID', models.TextField(blank=True, null=True)),
                ('MutationAssessor_variant', models.TextField(blank=True, null=True)),
                ('MutationAssessor_score', models.TextField(blank=True, null=True)),
                ('MutationAssessor_score_rankscore', models.TextField(blank=True, null=True)),
                ('MutationAssessor_pred', models.TextField(blank=True, null=True)),
                ('FATHMM_score', models.TextField(blank=True, null=True)),
                ('FATHMM_converted_rankscore', models.TextField(blank=True, null=True)),
                ('FATHMM_pred', models.TextField(blank=True, null=True)),
                ('PROVEAN_score', models.TextField(blank=True, null=True)),
                ('PROVEAN_converted_rankscore', models.TextField(blank=True, null=True)),
                ('PROVEAN_pred', models.TextField(blank=True, null=True)),
                ('Transcript_id_VEST3', models.TextField(blank=True, null=True)),
                ('Transcript_var_VEST3', models.TextField(blank=True, null=True)),
                ('VEST3_score', models.TextField(blank=True, null=True)),
                ('VEST3_rankscore', models.TextField(blank=True, null=True)),
                ('MetaSVM_score', models.TextField(blank=True, null=True)),
                ('MetaSVM_rankscore', models.TextField(blank=True, null=True)),
                ('MetaSVM_pred', models.TextField(blank=True, null=True)),
                ('MetaLR_score', models.TextField(blank=True, null=True)),
                ('MetaLR_rankscore', models.TextField(blank=True, null=True)),
                ('MetaLR_pred', models.TextField(blank=True, null=True)),
                ('Reliability_index', models.TextField(blank=True, null=True)),
                ('M_CAP_score', models.TextField(blank=True, null=True)),
                ('M_CAP_rankscore', models.TextField(blank=True, null=True)),
                ('M_CAP_pred', models.TextField(blank=True, null=True)),
                ('REVEL_score', models.TextField(blank=True, null=True)),
                ('REVEL_rankscore', models.TextField(blank=True, null=True)),
                ('MutPred_score', models.TextField(blank=True, null=True)),
                ('MutPred_rankscore', models.TextField(blank=True, null=True)),
                ('MutPred_protID', models.TextField(blank=True, null=True)),
                ('MutPred_AAchange', models.TextField(blank=True, null=True)),
                ('MutPred_Top5features', models.TextField(blank=True, null=True)),
                ('CADD_raw', models.TextField(blank=True, null=True)),
                ('CADD_raw_rankscore', models.TextField(blank=True, null=True)),
                ('CADD_phred', models.TextField(blank=True, null=True)),
                ('DANN_score', models.TextField(blank=True, null=True)),
                ('DANN_rankscore', models.TextField(blank=True, null=True)),
                ('fathmm_MKL_coding_score', models.TextField(blank=True, null=True)),
                ('fathmm_MKL_coding_rankscore', models.TextField(blank=True, null=True)),
                ('fathmm_MKL_coding_pred', models.TextField(blank=True, null=True)),
                ('fathmm_MKL_coding_group', models.TextField(blank=True, null=True)),
                ('Eigen_coding_or_noncoding', models.TextField(blank=True, null=True)),
                ('Eigen_raw', models.TextField(blank=True, null=True)),
                ('Eigen_phred', models.TextField(blank=True, null=True)),
                ('Eigen_PC_raw', models.TextField(blank=True, null=True)),
                ('Eigen_PC_phred', models.TextField(blank=True, null=True)),
                ('Eigen_PC_raw_rankscore', models.TextField(blank=True, null=True)),
                ('GenoCanyon_score', models.TextField(blank=True, null=True)),
                ('GenoCanyon_score_rankscore', models.TextField(blank=True, null=True)),
                ('integrated_fitCons_score', models.TextField(blank=True, null=True)),
                ('integrated_fitCons_score_rankscore', models.TextField(blank=True, null=True)),
                ('integrated_confidence_value', models.TextField(blank=True, null=True)),
                ('GM12878_fitCons_score', models.TextField(blank=True, null=True)),
                ('GM12878_fitCons_score_rankscore', models.TextField(blank=True, null=True)),
                ('GM12878_confidence_value', models.TextField(blank=True, null=True)),
                ('H1_hESC_fitCons_score', models.TextField(blank=True, null=True)),
                ('H1_hESC_fitCons_score_rankscore', models.TextField(blank=True, null=True)),
                ('H1_hESC_confidence_value', models.TextField(blank=True, null=True)),
                ('HUVEC_fitCons_score', models.TextField(blank=True, null=True)),
                ('HUVEC_fitCons_score_rankscore', models.TextField(blank=True, null=True)),
                ('HUVEC_confidence_value', models.TextField(blank=True, null=True)),
                ('GERP_NR', models.TextField(blank=True, null=True)),
                ('GERP_RS', models.TextField(blank=True, null=True)),
                ('GERP_RS_rankscore', models.TextField(blank=True, null=True)),
                ('phyloP100way_vertebrate', models.TextField(blank=True, null=True)),
                ('phyloP100way_vertebrate_rankscore', models.TextField(blank=True, null=True)),
                ('phyloP20way_mammalian', models.TextField(blank=True, null=True)),
                ('phyloP20way_mammalian_rankscore', models.TextField(blank=True, null=True)),
                ('phastCons100way_vertebrate', models.TextField(blank=True, null=True)),
                ('phastCons100way_vertebrate_rankscore', models.TextField(blank=True, null=True)),
                ('phastCons20way_mammalian', models.TextField(blank=True, null=True)),
                ('phastCons20way_mammalian_rankscore', models.TextField(blank=True, null=True)),
                ('SiPhy_29way_pi', models.TextField(blank=True, null=True)),
                ('SiPhy_29way_logOdds', models.TextField(blank=True, null=True)),
                ('SiPhy_29way_logOdds_rankscore', models.TextField(blank=True, null=True)),
                ('Gp3_AC_1k', models.TextField(blank=True, null=True)),
                ('Gp3_AF_1k', models.TextField(blank=True, null=True)),
                ('Gp3_AFR_AC_1k', models.TextField(blank=True, null=True)),
                ('Gp3_AFR_AF_1k', models.TextField(blank=True, null=True)),
                ('Gp3_EUR_AC_1k', models.TextField(blank=True, null=True)),
                ('Gp3_EUR_AF_1k', models.TextField(blank=True, null=True)),
                ('Gp3_AMR_AC_1k', models.TextField(blank=True, null=True)),
                ('Gp3_AMR_AF_1k', models.TextField(blank=True, null=True)),
                ('Gp3_EAS_AC_1k', models.TextField(blank=True, null=True)),
                ('Gp3_EAS_AF_1k', models.TextField(blank=True, null=True)),
                ('Gp3_SAS_AC_1k', models.TextField(blank=True, null=True)),
                ('Gp3_SAS_AF_1k', models.TextField(blank=True, null=True)),
                ('TWINSUK_AC', models.TextField(blank=True, null=True)),
                ('TWINSUK_AF', models.TextField(blank=True, null=True)),
                ('ALSPAC_AC', models.TextField(blank=True, null=True)),
                ('ALSPAC_AF', models.TextField(blank=True, null=True)),
                ('ESP6500_AA_AC', models.TextField(blank=True, null=True)),
                ('ESP6500_AA_AF', models.TextField(blank=True, null=True)),
                ('ESP6500_EA_AC', models.TextField(blank=True, null=True)),
                ('ESP6500_EA_AF', models.TextField(blank=True, null=True)),
                ('ExAC_AC', models.TextField(blank=True, null=True)),
                ('ExAC_AF', models.TextField(blank=True, null=True)),
                ('ExAC_Adj_AC', models.TextField(blank=True, null=True)),
                ('ExAC_Adj_AF', models.TextField(blank=True, null=True)),
                ('ExAC_AFR_AC', models.TextField(blank=True, null=True)),
                ('ExAC_AFR_AF', models.TextField(blank=True, null=True)),
                ('ExAC_AMR_AC', models.TextField(blank=True, null=True)),
                ('ExAC_AMR_AF', models.TextField(blank=True, null=True)),
                ('ExAC_EAS_AC', models.TextField(blank=True, null=True)),
                ('ExAC_EAS_AF', models.TextField(blank=True, null=True)),
                ('ExAC_FIN_AC', models.TextField(blank=True, null=True)),
                ('ExAC_FIN_AF', models.TextField(blank=True, null=True)),
                ('ExAC_NFE_AC', models.TextField(blank=True, null=True)),
                ('ExAC_NFE_AF', models.TextField(blank=True, null=True)),
                ('ExAC_SAS_AC', models.TextField(blank=True, null=True)),
                ('ExAC_SAS_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_Adj_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_Adj_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_AFR_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_AFR_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_AMR_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_AMR_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_EAS_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_EAS_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_FIN_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_FIN_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_NFE_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_NFE_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_SAS_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonTCGA_SAS_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_Adj_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_Adj_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_AFR_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_AFR_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_AMR_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_AMR_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_EAS_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_EAS_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_FIN_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_FIN_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_NFE_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_NFE_AF', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_SAS_AC', models.TextField(blank=True, null=True)),
                ('ExAC_nonpsych_SAS_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_AFR_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_AFR_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_AFR_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_AMR_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_AMR_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_AMR_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_ASJ_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_ASJ_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_ASJ_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_EAS_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_EAS_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_EAS_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_FIN_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_FIN_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_FIN_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_NFE_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_NFE_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_NFE_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_SAS_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_SAS_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_SAS_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_OTH_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_OTH_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_exomes_OTH_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_AFR_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_AFR_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_AFR_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_AMR_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_AMR_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_AMR_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_ASJ_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_ASJ_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_ASJ_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_EAS_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_EAS_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_EAS_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_FIN_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_FIN_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_FIN_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_NFE_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_NFE_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_NFE_AF', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_OTH_AC', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_OTH_AN', models.TextField(blank=True, null=True)),
                ('gnomAD_genomes_OTH_AF', models.TextField(blank=True, null=True)),
                ('clinvar_rs', models.TextField(blank=True, null=True)),
                ('clinvar_clnsig', models.TextField(blank=True, null=True)),
                ('clinvar_trait', models.TextField(blank=True, null=True)),
                ('clinvar_golden_stars', models.TextField(blank=True, null=True)),
                ('Interpro_domain', models.TextField(blank=True, null=True)),
                ('GTEx_V6p_gene', models.TextField(blank=True, null=True)),
                ('GTEx_V6p_tissue', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genome1kGenotype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genotype', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genome1kSample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genome1kSampleVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genotype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.Genome1kGenotype')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.Genome1kSample')),
            ],
        ),
        migrations.CreateModel(
            name='Genome1kVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos_index', models.TextField(db_index=True)),
                ('chrom', models.TextField(blank=True, db_index=True, null=True)),
                ('pos', models.TextField(blank=True, db_index=True, null=True)),
                ('rsid', models.TextField(blank=True, null=True)),
                ('ref', models.TextField(blank=True, db_index=True, null=True)),
                ('alt', models.TextField(blank=True, db_index=True, null=True)),
                ('qual', models.TextField(blank=True, null=True)),
                ('filter', models.TextField(blank=True, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('format', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genome1kVariantIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.TextField()),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.Genome1kVariant')),
            ],
        ),
        migrations.CreateModel(
            name='HGMD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.TextField(db_index=True)),
                ('chrom', models.TextField(blank=True, db_index=True, null=True)),
                ('pos', models.TextField(blank=True, db_index=True, null=True)),
                ('rsid', models.TextField(blank=True, null=True)),
                ('ref', models.TextField(blank=True, db_index=True, null=True)),
                ('alt', models.TextField(blank=True, db_index=True, null=True)),
                ('qual', models.TextField(blank=True, null=True)),
                ('filter', models.TextField(blank=True, null=True)),
                ('mutclass', models.TextField(blank=True, null=True)),
                ('mut', models.TextField(blank=True, null=True)),
                ('gene', models.TextField(blank=True, null=True)),
                ('strand', models.TextField(blank=True, null=True)),
                ('dna', models.TextField(blank=True, null=True)),
                ('prot', models.TextField(blank=True, null=True)),
                ('db', models.TextField(blank=True, null=True)),
                ('phen', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VariSNP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbsnp_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='genome1ksamplevariant',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.Genome1kVariant'),
        ),
    ]
