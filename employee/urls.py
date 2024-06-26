from django.urls import path
from .views import *

urlpatterns = [
    # Home
    path('', home, name='home'),

    # Department URLs
    path('departments/', DepartmentListView.as_view(), name='department_list'),
    path('departments/create/', DepartmentCreateView.as_view(), name='department_create'),
    path('departments/update/<int:pk>/', DepartmentUpdateView.as_view(), name='department_update'),
    path('emp/department/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department_delete'),
    # Employee URLs
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
    path('export-employee-data/', ExportEmployeeDataView.as_view(), name='export_employee_data'),
    
    # Attendance URLs
    path('attendance/create/', AttendanceCreateView.as_view(), name='attendance_create'),
    path('attendance/monthly-absence-count/', monthly_absence_count, name='monthly_absence_count'),

    # Overtime URLs
    path('overtime/create/', OvertimeCreateView.as_view(), name='overtime_add'),
    path('overtime/list/', OvertimeListView.as_view(), name='overtime_list'),
]
