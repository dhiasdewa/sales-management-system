from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_login, name='login'),
    path('hr-dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('employee-dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('inventory/', views.inventory_list, name='inventory'),
    path("export-sales/", views.export_sales_excel, name="export_sales"),
    path("export-top-products/", views.export_top_selling_products, name="export_top_products"),
    path("add-sale/", views.add_sale, name="add_sale"),
]