from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def pasar_a_dict(tuplaChoices):
        llaves = []
        for e in tuplaChoices:
            llaves.append(e[0])
        valores = []
        for e in tuplaChoices:
            valores.append(e[1])
        dict = {}
        for i in range(len(valores)):
            dict[llaves[i]]=valores[i]
        return dict
        

def group_or_staff_member_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
                          login_url='login'):
    """
    Decorator for views that checks that the user is logged in and is part of a group
    named 'administrador', redirecting to the login page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (u.groups.filter(name='administrador') or u.is_staff),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

