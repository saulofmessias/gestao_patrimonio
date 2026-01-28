from django.db import migrations, models
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('patrimonio', '0001_initial'),  # Se não existir, crie vazio
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaPatrimonio',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nome
