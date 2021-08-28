from django.shortcuts import render
from .forms import user_form
from .models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import csv  

# Create your views here.

def add_view(request):
	if request.method == 'POST':
		fm = user_form(request.POST)
		if fm.is_valid():
			product_name = fm.cleaned_data['product_name']
			volume = fm.cleaned_data['volume']
			market_capital = fm.cleaned_data['market_capital']
			credit_rating = fm.cleaned_data['credit_rating']

			reg = User(product_name=product_name,volume=volume,market_capital=market_capital,credit_rating=credit_rating)
			reg.save()
			fm = user_form()
			messages.success(request,'Data added sucessfully')
	else:
		fm = user_form()
	data = User.objects.all()
	return render(request,'userdata.html',{'form': fm,'alldata':data})


def update_view(request,id):
	if request.method=='POST':
		update = User.objects.get(pk=id)
		fm = user_form(request.POST,instance=update)
		if fm.is_valid():
			fm.save()
			fm = user_form()
			messages.success(request,'Data Updated sucessfully')
			return HttpResponseRedirect('/')
	else:
		update = User.objects.get(pk=id)
		fm = user_form(instance=update)
	return render(request,'updatedata.html',{'form':fm})


def delete_view(request,id):
	if request.method=='POST':
		delete = User.objects.get(pk=id)
		delete.delete()
		return HttpResponseRedirect('/')


def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    employees = User.objects.all()  
    writer = csv.writer(response)
    for employee in employees:
    	writer.writerow(['Product Name', 'Volume', 'Market market_capital','Credit rating'])
    	writer.writerow([employee.product_name,employee.volume,employee.market_capital,employee.credit_rating])
    return response  