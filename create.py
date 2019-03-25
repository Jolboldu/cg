from custom_user.models import User
user = User.objects.create_user(username='bob',
                                 password='bob')

