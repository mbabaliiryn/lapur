from notify.signals import notify
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver





@receiver(user_signed_up)
def activity_handler_new_signup(request, user, **kwargs):

notify.send(request.user, recipient=admin, actor=request.user
verb='joined', nf_type='user_joined')
    



