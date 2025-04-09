from django.http import JsonResponse
from django.db.models import Count, Sum
from django.db.models.functions import TruncDate
from django.utils import timezone
from datetime import timedelta
from product.models import Product, Order, OrderItem
from account.models import CustomUser as User, SuplierRequest as Supplier

def get_dashboard_stats(request):
    """Get total counts for products, orders, and suppliers"""
    user = request.user
    base_product_query = Product.objects
    base_order_query = Order.objects
    base_supplier_query = User.objects.filter(type="suplier")

    # If user is not superuser, filter data for their specific records
    if not user.is_superuser:
        if user.type == "suplier":
            base_product_query = base_product_query.filter(suplier=user)
            base_order_query = base_order_query.filter(orderitem__product__suplier=user).distinct()
        elif user.type == "customer":
            base_order_query = base_order_query.filter(user=user)
            base_product_query = base_product_query.filter(orderitem__order__user=user).distinct()

    stats = {
        'total_products': base_product_query.count(),
        'total_orders': base_order_query.count(),
        'total_suppliers': base_supplier_query.count() if user.is_superuser else 0,
        'total_revenue': base_order_query.filter(status='paid').aggregate(total=Sum('total_price'))['total'] or 0,
        'pending_orders': base_order_query.filter(status='pending').count(),
        'total_categories': base_product_query.values('category').distinct().count(),
    }
    return JsonResponse(stats)

def get_chart_data(request):
    """Get chart data for the last 7 and 30 days"""
    user = request.user
    last_7_days = timezone.now() - timedelta(days=7)
    last_30_days = timezone.now() - timedelta(days=30)

    # Base queries with user filtering
    base_product_query = Product.objects
    base_order_query = Order.objects
    base_supplier_query = User.objects.filter(type="suplier")

    # If user is not superuser, filter data for their specific records
    if not user.is_superuser:
        if user.type == "suplier":
            base_product_query = base_product_query.filter(suplier=user)
            base_order_query = base_order_query.filter(orderitem__product__suplier=user).distinct()
        elif user.type == "customer":
            base_order_query = base_order_query.filter(user=user)
            base_product_query = base_product_query.filter(orderitem__order__user=user).distinct()

    # Products data
    products_7_days = list(base_product_query.filter(
        created_at__gte=last_7_days
    ).annotate(
        date=TruncDate('created_at')
    ).values('date').annotate(
        count=Count('id')
    ).order_by('date'))

    products_30_days = list(base_product_query.filter(
        created_at__gte=last_30_days
    ).annotate(
        date=TruncDate('created_at')
    ).values('date').annotate(
        count=Count('id')
    ).order_by('date'))

    # Orders data
    orders_7_days = list(base_order_query.filter(
        created_at__gte=last_7_days
    ).annotate(
        date=TruncDate('created_at')
    ).values('date').annotate(
        count=Count('id'),
        total=Sum('total_price')
    ).order_by('date'))

    orders_30_days = list(base_order_query.filter(
        created_at__gte=last_30_days
    ).annotate(
        date=TruncDate('created_at')
    ).values('date').annotate(
        count=Count('id'),
        total=Sum('total_price')
    ).order_by('date'))

    # Suppliers data - only show for superusers
    suppliers_7_days = list(base_supplier_query.filter(
        date_joined__gte=last_7_days
    ).annotate(
        date=TruncDate('date_joined')
    ).values('date').annotate(
        count=Count('id')
    ).order_by('date')) if user.is_superuser else []

    suppliers_30_days = list(base_supplier_query.filter(
        date_joined__gte=last_30_days
    ).annotate(
        date=TruncDate('date_joined')
    ).values('date').annotate(
        count=Count('id')
    ).order_by('date')) if user.is_superuser else []

    # Order status distribution
    order_status = list(base_order_query.values('status').annotate(
        count=Count('id')
    ))

    return JsonResponse({
        'products_7_days': products_7_days,
        'products_30_days': products_30_days,
        'orders_7_days': orders_7_days,
        'orders_30_days': orders_30_days,
        'suppliers_7_days': suppliers_7_days,
        'suppliers_30_days': suppliers_30_days,
        'order_status': order_status
    }) 