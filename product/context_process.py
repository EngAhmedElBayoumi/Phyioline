from .models import Card , Wishlist


def cart_count(request):
    if request.user.is_authenticated:
        cards = Card.objects.filter(user=request.user).count()
        return {'cart':cards}
    else:
        return {'cart':None}
    
