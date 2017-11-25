import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'pastebin',
	'social_django',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
			],
		},
	},
]

AUTHENTICATION_BACKENDS = (
 'social_core.backends.open_id.OpenIdAuth',
 'social_core.backends.google.GoogleOpenId',
 'social_core.backends.google.GoogleOAuth2',
 'django.contrib.auth.backends.ModelBackend',
)

WSGI_APPLICATION = 'mysite.wsgi.application'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'



#/*****************************************************************************\
#                                 Keep Hidden
#\*****************************************************************************/

SECRET_KEY = 'SECRET_KEY'

EXPIRY_DAYS = 30 # Days after which the code snippet will be deleted

# Social Outh
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY    = 'TOKEN'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'SECRET'

# E-mail ssettings
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'PASSWORD'
EMAIL_HOST_USER     = 'EMAIL@EMAIL.COM'
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True