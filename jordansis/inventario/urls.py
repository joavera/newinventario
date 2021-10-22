from django.contrib import admin
from django.urls import path
from .import views
from .views import grupolistar,grupoguardar, grupomodificar
from .views import clientelistar,clienteguardar,clientemodificar
from .views import proveedorlistar, proveedorguardar, proveedormodificar
from .views import productoslistar, productosguardar, productosmodificar
from .views import notalistar, notaguardar, notamodificar
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('grupolistar', grupolistar.as_view(),name='grupolistar'),
    path('grupoguardar', grupoguardar.as_view(),name='grupoguardar'),
    path('grupomodificar/<int:pk>',grupomodificar.as_view(),name='grupomodificar'),
    path('holapdf',views.hello_pdf,name='holapdf'),
    path('grupospdf',views.grupos_print,name='grupospdf'),
    path('grupoindividual/<int:pk>',views.grupos_print,name='grupoindividual'),

########################### CLIENTES #############################################################################################
    path('clientelistar',clientelistar.as_view(),name='clientelistar'),
    path('clienteguardar',clienteguardar.as_view(),name='clienteguardar'),
    path('clientemodificar/<int:pk>',clientemodificar.as_view(),name='clientemodificar'),
    path('clientepdf',views.cliente_print,name='clientepdf'),
    path('clienteindividual/<int:pk>',views.cliente_print,name='clienteindividual'),

########################### PROVEEDOR ############################################################################################
    path('proveedorlistar',proveedorlistar.as_view(),name='proveedorlistar'),
    path('proveedorguardar',proveedorguardar.as_view(),name='proveedorguardar'),
    path('proveedormodificar/<int:pk>',proveedormodificar.as_view(),name='proveedormodificar'),
    path('proveedorpdf',views.proveedor_print,name='proveedorpdf'),
    path('proveedorindividual/<int:pk>',views.proveedor_print,name='proveedorindividual'),

########################### PRODUCTOS ############################################################################################
    path('productoslistar',productoslistar.as_view(),name='productoslistar'),
    path('productosguardar',productosguardar.as_view(),name='productosguardar'),
    path('productosmodificar/<int:pk>',productosmodificar.as_view(),name='productosmodificar'),
    path('productospdf',views.productos_print,name='productospdf'),
    path('productosindividual/<int:pk>',views.productos_print,name='productosindividual'),

########################### login ################################
    path('', auth_views.LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuario/login.html'), name='logout'),

    path('notaslistar',notalistar.as_view(),name='notaslistar'),
    path('notasguardar', notaguardar.as_view(), name='notasguardar'),
    path('notasdificar/<int:pk>', notamodificar.as_view(), name='notasmodificar'),
    path('notaspdf',views.nota_print,name='notaspdf'),
    path('notasindividual/<int:pk>', views.nota_print, name='notasindividual'),

]





