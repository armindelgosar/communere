from to_do.models import ProductManager, Developer

user_types = {
    'developer': Developer,
    'product_manager': ProductManager,
}

USER_TYPE_DEVELOPER = 'developer'
USER_TYPE_PRODUCT_MANAGER = 'product_manager'
