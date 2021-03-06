# Generated by Django 2.2 on 2022-02-06 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('alias_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('token', models.CharField(max_length=254)),
                ('first_login', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SlotDetails',
            fields=[
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('slot_detail_id', models.IntegerField(blank=True, null=True)),
                ('candidate_name', models.CharField(blank=True, max_length=50, null=True)),
                ('recruiter_name', models.CharField(blank=True, max_length=50, null=True)),
                ('recruiter_id', models.IntegerField(primary_key=True, serialize=False)),
                ('mp_item_date', models.DateField(blank=True, null=True)),
                ('mp_type', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'slot_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SlotAsscTime',
            fields=[
                ('slot_assc_pers_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_assc_id', models.IntegerField(blank=True, null=True)),
                ('slot_timing', models.CharField(max_length=20)),
            ],
        ),
    ]
