from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User, Organization, Project, Task, Report
from .serializers import UserSerializer, OrganizationSerializer, ProjectSerializer, TaskSerializer, ReportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inventory, Sales
from .serializers import InventorySerializer
from .inventory_utils import inventory_turnover, days_of_inventory_on_hand, forecast_sales, reorder_points


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrganizationListCreateAPIView(ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class OrganizationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class ProjectListCreateAPIView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ReportListCreateAPIView(ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
from django.shortcuts import render

class InventoryInsights(APIView):
    def post(self, request):
        sales_data = request.data.get("sales_data")
        average_inventory = request.data.get("average_inventory")
        lead_time = request.data.get("lead_time")
        safety_stock = request.data.get("safety_stock")
        days_to_forecast = request.data.get("days_to_forecast")
        
        turnover = inventory_turnover(sum(sales_data), average_inventory)
        days_on_hand = days_of_inventory_on_hand(turnover)
        forecasted_sales = forecast_sales(sales_data, days_to_forecast)
        reorder_point = reorder_points(lead_time, np.mean(sales_data), safety_stock)
        
        insights = {
            "inventory_turnover": turnover,
            "days_of_inventory_on_hand": days_on_hand,
            "forecasted_sales": forecasted_sales.tolist(),
            "reorder_point": reorder_point
        }
        
        return Response(insights)
class InventoryInsights(APIView):
    def get(self, request, format=None):
        inventory = Inventory.objects.all()
        sales = Sales.objects.all()

        sales_sum = sales.aggregate(Sum('quantity'))['quantity__sum']
        avg_inventory = inventory.aggregate(Avg('quantity'))['quantity__avg']

        turnover = inventory_turnover(sales_sum, avg_inventory)
        days_of_inventory = days_of_inventory_on_hand(turnover)

        return Response({
            'inventory_turnover': turnover,
            'days_of_inventory_on_hand': days_of_inventory
        })

class InventoryOptimization(APIView):
    def get(self, request, format=None):
        lead_time = float(request.GET.get('lead_time', 0))
        safety_stock = float(request.GET.get('safety_stock', 0))

        sales = Sales.objects.all().order_by('date')
        sales_data = [sale.quantity for sale in sales]
        daily_sales = np.mean(sales_data)
        reorder_point = reorder_points(lead_time, daily_sales, safety_stock)

        return Response({
            'reorder_point': reorder_point
        })

# Create your views here.
