from app.models.donation import Donation
from app.models.user import User
from app.models.fund import Fund
from django.contrib.auth.models import User
from django.http import QueryDict
import datetime

# business logic

def gettingDonation(id):
    id=Donation.donorId
    donation = Donation.objects.get(donor_id=id)
    return donation

def postingDonation(request):
    valueDonation= request.POST["ValueDonation"]
    dateDonation = request.POST["Fecha de la donación"]
    statusTransactionState = request.POST["Transacción exitosa(S/N)"]#Revisar ya que dependeria de otra funcionalidad
    legalState = request.POST["Donación legalizada(S/N)"] #Revisar ya que dependeria de otra funcionalidad
    donorId = User.objects.get(documentId)
    donation = Donation.objects.create(valueDonation=valueDonation,dateDonation = request.POST["Fecha de la donación"], donorId = User.objects.get(documentId))
    return donation

def puttingDonation(request,id):
    put = QueryDict(request.body)
        
    try:
        donorId = id
        donation = Donation.objects.get(id=donorId)
        donation.valueDonation = put.get('ValueDonation')
        donation.dateDonation = put.get('dateDonation')
        donation.statusTransactionState = put.get('statusTransactionState')
        donation.legalState = put.get('legalState')
        donation.save()
        
        return donation

    except Donation.full_clean(exclude=''): # revisar

        return "donation doesn´t exist"

def deletingDonation(request,id):
    donorId=id
    donation=Donation.objects.get(id=donorId)
    donation.delete()
    return ()

def checkBalance():
    date = datetime.datetime.now()
    timeLastSend = sendMoney()
    if (timeLastSend < Donation.dateDonation and Donation.dateDonation < date):
        balance = Donation.objects.all().aggregate(sum('valueDonation'))
    return balance

def sendMoney():
    actualBalance = checkBalance()
    fund = Fund()
    actualFund = fund.valueFundn + actualBalance
    timeLastSend = datetime.datetime.now()
    return timeLastSend
    #return "Exit send to fund"
    

    
