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

def index(request): # todo: find a way to make this more secure for apis
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

            # checking if the initial savings and checking is not set
            if data['savings_init'] is not None and data['checking_init'] is not None:
                full_name       = data['full_name']
                User_name       = data['user_name']
                password        = data['password']
                email           = data['email']
                api_key         = generateAPIKey(150)
                routing_nums    = rnd(10)
                acct_num        = rnd(10)
                checkingN       = data['checking_init']
                savings         = data['savings_init']
                
            else:
                full_name       = data['full_name']
                User_name       = data['user_name']
                password        = data['password']
                email           = data['email']
                api_key         = generateAPIKey(150)
                routing_nums    = rnd(10)
                acct_num        = rnd(10)
                checkingN       = 0.0
                savings         = 0.0

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)

        # process data here
        mAccount = MainAccount(
            checking    = checkingN,
            saving      = savings,
            routing_num = routing_nums, # should be the same
            account_num = acct_num # should be the same
        )
        usr = User(
            full_name   = full_name,
            user_name   = User_name,
            email       = email,
            password    = password,
            api_key     = api_key,
            routing_num = routing_nums, # should be the same as the MainAccount
            account_num = acct_num # should be the same as the MainAccount
        )
        loan = Loan(
            ext_routing_payment     = 0,
            ext_acct_num_payment    = 0,
            loan_Size               = 0,
            apr                     = 0,
            monthly_payment         = 0,
            payment_due             = 0,
            routing_num             = routing_nums,  # should be the same
            account_num             = acct_num  # should be the same
        )
        House_Loan = HouseLoan(
            ext_routing_payment     = 0,
            ext_acct_num_payment    = 0,
            loan_Size               = 0,
            apr                     = 0,
            monthly_payment         = 0,
            payment_due             = 0,
            routing_num             = routing_nums,  # should be the same
            account_num             = acct_num  # should be the same
        )
        car_loan = CarLoan(
            ext_routing_payment     = 0,
            ext_acct_num_payment    = 0,
            loan_Size               = 0,
            apr                     = 0,
            monthly_payment         = 0,
            payment_due             = 0,
            routing_num             = routing_nums,  # should be the same
            account_num             = acct_num  # should be the same
        )
        compound_investing = CompoundInvesting(
            Compound_interest_Percent = 0.0,
            invest_num                = 0,
            routing_num               = routing_nums,  # should be the same
            account_num               = acct_num  # should be the same
        )

        try:
            mAccount.save()
            usr.save()
            loan.save()
            House_Loan.save()
            car_loan.save()
            compound_investing.save()

        except Exception as e:
            return JsonResponse(
                {
                    "message": "Error",
                    "error-msg": str(e)
                }
            )

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
