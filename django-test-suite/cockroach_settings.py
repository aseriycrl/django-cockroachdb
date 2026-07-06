DATABASES = {
    'default': {
        'ENGINE': 'django_cockroachdb',
        'NAME': 'django_tests',
        'USER': os.environ['CRDB_USER'],
        'PASSWORD': os.environ['CRDB_PASSWORD'],
        'HOST': os.environ['CRDB_HOST'],
        'PORT': 26257,
        'OPTIONS': {
            'server_side_binding': True,
        },
    },
    'other': {
        'ENGINE': 'django_cockroachdb',
        'NAME': 'django_tests2',
        'USER': os.environ['CRDB_USER'],
        'PASSWORD': os.environ['CRDB_PASSWORD'],
        'HOST': os.environ['CRDB_HOST'],
        'PORT': 26257,
        'OPTIONS': {
            'server_side_binding': True,
        },
    },
}

SECRET_KEY = 'django_tests_secret_key'
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
USE_TZ = False
