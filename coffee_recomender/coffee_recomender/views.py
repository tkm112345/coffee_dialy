from django.shortcuts import render
from django.shortcuts import redirect
from .models import Entry,Coffee,Query
from .forms import InputForm,RegistrationForm,AccessForm,QueryForm
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.


#####index.htmlのページ用#####
def index(request):
    params = {
        'queryform':QueryForm(),
        'form':InputForm(),
    }
    return render(request,'coffee_recomender/index.html',params)

def post(request):
    if (request.method == 'POST'):
    #    return redirect(to="/index")
        entry_date = request.POST['entry_date']
        make = request.POST['make']
        coffee = request.POST['coffee']
        evaluation = request.POST['evaluation']
        entry = Entry(entry_date=entry_date,make=make, \
            coffee=coffee,evaluation=evaluation)
        entry.save()
        messages.success(request,'正常な登録処理')
        return redirect(to='/index')

    
#####registration.htmlのページ用#####
def registration(request,num=1):
    # data = Coffee.objects.all().values(
    #     'name','company','smell','acidity','taste','bitter','flavor'
    # )
    data = Coffee.objects.all()
    page = Paginator(data,5)
    params = {
        'queryform':QueryForm(),
        'form':RegistrationForm(),
        'data':page.get_page(num),
    }
    return render(request,'coffee_recomender/registration.html',params)

def post_registration(request):
    if (request.method == 'POST'):
    #    return redirect(to="/index")
        name = request.POST['name']
        company = request.POST['company']
        smell = request.POST['smell']
        acidity = request.POST['acidity']
        taste = request.POST['taste']
        bitter = request.POST['bitter']
        flavor = request.POST['flavor']
        coffee = Coffee(name=name,company=company, \
            smell=smell,acidity=acidity, \
            taste=taste,bitter=bitter, \
            flavor=flavor)
        coffee.save()
        messages.success(request,'正常な登録処理')
        return redirect(to='/registration')


#####edit/num.htmlのページ用#####
def edit(request,num):
    obj=Coffee.objects.get(id=num)
    if request.method == 'POST':
        coffee = AccessForm(request.POST,instance=obj)
        coffee.save()
        messages.success(request,'正常な変更処理')
        return redirect(to='/registration/1')
        #return redirect(to=('/edit/' + str(num)))
    params = {
        'id':num,
        'form':AccessForm(instance=obj),
    }
    return render(request, 'coffee_recomender/edit.html',params)


#####delete/num.htmlのページ用#####
def delete(request,num):
    obj=Coffee.objects.get(id=num)
    if(request.method == "POST"):
        obj.delete()
        messages.success(request,'正常な削除処理')
        return redirect(to='/registration/1')
    params = {
        'id':num,
        'obj':obj,
    }
    return render(request,'coffee_recomender/delete.html',params)
    
#####index,registrationのページ用(共通)#####
def query(request):
    if (request.method == 'POST'):
        mail = request.POST['mail']
        query = request.POST['query']
        query_obj = Query(mail=mail,query=query)
        query_obj.save()
        messages.success(request,'正常な登録処理')
        return redirect(request.META['HTTP_REFERER'])