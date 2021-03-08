from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from django.views.decorators.csrf import csrf_exempt
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
from django.core import serializers
from .models import SignUp,SignUp2
from .forms import RegisterForm
from django.db import connection
import string 
import random 
# Create your views here.
# class RegistrationView(GenericAPIView):
#     ser_data_class = UserSerializer
#     def post(self,request):
#         ser_data = UserSerializer(data = request.data)
#         if(ser_data.is_valid()):
#             ser_data.save()
#             return Response(ser_data.data,status =201)
#         return Response(ser_data.errors,status =400)
@csrf_exempt
def post(request):
    ser_data = RegisterForm()
    if request.method =='POST':
        print('inside_POST')
        ser_data = RegisterForm(request.POST)
        if ser_data.is_valid():
            print('inside_Valid')
            # ser_data.save()
            res =''.join(random.choices(string.ascii_uppercase + string.digits, k = 7)) 
            print(str(res))
            return HttpResponse('Your New Referral Code is: '+ str(res),status =201)
    return HttpResponse(status =400)

#Without Forms
@csrf_exempt
def post2(request):
    if request.method =='POST':
        print('inside_POST')
        first_name_v = (request.POST.get('first_name'))
        last_name_v = (request.POST.get('last_name'))
        email_v = (request.POST.get('email'))
        username_v = (request.POST.get('username'))
        new_score = str(request.POST.get('referral_code'))
        query_res = my_custom_sql(new_score)
        if(query_res == True):
            print("here_at_100")
            score_tab = 100
        else:
            print("here_at_0")
            score_tab = 0
        res =''.join(random.choices(string.ascii_uppercase + string.digits, k = 7))
        reg_data= SignUp2(first_name=first_name_v, last_name=last_name_v,email=email_v,username=username_v,referral_code=str(res),score=score_tab)
        reg_data.save()
        return HttpResponse('Your New Referral Code is: '+ str(res),status =201)
    return HttpResponse(status =400) 




@csrf_exempt
def get_data(request):
    send_data_class = UserSerializer()
    if request.method=='GET':        
    # if request.method == 'GET':
        fetch_data = my_custom_sql()
        # qs_json = serializers.serialize('json', fetch_data)
        qs_json = fetch_data
        # resp = json.loads(fetch_data)
        # if(fetch_data.hasattr()):
        print(fetch_data)
        return HttpResponse(qs_json, content_type='application/json',status = 200)
    return HttpResponse("Kuch nhi mila",status = 400)

def my_custom_sql(ref_code):
    with connection.cursor() as cursor:
        try:
            print("inside_try of SQL",ref_code)
            code = str(ref_code)
            # cursor.execute("UPDATE SignUp2 SET score = score+100 where referral_code = %s",[ref_code])
            cursor.execute("update ref_app_SignUp2 Set score = score + 100 WHERE SignUp2.referral_code = %s",[code])
            cursor.execute("SELECT score from  ref_app_SignUp2  WHERE SignUp2.referral_code = %s",[code])
            row = cursor.fetchone()
            print("Executed")
            # cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
            row = cursor.fetchone()
            print(row)
            return True
        except:
            return False
        finally:
            cursor.close()
