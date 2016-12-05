# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casino_finder', '0003_auto_20161123_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='DegreeModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('institute_name', models.CharField(max_length=50)),
                ('instititute_location', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='DesignationModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('institute_name', models.CharField(max_length=50)),
                ('instititute_location', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='DoctorBioModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to=b'pictures', verbose_name=b'Picture')),
                ('telephone_no', models.IntegerField(verbose_name=b'Telephone No')),
                ('available_time', models.IntegerField(verbose_name=b'Available Time')),
                ('degree_ids', models.ForeignKey(verbose_name=b'Degree', to='casino_finder.DegreeModel')),
                ('designation_ids', models.ForeignKey(verbose_name=b'Designation', to='casino_finder.DesignationModel')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Doctors',
            },
        ),
        migrations.CreateModel(
            name='HospitalINFModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='SpecialistModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('institute_name', models.CharField(max_length=50)),
                ('instititute_location', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='doctorbiomodel',
            name='present_organization_ids',
            field=models.ForeignKey(verbose_name=b'Present Organization', to='casino_finder.HospitalINFModel'),
        ),
        migrations.AddField(
            model_name='doctorbiomodel',
            name='specialist_ids',
            field=models.ForeignKey(verbose_name=b'Specialist', to='casino_finder.SpecialistModel'),
        ),
    ]
