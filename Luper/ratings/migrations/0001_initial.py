# Generated by Django 4.2.1 on 2023-11-15 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_rating', models.IntegerField()),
                ('age_recommendation', models.CharField(max_length=100)),
                ('mood_type', models.CharField(choices=[('Fun', 'Fun'), ('Comedy', 'Comedy'), ('Light-Hearted', 'Light-Hearted'), ('Romantic', 'Romantic'), ('Dramatic', 'Dramatic'), ('Suspenseful', 'Suspenseful'), ('Heartwarming', 'Heartwarming'), ('Inspirational', 'Inspirational'), ('Sad', 'Sad'), ('Melancholic', 'Melancholic'), ('Nostalgic', 'Nostalgic'), ('Fantasy', 'Fantasy'), ('Mysterious', 'Mysterious'), ('Action-Packed', 'Action-Packed'), ('Adventurous', 'Adventurous'), ('Documentary', 'Documentary'), ('Educational', 'Educational'), ('Artistic', 'Artistic'), ('Family-Friendly', 'Family-Friendly'), ('Dark/Horror', 'Dark/Horror'), ('Sci-Fi', 'Sci-Fi'), ('Epic', 'Epic')], max_length=500)),
                ('theme_label', models.CharField(max_length=50)),
                ('theme_description', models.TextField(max_length=2000, verbose_name='theme description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'movie')},
            },
        ),
    ]
