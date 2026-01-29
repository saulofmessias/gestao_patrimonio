import decouple  # Se usar .env

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': decouple.config('DB_NAME', default='gestao_patrimonio'),
        'USER': decouple.config('DB_USER', default='postgres'),
        'PASSWORD': decouple.config('DB_PASSWORD', default=''),
        'HOST': decouple.config('DB_HOST', default='localhost'),
        'PORT': decouple.config('DB_PORT', default='5432'),
    }
}

# Cloudinary (adicione se não tiver)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': decouple.config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': decouple.config('CLOUDINARY_API_KEY'),
    'API_SECRET': decouple.config('CLOUDINARY_API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Login configs
LOGIN_URL = '/admin/'
LOGIN_REDIRECT_URL = '/admin/'

# Outros (INSTALLED_APPS já tem?)
INSTALLED_APPS += [
    'jazzmin',  # Se instalou
    'cloudinary_storage',
    'crispy_forms',
    'crispy_bootstrap5',
    'patrimonio',  # Seu app
]
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'
