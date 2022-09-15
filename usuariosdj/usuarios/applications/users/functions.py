# Funciones extra de la aplicación Users

import random
from secrets import choice
import string



def code_generator(size=6,chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))