from django.urls import path,re_path
from . import views


urlpatterns = [
    path('',views.customer,name='customer'),
    path('ServiceRequest/',views.servicerequest,name='ServiceRequest'),
    re_path(r'^entry_id/(?P<entry_id>[0-9]+)$',views.editservicerequest,name='entry_id'),

    path('TrackRequest/', views.trackrequest, name='TrackRequest'),
    path('button/', views.chooseoption, name='button')

]