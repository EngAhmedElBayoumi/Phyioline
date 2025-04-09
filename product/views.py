from django.shortcuts import render , redirect  , get_object_or_404
from django.contrib import messages
from .models import *
# pagination
from django.core.paginator import Paginator
from django.db.models import Q
# import gettext_lazy as _
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from account.models import CustomUser
from django.conf import settings
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def product(request):
    products=Product.objects.all().order_by('-id')    
    product_count=products.count()
    paginator=Paginator(products, 12)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    category=Category.objects.all()
    
    context={
        'products':page_obj,
        'category':category,
        "product_count":product_count, 
    }
    return render(request, 'shop.html',context)


def search(request):
    obj=request.GET['obj']
    # filter by title or title_ar icontains=obj
    products = Product.objects.filter(Q(title__icontains=obj) | Q(title_ar__icontains=obj))    
    
    product_count=products.count()
    paginator=Paginator(products, 12)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    category=Category.objects.all()
    
    context={
        'products':page_obj,
        'category':category,
        "product_count":product_count, 
    }
    return render(request, 'shop.html',context)




def category_filter(request,obj):
    # filter by category.name or category.name_ar icontains=obj
    products = Product.objects.filter(Q(category__name__icontains=obj) | Q(category__name_ar__icontains=obj))
    product_count=products.count()
    paginator=Paginator(products, 12)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    category=Category.objects.all()
    
    context={
        'products':page_obj,
        'category':category,
        "product_count":product_count, 
    }
    return render(request, 'shop.html',context)

def cart(request):
    return render(request, 'cart.html')


def wishlist(request):
    return render(request, 'wishlist.html')


def shop_details(request,slug):
    product=get_object_or_404(Product, slug=slug)
    reviews_count=product.reviews.count()
    
    
    context={
        'product':product,
        'reviews_count':reviews_count,
    }
    return render(request, 'shop-details-1.html', context)



# cart
@login_required
def cart(request):
    product=Card.objects.filter(user=request.user)
    total_price_after_discount=0
    total_price=0
    for item in product:
        total_price_after_discount+=item.total_price_after_discount
        total_price+=item.total_price
    context={    
        'product':product,
        'total_price_after_discount':total_price_after_discount,
        'total_price':total_price,
    }
    return render(request, 'cart.html', context)



@login_required
def update_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        quantity = int(request.POST.get("quantity", 1))

        # Get the cart item for the current user
        cart_item = get_object_or_404(Card, user=request.user, product_id=product_id)

        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()  # Remove item if quantity is 0

        # Recalculate totals
        cart_items = Card.objects.filter(user=request.user)
        total_price = sum(item.total_price for item in cart_items)
        total_price_after_discount = sum(item.total_price_after_discount for item in cart_items)

        return JsonResponse({
            "status": "success",
            "total_price": total_price,
            "total_price_after_discount": total_price_after_discount,
            "item_total": cart_item.total_price if quantity > 0 else 0,
        })

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


# add to card
@login_required
def add_to_card(request, slug):
    if request.method == "GET" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        product = get_object_or_404(Product, slug=slug)
        quantity = int(request.GET.get("quantity", 1))  # Default to 1 if not provided

        card, created = Card.objects.get_or_create(user=request.user, product=product, defaults={'quantity': quantity})

        if not created:
            card.quantity += quantity
            card.save()

        return JsonResponse({
            "status": "success",
            "message": _("Product added to cart"),
            "product_name": product.name,
            "quantity": card.quantity
        })
    
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)
    
    
# add to card
def add_to_card_2(request, slug):
    product=get_object_or_404(Product, slug=slug)
    card, created=Card.objects.get_or_create(user=request.user, product=product)
    if not created:
        card.quantity+=1
        card.save()
    messages.success(request, _('Product added to card'))
    # return to the same page that the user was before
    return redirect(request.META.get('HTTP_REFERER'))
        
# add to wishlist
def add_to_wishlist(request, slug):
    product=get_object_or_404(Product, slug=slug)
    wishlist=Wishlist.objects.create(user=request.user, product=product)
    messages.success(request, _('Product added to wishlist'))
    return redirect('product:wishlist')
    

def add_to_wishlist_2(request, slug):
    product=get_object_or_404(Product, slug=slug)
    wishlist=Wishlist.objects.create(user=request.user, product=product)
    messages.success(request, _('Product added to wishlist'))
    return redirect(request.META.get('HTTP_REFERER'))
    


def wishlist(request):
    wishlist=Wishlist.objects.filter(user=request.user)
    context={
        'wishlist':wishlist,
    }
    return render(request, 'wishlist.html', context)

    

# remove from card
def remove_from_card(request, slug):
    product=get_object_or_404(Product, slug=slug)
    card=get_object_or_404(Card, user=request.user, product=product)
    card.delete()
    messages.success(request, _('Product removed from card'))
    return redirect('product:cart')


# remove from wishlist
def remove_from_wishlist(request, slug):
    product=get_object_or_404(Product, slug=slug)
    wishlist=get_object_or_404(Wishlist, user=request.user, product=product)
    wishlist.delete()
    messages.success(request, _('Product removed from wishlist'))
    return redirect('product:wishlist')



@login_required
def create_payment_intention(request, amount, currency):
    try:
        # Step 1: Authentication Request
        auth_response = requests.post(
            'https://accept.paymob.com/api/auth/tokens',
            json={
                'api_key': settings.PAYMOB_API_KEY
            }
        )
        auth_response.raise_for_status()
        token = auth_response.json()['token']

        # Generate a unique order ID using timestamp
        import time
        merchant_order_id = f"order_{int(time.time())}"

        # Step 2: Order Registration
        order_response = requests.post(
            'https://accept.paymob.com/api/ecommerce/orders',
            json={
                'auth_token': token,
                'delivery_needed': 'false',
                'merchant_order_id': merchant_order_id,
                'amount_cents': 20000,  # Static amount 200 EGP
                'currency': 'EGP',
                'items': []
            }
        )
        order_response.raise_for_status()
        order_id = order_response.json()['id']

        # Print full response for debugging
        print("Order Response:", order_response.text)

        # Step 3: Payment Key Request
        payment_key_request = {
            'auth_token': token,
            'amount_cents': 20000,  # Static amount 200 EGP
            'expiration': 3600,
            'order_id': order_id,
            'billing_data': {
                'first_name': "Ahmed",
                'last_name': "Mohamed",
                'email': "test@test.com",
                'phone_number': "01234567890",
                'street': "NA",
                'building': "NA",
                'floor': "NA",
                'apartment': "NA",
                'city': "Cairo",
                'country': "EG",
                'state': "Cairo",
                'postal_code': "11511"
            },
            'currency': 'EGP',
            'integration_id': 4548403,  # Online Card integration ID
            'lock_order_when_paid': 'false',
            'shipping_data': {
                'first_name': "Ahmed",
                'last_name': "Mohamed",
                'email': "test@test.com",
                'phone_number': "01234567890",
                'street': "NA",
                'building': "NA",
                'floor': "NA",
                'apartment': "NA",
                'city': "Cairo",
                'country': "EG",
                'state': "Cairo",
                'postal_code': "11511"
            }
        }

        # Print request payload for debugging
        print("Payment Key Request:", json.dumps(payment_key_request, indent=2))

        payment_key_response = requests.post(
            'https://accept.paymob.com/api/acceptance/payment_keys',
            json=payment_key_request
        )

        # Print full response for debugging
        print("Payment Key Response:", payment_key_response.text)

        payment_key_response.raise_for_status()
        payment_key = payment_key_response.json()['token']

        # Generate the iframe URL with the correct format
        iframe_url = f'https://accept.paymob.com/api/acceptance/iframes/835633?payment_token={payment_key}'

        print("Generated iframe URL:", iframe_url)  # Debug print

        return {
            'status': 'success',
            'order_id': order_id,
            'payment_key': payment_key,
            'checkout_url': iframe_url
        }

    except requests.exceptions.RequestException as e:
        print("API Error:", str(e))
        if hasattr(e.response, 'text'):
            print("Error Response:", e.response.text)
        return {
            'status': 'error',
            'message': str(e)
        }
    except Exception as e:
        print("General Error:", str(e))
        return {
            'status': 'error',
            'message': str(e)
        }

@login_required
def get_payment_details(request):
    try:
        # Return static amount for testing
        return 200, "EGP", None
    except Exception as e:
        return None, None, str(e)

@login_required
def initiate_payment(request):
    try:
        amount, currency, error = get_payment_details(request)
        if error:
            return JsonResponse({'status': 'error', 'message': error}, status=400)

        result = create_payment_intention(request, amount, currency)
        
        if result['status'] == 'success':
            # Store order_id in session for later verification
            request.session['paymob_order_id'] = result['order_id']
            request.session['payment_amount'] = float(amount)
            
            return redirect(result['checkout_url'])
        else:
            return JsonResponse({'status': 'error', 'message': result['message']}, status=500)

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

# Add new views for specific payment methods
@login_required
def pay_with_card(request):
    return initiate_payment(request)

@login_required
def pay_with_wallet(request):
    request.GET = request.GET.copy()
    request.GET['method'] = 'wallet'
    return initiate_payment(request)

@login_required
def pay_with_cash(request):
    request.GET = request.GET.copy()
    request.GET['method'] = 'cash'
    return initiate_payment(request)

@login_required
def pay_with_paypal(request):
    request.GET = request.GET.copy()
    request.GET['method'] = 'paypal'
    return initiate_payment(request)

@login_required
def payment_complete(request):
    try:
        order_id = request.session.get('paymob_order_id')
        if not order_id:
            messages.error(request, _('Invalid payment session'))
            return redirect('product:cart')

        # Verify payment status with Paymob
        auth_response = requests.post(
            'https://accept.paymob.com/api/auth/tokens',
            json={'api_key': settings.PAYMOB_API_KEY}
        )
        token = auth_response.json()['token']

        order_response = requests.get(
            f'https://accept.paymob.com/api/ecommerce/orders/{order_id}/',
            params={'auth_token': token}
        )
        order_data = order_response.json()

        if order_data['status'] == 'paid':
            # Clear cart
            Card.objects.filter(user=request.user).delete()
            
            # Clear session data
            if 'paymob_order_id' in request.session:
                del request.session['paymob_order_id']
            if 'payment_amount' in request.session:
                del request.session['payment_amount']
                
            messages.success(request, _('Payment successful! Thank you for your purchase.'))
            return redirect('product:product')
        else:
            messages.error(request, _('Payment verification failed'))
            return redirect('product:cart')

    except Exception as e:
        messages.error(request, _('Payment verification failed'))
        return redirect('product:cart')