"""
Настройки Django для проекта Store.

Сгенерировано «django-admin startproject» с использованием Django 4.2.2.

Дополнительные сведения об этом файле см.
https://docs.djangoproject.com/en/4.2/topics/settings/

Полный список настроек и их значений см.
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
from pathlib import Path

# Создавайте пути внутри проекта следующим образом: BASE_DIR 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Настройки быстрого старта разработки — не подходят для продакшена
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# ВНИМАНИЕ ПО БЕЗОПАСНОСТИ: держите секретный ключ, используемый в производстве, в секрете!
SECRET_KEY = 'django-insecure-_$q8-n&3ln5-mt*#p32%51^4d(97mmwact2*q@_kun+5$h85ay'

# ПРЕДУПРЕЖДЕНИЕ: ITY не запускается с включенной отладкой!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition (Определение приложения)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',
    'news.apps.NewsConfig',
    'subscriptions.apps.SubscriptionsConfig',
    'django_filters',
    # В данный раздел добавьте 3 обязательных приложения allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # и одно, которое отвечает за выход через Yandex
    'allauth.socialaccount.providers.yandex',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # AccountMiddleware действует как связующее звено между
    # процессом обработки запросов Django, системой сессий, аутентификацией и перенаправлениями,
    # это ключевой элемент для работы 'django-allauth'.
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'News_Portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'news/templates/news')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # для `allauth` обязательно нужен этот процессор ('django.template.context_processors.request',)
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'News_Portal.wsgi.application'


# Database (База данных)
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation (Проверка пароля)
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization (Интернационализация)
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Статические файлы (CSS, JavaScript, изображения)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'


# Тип поля первичного ключа по умолчанию
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#  После входа, пользователя перенаправляем на страницу с новостями.
LOGIN_REDIRECT_URL = "/news"

# Этого раздела может не быть, добавьте его в указанном виде.
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

'''
Первые два параметра указывают на то, что поле email является обязательным и уникальным. 
Третий, наоборот, — говорит, что username необязательный. 
Следующий параметр указывает, что аутентификация будет происходить посредством электронной почты. 
Напоследок мы указываем, что верификация почты отсутствует. 

Обычно на почту отправляется подтверждение аккаунта, 
после подтверждения которого восстанавливается полная функциональность учётной записи.
'''

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# 'none' - проверка email — отсутствует;
# 'mandatory' — не пускать пользователя на сайт до момента подтверждения почты;
# 'optional' — сообщение о подтверждении почты будет отправлено, но пользователь может залогиниться на сайте
# без подтверждения почты.
# Чтобы allauth распознал нашу форму как ту, что должна выполняться вместо формы по умолчанию, необходимо добавить
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

# Блок кода настроек нашего проекта работы с почтой (Yandex-почтой)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # для писем в терминал
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# класс отправителя сообщений (у нас установлено значение по умолчанию, а значит, эта строчка не обязательна)
EMAIL_HOST = 'smtp.yandex.ru'
# Хост почтового сервера - это адрес или доменное имя сервера, который обрабатывает и отправляет электронную почту.
# Хост почтового сервера может быть использован как для отправки, так и для получения почты
EMAIL_PORT = 465
"""
Порт, на который почтовый сервер принимает письма, называется почтовым портом. 
Один из самых распространенных почтовых портов - это порт 25, который используется для передачи электронной почты 
по протоколу SMTP (Simple Mail Transfer Protocol). 
Однако, существуют и другие почтовые порты, 
такие как порт 587, который используется для SMTP с шифрованием TLS (Transport Layer Security), 
и порт 465, который используется для SMTP с шифрованием SSL (Secure Sockets Layer). 
Использование конкретного почтового порта зависит от настроек и требований почтового сервера.
"""
EMAIL_HOST_USER = "AndreyTestSF"
# логин пользователя почтового сервера
EMAIL_HOST_PASSWORD = "zuqvkobqbkixymje"
# пароль пользователя почтового сервера
EMAIL_USE_TLS = False
# необходимость использования TLS
# (зависит от почтового сервера, смотрите документацию по настройке работы с сервером по SMTP)
EMAIL_USE_SSL = True
# необходимость использования SSL
# (зависит от почтового сервера, смотрите документацию по настройке работы с сервером по SMTP)

DEFAULT_FROM_EMAIL = "AndreyTestSF@yandex.ru"
# почтовый адрес отправителя по умолчанию
# Последняя строчка будет использоваться как значение по умолчанию для поля from в письме.
# То есть будет отображаться в поле «отправитель» у получателя письма

SERVER_EMAIL = "AndreyTestSF@yandex.ru"
# SERVER_EMAIL содержит адрес почты, от имени которой будет отправляться письмо при вызове mail_admins и mail_manager.
# А переменная MANAGERS будет хранить список имён менеджеров и адресов их почтовых ящиков.

ADMINS = (
    ('ADMIN', 'ADMIN@zhiza.net'),
    ('admin', 'admin@mail.com'),
)

EMAIL_SUBJECT_PREFIX = 'News Portal'
