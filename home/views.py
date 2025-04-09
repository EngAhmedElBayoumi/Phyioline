from django.shortcuts import render
from product.models import Product , Category , Card , OrderItem , Order , Wishlist , Review
from account.models import CustomUser , SuplierRequest
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
# import gettext_lazy as _
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission
from .models import About , Vission , Mission , Terms_and_condition , refund_and_policy
# Create your views here.


def home(request):
    # Get the first 8 categories
    categories = Category.objects.all()[:8]
    
    # Get all products ordered by ID (latest first)
    products = Product.objects.all().order_by('-id')
    
    about = About.objects.first()
    mission=Mission.objects.first()
    vission=Vission.objects.first()
    
    # Prepare context with products filtered by category
    category_products = {category.name.strip(): products.filter(category=category)[:8] for category in categories}    
    # Debugging: Print category and product counts
    for name, prods in category_products.items():
        print(f"Category: {name}, Products: {prods.count()}")
    
    context = {
        'categories': categories,
        'products': products,
        'category_products': category_products,
        'about': about,
        'mission': mission,
        'vission': vission
    }
    
    return render(request, 'index.html', context)




def terms_conditions(request):
    terms=Terms_and_condition.objects.first()
    context={
        "terms":terms
    }
    return render(request, 'TearmsCondition.html',context)


def refund_and_policy_def (request):
    refund=refund_and_policy.objects.first()
    context={
        "refund":refund
    }
    return render(request, 'refund.html',context)

def apply(request):
    if request.method == 'POST':
        # get nam , email , phone , account_statement , commercial_register , tax_card , id_card , password,confirm_password 
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        account_statement = request.FILES.get('account_statement')
        commercial_register = request.FILES.get('commercial_register')
        tax_card = request.FILES.get('tax_card')
        id_card = request.FILES.get('id_card')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # check if password and confirm_password are same
        if password != confirm_password:
            messages.error(request, _('Passwords do not match'))
            return render(request, 'singUp.html', {'error': 'Passwords do not match'})
        # check if email already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, _('Email already exists'))
            return render(request, 'singUp.html', {'error': 'Email already exists'})
        
        # validate that all data is entered
        if not all([name, email, phone, account_statement, commercial_register, tax_card, id_card, password, confirm_password]):
            messages.error(request, _('Please fill all fields'))
            return render(request, 'singUp.html', {'error': 'Please fill all fields'})
        
        # create user
        user = CustomUser.objects.create_user(email=email, password=password, username=name, phone=phone)
        user.type = 'suplier'
        user.save()
        
        # give it djangomodelpermission for Product , Card , Order , WishList (full crud)
        user.is_staff = True
        user.save()
        
        # create supplier request
        SuplierRequest.objects.create(
            user=user,
            account_statement=account_statement,
            commercial_register=commercial_register,
            tax_card=tax_card,
            id_card=id_card,
        )
        messages.success(request, _('Your request has been sent successfully'))
    return render(request, 'singUp.html')


