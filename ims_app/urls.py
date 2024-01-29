from django.urls import path
from .views import *


urlpatterns = [
    path('company_info/',CompanyInfoApiView.as_view(),name='company info'),
    path('company_info/<int:pk>/',CompanyInfoIdApiView.as_view(),name='company info detail'),
    # path('user-info/',UserInfo.as_view(),name='user info detail'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('admin-create/',admin_create,name='admin-create'),
    path('group/',GroupApiView.as_view(),name='group list'),
    path('product_type/',ProductTypeApiView.as_view(),name='product type list'),
    path('product_type/<int:pk>/',ProductTypeIdApiView.as_view(),name='product type list detail'),
    path('product_info/',ProductsApiView.as_view(),name='product info'),
    path('product_infoid/<int:pk>/', ProductInfoIdApiView.as_view(), name='product_type_detail'),
    path('buyer_info/',BuyerInfoApiView.as_view(),name='buyer list'),
    path('buyer_infoid/<int:pk>/',BuyerInfoIdApiView.as_view(),name='buyer list detail'),
    path('seller_info/',SellerInfoApiView.as_view(),name='seller list'),
    path('seller_infoid/<int:pk>/',SellerInfoIdApiView.as_view(),name='seller list detail'),
    path('vendor_info/',VendorInfoApiView.as_view(),name='vendor list'),
    path('vendor_info/<int:pk>/',VendorInfoIdApiView.as_view(),name='vendor list detail'),
    path('purchase_info/',PurchaseInfoApiView.as_view(),name='purhase list'),
    path('purchase_info/<int:pk>/',PurchaseInfoIdApiView.as_view(),name='purhase list detail'),
]