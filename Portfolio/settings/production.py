from .base import *

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['awarenessthroughcode.pythonanywhere.com']

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DB-NAME'),
#         'USER': config('DB-USER'),
#         'PASSWORD': config('DB-PASSWORD'),
#         'HOST': config('DB-HOST'),
#         'PORT': config('DB-PORT'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'), 
    }
}

# STRIPE_PUBLIC_KEY = config('STRIPE-PUBLIC-KEY')
# STRIPE_SECRET_KEY = config('STRIPE-SECRET-KEY') 