from django.db import models

# Create your models here.

class MainAccount(models.Model):
    _id         = models.AutoField(primary_key=True)
    checking    = models.CharField(max_length=150)
    saving      = models.CharField(max_length=150)

    # have these connect to all 
    routing_num = models.IntegerField()
    account_num = models.IntegerField()

    def __str__(self):
        return self.name


class User(models.Model):
    id          = models.AutoField(primary_key=True)
    full_name   = models.CharField(max_length=200)
    user_name   = models.CharField(max_length=200)
    email       = models.CharField(max_length=150)
    password    = models.CharField(max_length=255)
    api_key     = models.CharField(max_length=255)

    # having it connected to the main account 
    # routing_num = models.ForeignKey(MainAccount, on_delete=models.CASCADE)
    # account_num = models.ForeignKey(MainAccount, on_delete=models.CASCADE)
    
    routing_num = models.IntegerField()
    account_num = models.IntegerField()

    def __str__(self):
        return self.name



class Loan(models.Model):
    _id                  = models.AutoField(primary_key=True)
    ext_routing_payment  = models.CharField(max_length=150)
    ext_acct_num_payment = models.CharField(max_length=150)
    loan_Size            = models.BigIntegerField()
    apr                  = models.IntegerField()
    monthly_payment      = models.CharField(max_length=150)
    
    # date and time that it's due before a late fee is set
    payment_due          = models.CharField(max_length=150) 

    # routing_num = models.ForeignKey(MainAccount, on_delete=models.CASCADE)
    # account_num = models.ForeignKey(MainAccount, on_delete=models.CASCADE)
    routing_num = models.IntegerField()
    account_num = models.IntegerField()

    def __str__(self):
        return self.name


class HouseLoad(models.Model):
    _id                     = models.AutoField(primary_key=True)
    ext_routing_payment     = models.CharField(max_length=150)
    ext_acct_num_payment    = models.CharField(max_length=150)
    loan_Size               = models.BigIntegerField()
    apr                     = models.IntegerField()
    monthly_payment         = models.CharField(max_length=150)

    # date and time that it's due before a late fee is set
    payment_due = models.CharField(max_length=150)

    # routing_num = models.ForeignKey(MainAccount, on_delete=models.CASCADE)
    # account_num = models.ForeignKey(MainAccount, on_delete=models.CASCADE)

    routing_num = models.IntegerField()
    account_num = models.IntegerField()

    def __str__(self):
        return self.name


class CarLoan(models.Model):
    _id                   = models.AutoField(primary_key=True)
    ext_routing_payment   = models.CharField(max_length=150)
    ext_acct_num_payment  = models.CharField(max_length=150)
    loan_Size             = models.BigIntegerField()
    apr                   = models.IntegerField()
    monthly_payment       = models.CharField(max_length=150)

    # date and time that it's due before a late fee is set
    payment_due = models.CharField(max_length=150)

    # routing_num = models.ForeignKey(MainAccount, on_delete=models.CASCADE)
    # account_num = models.ForeignKey(MainAccount, on_delete=models.CASCADE)

    routing_num = models.IntegerField()
    account_num = models.IntegerField()

    def __str__(self):
        return self.name
    


class CompoundInvesting(models.Model):
    id                        = models.AutoField(primary_key=True)
    Compound_interest_Percent = models.CharField(max_length=255)
    invest_num                = models.CharField(max_length=255)

    # routing_num = models.ForeignKey(MainAccount, on_delete=models.CASCADE)
    # account_num = models.ForeignKey(MainAccount, on_delete=models.CASCADE)

    routing_num = models.IntegerField()
    account_num = models.IntegerField()

    def __str__(self):
        return self.name
