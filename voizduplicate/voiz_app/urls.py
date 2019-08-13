from django.urls import path
from .import views
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'usersbynum', views.UserViewSetByNum)
router.register(r'usersbyusername', views.UserViewSetByUsername)
router.register(r'users', views.UserViewSet)
router.register(r'customersbynum', views.CustomerViewSetByNum)

router.register(r'prepaid', views.PrepaidPlanViewSetByNum)
router.register(r'postpaid', views.PostpaidPlanViewSetByNum)
router.register(r'dongle', views. DongleViewSetByNum)

router.register(r'credit', views.CreditViewSet)
router.register(r'bankaxis', views.BankAxisViewSet)
router.register(r'banksbi', views.BankSBIViewSet)

router.register(r'creditbynum', views.CreditViewSetByNum)
router.register(r'bankaxisbynum', views.BankAxisViewSetByNum)
router.register(r'banksbibynum', views.BankSBIViewSetByNum)


router.register(r'complaint',views.ComplaintViewSet)
router.register(r'faq',views.FaqViewSet)

urlpatterns = [

    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('createaccount', views.createaccount, name="createaccount"),
    path('newconnection', views.newconnection, name="newconnection"),
    path('pay', views.pay, name="pay"),



    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/',ObtainAuthToken.as_view())

]
