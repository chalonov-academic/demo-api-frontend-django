from django.urls import path
from biblioteca import views, views_autor, views_libro

# Prueba de contribución

urlpatterns = [
    path("biblioteca/", views.library_home_view, name='biblioteca_home'),
    path("biblioteca/autores/", views_autor.users_list, name='autor_list'),
    path("biblioteca/autores/search", views_autor.user_search, name='autor_search'),
    path("biblioteca/libros/", views_libro.users_list, name='libro_list'),
    path("biblioteca/libros/search", views_libro.user_search, name='libro_search'),
]
