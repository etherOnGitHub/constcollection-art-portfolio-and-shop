from django.db import migrations, models
import cloudinary.models

class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='video_url',
            field=cloudinary.models.CloudinaryField(blank=True, null=True, verbose_name='video'),
        ),
    ]
