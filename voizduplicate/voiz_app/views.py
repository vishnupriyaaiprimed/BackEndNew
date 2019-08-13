from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Customer5, PrepaidPlan,PostpaidPlan,Dongle5,Credit, BankAxis, BankSBI, Complaint, Faq
from rest_framework import viewsets
from .serializers import UserSerializer, CustomerSerializer, PrepaidPlanSerializer,PostpaidPlanSerializer,DongleSerializer,CreditSerializer, BankAxisSerializer, BankSBISerializer, ComplaintSerializer, FaqSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def home(request):
    return render(request, 'home.html')


def prepaid(request):
    return render(request, 'prepaid.html')


def postpaid(request):
    return render(request, 'postpaid.html')

# new connection


def pay(request):
    #     if request.method == 'POST':
    #         ncname = request.POST['ncname']
    #         ncphone_num = request.POST['ncphone_no']
    #         ncaddress = request.POST['ncaddress']
    #         ncemail = request.POST['ncemail']
    #         ncpincode = request.POST['ncpincode']
    #         ncdate = request.POST['ncdate']
    #         newconn = NewConnection(name=ncname, phone_num=ncphone_num,
    #                                 address=ncaddress, email=ncemail, pincode=ncpincode, date=ncdate)
    #         newconn.save()

    return render(request, 'pay.html')


def login(request):
    #     if request.method == 'POST':
    #         name = request.POST['name']
    #         phone_num = request.POST['phone_num']
    #         pw = request.POST['pw']
    #         retype_pw = request.POST['retype_pw']

    #         ou = OnlineUsers(name=name, phone_num=phone_num,
    #                          pw=pw, retype_pw=retype_pw)

    #         ou.save()

    #         # salt = uuid.uuid4().hex
    #         # hpw = hashlib.sha512(pw + salt).hexdigest()
    #         user, created = User.objects.get_or_create(
    #             username=phone_num, is_staff=True)
    #         user.set_password(pw)
    #         user.save()
    #         # u = User(username=name, password=pw)
    #         # u.save()

    return render(request, 'login.html')


def createaccount(request):
    return render(request, 'createaccount.html')


def newconnection(request):
    return render(request, 'newconn.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSetByNum(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class UserViewSetByUsername(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'last_name'


class CustomerViewSetByNum(viewsets.ModelViewSet):
    queryset = Customer5.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'phone_num'


class PostpaidPlanViewSetByNum(viewsets.ModelViewSet):
    serializer_class = PostpaidPlanSerializer
    queryset = PostpaidPlan.objects.all()


class PrepaidPlanViewSetByNum(viewsets.ModelViewSet):
    serializer_class = PrepaidPlanSerializer
    queryset = PrepaidPlan.objects.all()


class DongleViewSetByNum(viewsets.ModelViewSet):
    serializer_class = DongleSerializer
    queryset = Dongle5.objects.all()

    

class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer

class CreditViewSetByNum(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    lookup_field = 'cardnumber'


class BankAxisViewSet(viewsets.ModelViewSet):
    queryset = BankAxis.objects.all()
    serializer_class = BankAxisSerializer
    
class BankAxisViewSetByNum(viewsets.ModelViewSet):
    queryset = BankAxis.objects.all()
    serializer_class = BankAxisSerializer
    lookup_field = 'accountnumber'


class BankSBIViewSet(viewsets.ModelViewSet):
    queryset = BankSBI.objects.all()
    serializer_class = BankSBISerializer

class BankSBIViewSetByNum(viewsets.ModelViewSet):
    queryset = BankSBI.objects.all()
    serializer_class = BankSBISerializer
    lookup_field = 'accountnumber'


class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

class FaqViewSet(viewsets.ModelViewSet):
    queryset=Faq.objects.all()
    serializer_class=FaqSerializer
