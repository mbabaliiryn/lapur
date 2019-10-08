
from django_rq import job  






@job
def send_new_user_joined(instance):
    instance = clean_instance(instance, get_user_model())
    subject = "{} joined ".format(instance.display_name)
    to = ORGANISATION_STAFF_UPDATE_EMAIL_RECIPIENTS
    ctx = {
        'user': instance,
        'user_url': '%s/people/%s/' % (ORGANISATION_URL, instance.username)
    }
    send_mail(subject, 'organisation/email/new_user', to, ctx)