from django.urls import path
from .views import (
    CodeListView,
    CodeDetailView,
    CodeCreateView,
    CodeUpdateView,
    CodeDeleteView,
    output
)

from . import views

urlpatterns = [
    path('', CodeListView.as_view(), name='code-home'),
    path('codes/output', output, name='output'),
    path('codes/<int:pk>/', CodeDetailView.as_view(), name='code-detail'),
    path('codes/new/', CodeCreateView.as_view(), name='code-create'),
    path('codes/<int:pk>/update/', CodeUpdateView.as_view(), name='code-update'),
    path('codes/<int:pk>/delete/', CodeDeleteView.as_view(), name='code-delete'),
    
]