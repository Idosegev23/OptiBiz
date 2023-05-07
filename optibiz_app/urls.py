from django.urls import path
from .views import (
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView,
    OrganizationListCreateAPIView,
    OrganizationRetrieveUpdateDestroyAPIView,
    ProjectListCreateAPIView,
    ProjectRetrieveUpdateDestroyAPIView,
    TaskListCreateAPIView,
    TaskRetrieveUpdateDestroyAPIView,
    ReportListCreateAPIView,
    ReportRetrieveUpdateDestroyAPIView,
    InventoryInsights,
    InventoryOptimization,
)

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user_list_create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user_retrieve_update_destroy'),
    path('organizations/', OrganizationListCreateAPIView.as_view(), name='organization_list_create'),
    path('organizations/<int:pk>/', OrganizationRetrieveUpdateDestroyAPIView.as_view(), name='organization_retrieve_update_destroy'),
    path('projects/', ProjectListCreateAPIView.as_view(), name='project_list_create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project_retrieve_update_destroy'),
    path('tasks/', TaskListCreateAPIView.as_view(), name='task_list_create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task_retrieve_update_destroy'),
    path('reports/', ReportListCreateAPIView.as_view(), name='report_list_create'),
    path('reports/<int:pk>/', ReportRetrieveUpdateDestroyAPIView.as_view(), name='report_retrieve_update_destroy'),
    path('inventory-insights/', InventoryInsights.as_view(), name='inventory-insights'),
        path('inventory_optimization/', InventoryOptimization.as_view(), name='inventory_optimization'),
]
