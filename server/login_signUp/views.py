from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.middleware import csrf
import json

from lib.util.util import generateAPIKey, rnd
from .models import MainAccount ,User ,Loan ,HouseLoan ,CarLoan ,CompoundInvesting

main_account        = MainAccount()
user                = User()
loan                = Loan()
house_load          = HouseLoan()
car_loan            = CarLoan()
compound_investing  = CompoundInvesting()

def index(request):
    return csrf.get_token(request)
    

def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)


        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)
        
        # process data here

        return JsonResponse({'message': 'Data processed successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


def signUp(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            print(data)

            user_name   = data['user_name']
            password    = data['password']
            email       = data['email']
            api_key     = generateAPIKey(150)
            routing_num = rnd(10)
            acct_num    = rnd(10)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)

        # process data here

        

        return JsonResponse(
                {
                    'message': 'Data processed successfully.',
                    "token": api_key,
                }
            )
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)



def forgot(request):
    return HttpResponse('hello forgot')
