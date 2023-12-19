from django.contrib.auth.models import Group, Permission


def is_member(user):
    return user.groups.filter(name='moderator').exists()
