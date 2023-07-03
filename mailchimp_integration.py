import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
from . import settings


def initialize_mailchimp_client():
    client = MailchimpMarketing.Client()
    client.set_config({
        "api_key": settings.MAILCHIMP_API_KEY,
        "server": settings.MAILCHIMP_SERVER_PREFIX,
    })

    try:
        response = client.ping.get()
        print(response)
    except ApiClientError as error:
        print(f"Mailchimp API error: {error}")

    return client