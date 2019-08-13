from django.db import models

class Customer5(models.Model):
    PR = 'Prepaid'
    PO = 'Postpaid'
    DO = 'Dongle'
    prepost = ((PR, 'Prepaid'), (PO, 'Postpaid'), (DO, 'Dongle'))

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pincode = models.IntegerField()
    aadhar = models.CharField(max_length=100)
    aadhar_verified = models.BooleanField()
    email = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=10)
    type1 = models.CharField(max_length=8, choices=prepost)
    plan = models.CharField(max_length=10)
    kyc_date = models.DateField()

    balance = models.CharField(max_length=50)
    expiriesIn = models.CharField(max_length=100)
    callUsage = models.CharField(max_length=500)#(9092564782,10/08/19,10min);(9898989898,11/08/19,12min)
    dataUsage = models.CharField(max_length=500)#(10/08/19,10Mb);(11/08/19,11Mb)
    smsUsage = models.CharField(max_length=500)#(9092564782,10/08/19,10);(9092464782,11/08/19,15)
    bill = models.CharField(max_length=2000)#(9873547692,74968736,20-06-2019,15-07-2019 to 20-07-2019,30-07-2019,Rs.300,0);(9873547692,74968736,20-05-2019,15-07-2019 to 20-07-2019,30-07-2019,Rs.200,1)

    def __str__(self):
        return self.phone_num


class PrepaidPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    duration = models.CharField(max_length=200)
    talktime = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    sms = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.plan_name


class PostpaidPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    duration = models.CharField(max_length=200)
    talktime = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    sms = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.plan_name


class Dongle5(models.Model):
    # PR = 'PR'
    # PO = 'PO'
    # typ = ((PR, 'Prepaid'), (PO, 'Postpaid'))
    plan_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    data = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    # types = models.CharField(max_length=50, choices=typ)

    def __str__(self):
        return self.plan_name





class Credit(models.Model):
    cardnumber = models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    pinnumber = models.CharField(max_length=100)
    balance = models.CharField(max_length=100)

    def __str__(self):
        return self.cardnumber
        

class BankAxis(models.Model):
    accountnumber = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    balance = models.CharField(max_length=100)

    def __str__(self):
        return self.accountnumber


class BankSBI(models.Model):
    accountnumber = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    balance = models.CharField(max_length=100)

    def __str__(self):
        return self.accountnumber

class Complaint(models.Model):
    phone_num = models.CharField(max_length=100)
    msg = models.CharField(max_length=100)

class Faq(models.Model):
    q=models.CharField(max_length=250)
    a=models.CharField(max_length=500)

    def __str__(self):
        return self.q
