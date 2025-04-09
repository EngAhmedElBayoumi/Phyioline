from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from product.models import Product, Order
from account.models import SuplierRequest as Supplier
from account.models import CustomUser as User
from unfold.views import UnfoldModelAdminViewMixin
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from .api import get_dashboard_stats, get_chart_data

class DashboardView(UnfoldModelAdminViewMixin, TemplateView):
    title = _("Dashboard")
    permission_required = ()
    template_name = "admin/index.html"

    def __init__(self, model_admin, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_admin = model_admin

def toggle_sidebar(request):
    """Toggle the sidebar state"""
    if request.session.get('sidebar_collapsed'):
        request.session['sidebar_collapsed'] = False
    else:
        request.session['sidebar_collapsed'] = True
    return JsonResponse({'status': 'success'})

# Register models with the default admin site
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Supplier)

# Add custom URLs to the default admin site
admin.site.get_urls = lambda: [
    path('toggle-sidebar/', admin.site.admin_view(toggle_sidebar), name='toggle_sidebar'),
    path('dashboard-stats/', admin.site.admin_view(get_dashboard_stats), name='dashboard_stats'),
    path('chart-data/', admin.site.admin_view(get_chart_data), name='chart_data'),
    path('', admin.site.admin_view(DashboardView.as_view(model_admin=admin.site)), name='index'),
] + admin.site.get_urls()
    
    
