from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer5, PrepaidPlan,PostpaidPlan,Dongle5,Credit,BankAxis,BankSBI,Complaint,Faq


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer5
        # fields=['id','name','address','pincode','email','select_num','prepostdon','plan','kyc_date']
        fields = "__all__"


class PrepaidPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrepaidPlan
        fields = "__all__"


class PostpaidPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostpaidPlan
        fields = "__all__"


class DongleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dongle5
        fields = "__all__"


class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = "__all__"

class BankAxisSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAxis
        fields = "__all__"

class BankSBISerializer(serializers.ModelSerializer):
    class Meta:
        model = BankSBI
        fields = "__all__"

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = "__all__"

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model=Faq
        fields="__all__"
