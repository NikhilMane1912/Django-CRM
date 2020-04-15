import os


# Make this unique, and don't share it with anybody.
# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = 'YOUR_SECRET_KEY'


# Email Server Settings
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.getenv('SG_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('SG_PWD', '')
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Database Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dd96v3avhpjfs0',
        'USER': 'aoobrebuyfnrku',
        'PASSWORD': '2430c7d85a7aec13d36f6ef89c6fc77a7c0c8c7e61cecab5bcc79a128f8a1064',
        'HOST': 'ec2-34-197-212-240.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}

# Server Customizations
ADMIN_EMAIL = "you@your_email.com"
URL_FOR_LINKS = "https://crm.example.com"


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True
