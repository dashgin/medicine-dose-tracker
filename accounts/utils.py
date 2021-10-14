import random

from django.utils.text import slugify


def unique_username_generator(instance, base_field, new_username=None):
    """ Generate unique username from given <new_username> or <base_field> of user"""

    unique_username = new_username if (new_username is not None) else slugify(base_field)
    user = instance.__class__  # solution for AttributeError:"Manager isn't accessible via User instances"
    while user.objects.filter(username=unique_username).exists():
        random_number = random.randint(1, 9_999)
        unique_username = f'{unique_username}-{random_number}'
    instance.username = unique_username
    return instance.username
