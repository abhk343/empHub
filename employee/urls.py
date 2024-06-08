from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name='home'),
    # Department URLs
    path('dept/', DepartmentListView.as_view(), name='department_list'),
    path('dept/create/', DepartmentCreateView.as_view(), name='department_create'),
    path('dept/update/<int:pk>/', DepartmentUpdateView.as_view(), name='department_update'),
    path('dept/delete/<int:pk>/', DepartmentDeleteView.as_view(), name='department_delete'),
    
    # Employee URLs
    path('emp/', EmployeeListView.as_view(), name='employee_list'),
    path('emp/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
    
    # Attendance URLs
    path('attcrt/', AttendanceCreateView.as_view(), name='attendance_create'),
    path('attv/', monthly_absence_count, name='monthly_absence_count'),
    
    # Overtime URLs
    path('otcrt/', OvertimeCreateView.as_view(), name='overtime_create'),
    path('otv/', OvertimeListView.as_view(), name='overtime_list'),
]
