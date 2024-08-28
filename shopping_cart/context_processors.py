from .cart import Cart

def cart(request):
    cart_in_context = Cart(request)
    num_items = len(cart_in_context)
    plural = ''
    if num_items in (11, 12, 13, 14):
        plural = 'ов'
    elif str(num_items)[-1] == '1':
        plural = ''
    elif str(num_items)[-1] in ('2', '3', '4'):
        plural = 'а'
    else:
        plural = 'ов'
    return {'cart': Cart(request), 'plural': plural}