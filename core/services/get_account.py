from django.core.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from core.models import BaseAccount
from core.statics import user_types


def get_account(user):
    try:
        account = get_object_or_404(BaseAccount, pk=user.pk)
        return account
    except BaseAccount.DoesNotExist:
        raise ValidationError('Account with this id does not exist!')


def get_product_manager(user):
    try:
        account = get_object_or_404(BaseAccount, pk=user.pk)
        if account.user_type == user_types.USER_TYPE_PRODUCT_MANAGER:
            return account.productmanager
        raise BaseAccount.DoesNotExist()
    except BaseAccount.DoesNotExist:
        raise ValidationError('PRODUCT MANAGER with this id does not exist!')


def get_developer(user):
    try:
        account = get_object_or_404(BaseAccount, pk=user.pk)
        if account.user_type == user_types.USER_TYPE_DEVELOPER:
            return account.developer
        raise BaseAccount.DoesNotExist()
    except BaseAccount.DoesNotExist:
        raise ValidationError('DEVELOPER with this id does not exist!')
