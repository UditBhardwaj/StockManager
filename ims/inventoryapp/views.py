from django.shortcuts import render, redirect , HttpResponseRedirect
from .models import Stock,Sales

from .forms import StockCreateForm, StockSearchForm, StockUpdateForm, ReceiveForm,IssueForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .forms import UserRegisterForm



def home(request):
    return render(request, 'inventoryapp/home.html')




# def home(request):
#     title = 'Welcome: This is the Home Page'
#     context = {
#         "title": title,
#     }
#     return render(request, "inventoryapp/home.html", context)

@login_required(login_url='login')
def list_item(request):
    form = StockSearchForm(request.POST)
    title = 'List of Items'
    queryset = Stock.objects.all()

    context = {
        "form":form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "inventoryapp/list_item.html", context)

@login_required(login_url='login')
def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('list_item')
    messages1 = "Item has been added"
    context = {
        "form": form,
        "messages":messages1,
    }
    return render(request, "inventoryapp/add_items.html", context)

@login_required(login_url='login')
def stock_detail(request, pk):
    queryset = Stock.objects.get(id=pk)
    if queryset.quantity == 0:
        queryset.delete()
        return HttpResponseRedirect('/list_item')
    context = {
		"title": queryset.item_name,
		"queryset": queryset,
	}
    return render(request, "inventoryapp/stock_detail.html", context)

@login_required(login_url='login')
def issue(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = IssueForm(request.POST)
    # form1 = IssueForm(request.POST)
    if request.method == "POST" and form.is_valid():
        x = form.cleaned_data['issue_quantity']
        if(queryset.quantity - x>=0):
            per = queryset.price
            total = per*x
            messages.success(request, f'Total price is {total}')
            queryset.quantity = queryset.quantity - x

            instance = form.save(commit=False)
            instance.total_price = total
            instance.save()
            queryset.save()


        else:
            messages.success(request, 'NOT enough quantity')



        return redirect('/stock_detail/' + str(queryset.id))
    context = {
        "queryset": queryset,
        "form": form,

    }
    return render(request, "inventoryapp/issue.html", context)




# def reorder(request, pk):
#     queryset = Stock.objects.get(id=pk)
#     form = ReorderLevelForm(request.POST or None, instance=queryset)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         messages.success(request, "Reorder level for " + str(instance.item_name) + " is updated to " + str(
#             instance.reorder_level))
#         return redirect('/list_item/')
#     context = {
#         "instance": queryset,
#         "form": form,
#     }
#     return render(request, "inventoryapp/reorder.html", context)

@login_required(login_url='login')
def sales(request):
    queryset = Sales.objects.all()

    return render(request,"inventoryapp/sales.html",{"queryset":queryset
                                                     })

@login_required(login_url='login')
def receive(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReceiveForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity += instance.receive_quantity
		instance.save()
		messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name)+"s now in Store")

		return redirect('/stock_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())
	context = {
			"title": 'Reaceive ' + str(queryset.item_name),
			"instance": queryset,
			"form": form,
			"username": 'Receive By: ' + str(request.user),
		}
	return render(request, "inventoryapp/receive.html", context)



@login_required(login_url='login')
def search_items(request):
    form = StockSearchForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        models = Stock.objects.filter(category__icontains= form.cleaned_data['category'],
                                         item_name__icontains=form.cleaned_data['item_name'])

        # context ={
        #     'count':['count'],
        #     'category':form['category'],
        #     'item_name':form['item_name'],
        #     'quantity':form['quantity'],
        # }

        return render(request, "inventoryapp/search_items.html",{'orders':models})
    return render(request, "inventoryapp/list_item.html")





def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('list_item')
    context = {
		'form':form
	}
    return render(request, 'inventoryapp/update.html', context)


def delete_bill(request, pk):
    queryset = Sales.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('/sales')
    return render(request, 'inventoryapp/delete_bill.html')

def delete_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('/list_item')
    return render(request, 'inventoryapp/delete_items.html')