# Generated by Django 4.1.5 on 2023-02-05 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscourseFeedbackInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_post_timestamp', models.DateField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.application')),
            ],
        ),
        migrations.CreateModel(
            name='DiscourseFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.TextField()),
                ('username', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('parent_post_id', models.TextField(blank=True, null=True)),
                ('like_count', models.IntegerField(blank=True, null=True)),
                ('created_at_discourse', models.DateTimeField()),
                ('updated_at_discourse', models.DateTimeField(blank=True, null=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.application')),
            ],
        ),
    ]