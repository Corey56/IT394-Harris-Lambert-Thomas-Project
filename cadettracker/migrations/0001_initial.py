# Generated by Django 3.0.3 on 2020-05-08 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BuildingName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Floor', models.IntegerField()),
                ('RoomNum', models.IntegerField()),
                ('RoomDescription', models.CharField(max_length=50)),
                ('BLDGName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadettracker.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xNum', models.CharField(max_length=6)),
                ('jobTitle', models.CharField(max_length=15)),
                ('phoneNum', models.CharField(max_length=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadettracker.Company')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadettracker.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Regiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RegNum', models.IntegerField()),
                ('RegSupplyLocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadettracker.Location')),
            ],
        ),
        migrations.CreateModel(
            name='RegHasSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=15)),
                ('NumberAvailable', models.IntegerField()),
                ('RegimentID', models.IntegerField()),
                ('Location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadettracker.Location')),
            ],
        ),
        migrations.CreateModel(
            name='RegHasPersonnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadettracker.Regiment')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadettracker.Personnel')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyNeedsSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumRequested', models.IntegerField()),
                ('CompanyLabel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadettracker.Company')),
                ('Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadettracker.Supply')),
                ('Location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadettracker.Location')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyHasSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumAvailable', models.IntegerField()),
                ('CompanyLabel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadettracker.Company')),
                ('Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadettracker.Supply')),
                ('Location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadettracker.Location')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='LocationID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadettracker.Location'),
        ),
        migrations.AddField(
            model_name='company',
            name='regiment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadettracker.Regiment'),
        ),
    ]