


from django.urls import path
from .views import (
    ProductoListView,
    ProductoCreateView,
    ProductoDetailView,
    ProductoUpdateView,
    ProductoDeleteView
    
)

urlpatterns = [

   path("listar", ProductoListView.as_view(), name="lista_productos"),
   path("crear", ProductoCreateView.as_view(), name = "lista_productos"),
   path("producto/<int:pk>", ProductoDetailView.as_view(), name = "detail_producto")
]