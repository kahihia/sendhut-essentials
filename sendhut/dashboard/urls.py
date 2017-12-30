from django.conf.urls import url
from sendhut.dashboard import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^orders$', views.order_list, name='orders'),
    url(r'^join/(?P<token>[a-zA-Z0-9-]+)$', views.accept_invitation, name='join'),
    url(r'^employee/add$', views.EmployeeCreate.as_view(), name='employee_add'),
    url(r'^employees$', views.employee_list, name='employees'),
    url(r'^allowances$', views.allowance_list, name='allowances'),
    url(r'^allowance/add$', views.AllowanceCreate.as_view(), name='allowance_add'),
    url(r'^allowance/(?P<allowance_id>[a-zA-Z0-9-]+)/$', views.AllowanceUpdate.as_view(),
        name='allowance_details'),
]