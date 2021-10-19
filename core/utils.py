from django.core.mail import send_mail



def send_mail_to_me(customer_name,to_email,message,email,phone,extra_field):
    """
    This function will send mail to 
    customer who requested for appionment
    """
    send_mail(
    subject = f'New mail form website {extra_field}',
    message = f'Hey! {customer_name} has sent you mail.\n email = {email} \n phone = {phone}\n message = {message}' ,
    from_email = 'rkview934@gmail.com',
    recipient_list = (f'{to_email}',),
    fail_silently=True,
    )