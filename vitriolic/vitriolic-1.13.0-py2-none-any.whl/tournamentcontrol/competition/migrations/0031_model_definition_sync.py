# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 11:59
from __future__ import unicode_literals

import django.db.models.deletion
import touchtechnology.common.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0030_match_referees'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seasonreferee',
            options={'ordering': ('season', 'person__last_name', 'person__first_name'), 'verbose_name': 'referee'},
        ),
        migrations.AlterField(
            model_name='club',
            name='primary',
            field=touchtechnology.common.db.models.ForeignKey(blank=True, help_text='Appears on the front-end with other club information.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='competition.Person', verbose_name='Primary contact'),
        ),
        migrations.AlterField(
            model_name='club',
            name='slug_locked',
            field=touchtechnology.common.db.models.BooleanField(default=False, verbose_name='Slug locked'),
        ),
        migrations.AlterField(
            model_name='clubassociation',
            name='club',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='staff', to='competition.Club'),
        ),
        migrations.AlterField(
            model_name='clubassociation',
            name='person',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='competition.Person'),
        ),
        migrations.AlterField(
            model_name='clubrole',
            name='competition',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='club_roles', to='competition.Competition'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='enabled',
            field=touchtechnology.common.db.models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='slug_locked',
            field=touchtechnology.common.db.models.BooleanField(default=False, verbose_name='Slug locked'),
        ),
        migrations.AlterField(
            model_name='division',
            name='draft',
            field=touchtechnology.common.db.models.BooleanField(default=False, help_text='Marking a division as draft will prevent matches from being visible in the front-end.'),
        ),
        migrations.AlterField(
            model_name='division',
            name='include_forfeits_in_played',
            field=touchtechnology.common.db.models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='division',
            name='rank_division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='competition.RankDivision'),
        ),
        migrations.AlterField(
            model_name='division',
            name='season',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='divisions', to='competition.Season'),
        ),
        migrations.AlterField(
            model_name='division',
            name='slug_locked',
            field=touchtechnology.common.db.models.BooleanField(default=False, verbose_name='Slug locked'),
        ),
        migrations.AlterField(
            model_name='divisionexclusiondate',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='drawformat',
            name='is_final',
            field=touchtechnology.common.db.models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ground',
            name='venue',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='grounds', to='competition.Venue'),
        ),
        migrations.AlterField(
            model_name='ladderentry',
            name='opponent',
            field=touchtechnology.common.db.models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='competition.Team'),
        ),
        migrations.AlterField(
            model_name='laddersummary',
            name='team',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ladder_summary', to='competition.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='away_team',
            field=touchtechnology.common.db.models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='away_games', to='competition.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='away_team_eval_related',
            field=touchtechnology.common.db.models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='competition.Match'),
        ),
        migrations.AlterField(
            model_name='match',
            name='away_team_undecided',
            field=touchtechnology.common.db.models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='away_games', to='competition.UndecidedTeam'),
        ),
        migrations.AlterField(
            model_name='match',
            name='bye_processed',
            field=touchtechnology.common.db.models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='forfeit_winner',
            field=touchtechnology.common.db.models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='competition.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team',
            field=touchtechnology.common.db.models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='home_games', to='competition.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team_eval_related',
            field=touchtechnology.common.db.models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='competition.Match'),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team_undecided',
            field=touchtechnology.common.db.models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='home_games', to='competition.UndecidedTeam'),
        ),
        migrations.AlterField(
            model_name='match',
            name='include_in_ladder',
            field=touchtechnology.common.db.models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='is_bye',
            field=touchtechnology.common.db.models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='match',
            name='is_forfeit',
            field=touchtechnology.common.db.models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='match',
            name='is_washout',
            field=touchtechnology.common.db.models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='match',
            name='stage',
            field=touchtechnology.common.db.models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='matches', to='competition.Stage'),
        ),
        migrations.AlterField(
            model_name='match',
            name='stage_group',
            field=touchtechnology.common.db.models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='matches', to='competition.StageGroup', verbose_name='Pool'),
        ),
        migrations.AlterField(
            model_name='match',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='club',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='members', to='competition.Club'),
        ),
        migrations.AlterField(
            model_name='person',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='place',
            name='slug_locked',
            field=touchtechnology.common.db.models.BooleanField(default=False, verbose_name='Slug locked'),
        ),
        migrations.AlterField(
            model_name='rankdivision',
            name='enabled',
            field=touchtechnology.common.db.models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='rankdivision',
            name='slug_locked',
            field=touchtechnology.common.db.models.BooleanField(default=False, verbose_name='Slug locked'),
        ),
        migrations.AlterField(
            model_name='season',
            name='competition',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='seasons', to='competition.Competition'),
        ),
        migrations.AlterField(
            model_name='season',
            name='complete',
            field=touchtechnology.common.db.models.BooleanField(default=False, help_text='Set to indicate this season is in the past. Optimises progression calculations.'),
        ),
        migrations.AlterField(
            model_name='season',
            name='enabled',
            field=touchtechnology.common.db.models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='season',
            name='forfeit_notifications',
            field=touchtechnology.common.db.models.ManyToManyField(blank=True, help_text='When a team advises they are forfeiting, notify the opposition team plus these people.', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='season',
            name='mvp_results_public',
            field=models.DateTimeField(blank=True, help_text='The time when the results of the MVP voting will be made public on the website. Leave blank to show at all times.', null=True, verbose_name='MVP public at'),
        ),
        migrations.AlterField(
            model_name='season',
            name='slug_locked',
            field=touchtechnology.common.db.models.BooleanField(default=False, verbose_name='Slug locked'),
        ),
        migrations.AlterField(
            model_name='season',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='season',
            name='statistics',
            field=touchtechnology.common.db.models.BooleanField(default=True, help_text='Set to No if you do not wish to keep scoring or most valuable player statistics.'),
        ),
        migrations.AlterField(
            model_name='seasonassociation',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='officials', to='competition.Club'),
        ),
        migrations.AlterField(
            model_name='seasonassociation',
            name='person',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='competition.Person'),
        ),
        migrations.AlterField(
            model_name='seasonassociation',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='officials', to='competition.Season'),
        ),
        migrations.AlterField(
            model_name='seasonexclusiondate',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='seasonmatchtime',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Until'),
        ),
        migrations.AlterField(
            model_name='seasonmatchtime',
            name='start',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='seasonmatchtime',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='From'),
        ),
        migrations.AlterField(
            model_name='simplescorematchstatistic',
            name='match',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='statistics', to='competition.Match'),
        ),
        migrations.AlterField(
            model_name='simplescorematchstatistic',
            name='player',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='statistics', to='competition.Person'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='carry_ladder',
            field=touchtechnology.common.db.models.BooleanField(default=False, help_text='Set this to <b>Yes</b> if this stage should carry over values from the previous stage.', verbose_name='Carry over points'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='division',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stages', to='competition.Division'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='follows',
            field=touchtechnology.common.db.models.ForeignKey(blank=True, help_text='When progressing teams into this stage, which earlier stage should be used for determining positions.<br>Default is the immediately preceeding stage.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preceeds', to='competition.Stage'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='keep_ladder',
            field=touchtechnology.common.db.models.BooleanField(default=True, help_text='Set this to <b>No</b> if this stage does not need to keep a competition ladder.<br>Usually set to No for a Final Series or a Knockout stage.', verbose_name='Keep a ladder'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='keep_mvp',
            field=touchtechnology.common.db.models.BooleanField(default=True, help_text='Set this to <b>No</b> if this stage does not need to keep track of MVP points.<br>Usually set to No for a Final Series.', verbose_name='Keep MVP stats'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='scale_group_points',
            field=touchtechnology.common.db.models.BooleanField(default=False, help_text='In stages with multiple pools, adjust points in the smaller groups to compensate for the reduced opportunity to score points.<br>You <strong>should</strong> also set 0 points for Bye matches.'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='slug_locked',
            field=touchtechnology.common.db.models.BooleanField(default=False, verbose_name='Slug locked'),
        ),
        migrations.AlterField(
            model_name='stagegroup',
            name='carry_ladder',
            field=touchtechnology.common.db.models.BooleanField(default=False, help_text='Set this to <b>Yes</b> if the ladder for this pool should carry over values from the previous stage.<br>Will only apply for matches played against teams that are now in this group.', verbose_name='Carry over points'),
        ),
        migrations.AlterField(
            model_name='stagegroup',
            name='slug_locked',
            field=touchtechnology.common.db.models.BooleanField(default=False, verbose_name='Slug locked'),
        ),
        migrations.AlterField(
            model_name='stagegroup',
            name='stage',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pools', to='competition.Stage'),
        ),
        migrations.AlterField(
            model_name='team',
            name='division',
            field=touchtechnology.common.db.models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='teams', to='competition.Division'),
        ),
        migrations.AlterField(
            model_name='team',
            name='names_locked',
            field=touchtechnology.common.db.models.BooleanField(default=False, help_text='When the team name is locked, the team manager will not be able to change their team name.<br>As a tournament manager you can always change the names.'),
        ),
        migrations.AlterField(
            model_name='team',
            name='rank_division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='competition.RankDivision'),
        ),
        migrations.AlterField(
            model_name='team',
            name='slug_locked',
            field=touchtechnology.common.db.models.BooleanField(default=False, verbose_name='Slug locked'),
        ),
        migrations.AlterField(
            model_name='team',
            name='timeslots_after',
            field=models.TimeField(blank=True, help_text='Specify the earliest time that this team can play. Leave blank for no preference.', null=True, verbose_name='Start after'),
        ),
        migrations.AlterField(
            model_name='team',
            name='timeslots_before',
            field=models.TimeField(blank=True, help_text='Specify the latest time that this team can play. Leave blank for no preference.', null=True, verbose_name='Start before'),
        ),
        migrations.AlterField(
            model_name='teamassociation',
            name='is_player',
            field=touchtechnology.common.db.models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='teamassociation',
            name='person',
            field=touchtechnology.common.db.models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='competition.Person'),
        ),
        migrations.AlterField(
            model_name='teamassociation',
            name='team',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='people', to='competition.Team'),
        ),
        migrations.AlterField(
            model_name='teamrole',
            name='competition',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_roles', to='competition.Competition'),
        ),
        migrations.AlterField(
            model_name='undecidedteam',
            name='stage',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='undecided_teams', to='competition.Stage'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='season',
            field=touchtechnology.common.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='venues', to='competition.Season'),
        ),
    ]
