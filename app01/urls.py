from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book),
    path('query_book/', views.query_book),
    path('query_book_by_name/', views.query_book_by_name),
    path('query_publish/', views.query_publish),
    path('query_publish_by_city/', views.query_publish_by_city),
    path('query_author/', views.query_author),
    path('query_authors_add/', views.query_authors_add),
    path('query_avg_price/', views.query_avg_price),
    path('query_book_multi/', views.query_book_multi),
    path('query_publish_min/', views.query_publish_min),
    path('query_book_dync/', views.query_book_dync),
    path('add_emp/', views.add_emp),
]