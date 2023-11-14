from django.test import TestCase
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
import os


from django.core.management.utils import get_random_secret_key
 
print(get_random_secret_key())

class TryDjangoConfigTeste(TestCase):

    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        # self.assertEqual(SECRET_KEY, '0tezyx_h7uc8&^*#3%7kkvtv35y#03!6ydy7yw=m+xeyabzfny')
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'Weak Secret Ket {e.messages}'
            self.fail(msg)