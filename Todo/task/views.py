from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,CustomerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Customer
# Create your views here.


@login_required(login_url='login')
def index(request):
	customers=Customer.objects.all()
	form=CustomerForm(request.POST)
	if request.method=='POST':
	
		if form.is_valid():
			form.save()
			return redirect('home page')
		else:
			form=CustomerForm()
	return render(request,'task/index.html',{'form':form,'customers':customers})


def delete_items(request, pk):
	data = Customer.objects.get(id=pk)
	if request.method == 'POST':
		data.delete()
		# messages.success(request,'successfully deleted')
		return redirect('home page')
	return render(request, 'task/task_confirm_delete.html')




    


def register(request):
	form=UserRegistrationForm(request.POST)

	if request.method=='POST':

		
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'your account has been created! now you are able to login {username}')


			return redirect('login')
		else:
			form=UserRegistrationForm()
	return render(request,'task/register.html',{'form':form})   