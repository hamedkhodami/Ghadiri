from apps.core.utils import send_sms


class NotificationUser:

    @classmethod
    def mobile_verification_code_handler(cls, notification, phone_number):
        pattern = '6yk1gp8ytmyk7ia'
        send_sms(phone_number, pattern, **{'verification-code': notification.kwargs['code']})

    @classmethod
    def subscription_end_warning(cls, notification, phone_number):
        pattern = '6ykk1gp8ytmykk7ia'
        send_sms(phone_number, pattern, days=notification.kwargs['days'])

    @classmethod
    def new_ticket_created(cls, notification, phone_number):
        pattern = 'l9ps8j8a19ysv9h'
        send_sms(phone_number, pattern, name=notification.to_user.get_full_name())

    @classmethod
    def new_ticket_created_admin(cls, notification, phone_number):
        pattern = '68dhge9j2geb5at'
        send_sms(phone_number, pattern, name=notification.to_user.get_full_name())

    @classmethod
    def new_subscription_registered_admin(cls, notification, phone_number):
        pattern = 'mkomyeb4pc763kk'
        send_sms(phone_number, pattern, user_name=notification.to_user.get_full_name())

    @classmethod
    def new_counseling_registered_admin(cls, notification, phone_number):
        pattern = 'j8or87s3zoaaxio'
        send_sms(phone_number, pattern, user_name=notification.to_user.get_full_name())

    @classmethod
    def new_user_registered_admin(cls, notification, phone_number):
        pattern = 'g3lskg36yfl8d1r'
        send_sms(phone_number, pattern, user_name=notification.to_user.get_full_name())


NOTIFICATION_USER_HANDLERS = {
    'MOBILE_VERIFICATION_CODE': NotificationUser.mobile_verification_code_handler,
    'NEW_SUBSCRIPTION_REGISTERED_ADMIN': NotificationUser.new_subscription_registered_admin,
    'NEW_USER_ADMIN': NotificationUser.new_user_registered_admin,
    'NEW_COUNSELING_FORM_SUBMITED_ADMIN': NotificationUser.new_counseling_registered_admin,
    'SUBSCRIPTION_END_WARNING': NotificationUser.subscription_end_warning,
    'NEW_TICKET_CREATED': NotificationUser.new_ticket_created,
    'NEW_TICKET_CREATED_ADMIN': NotificationUser.new_ticket_created_admin,
}
