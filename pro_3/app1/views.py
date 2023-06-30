from django.shortcuts import redirect, render
from app1.models import regist

# Create your views here.
def home(request):
    mydata=regist.objects.all()
    if mydata!='':
        return render(request,'home.html',{'data':mydata})
    else:
        return render(request,'home.html')

def addData(request):
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']

        obj=regist()
        obj.name=name
        obj.address=address
        obj.contact=contact
        obj.mail=mail
        obj.save()
        mydata=regist.objects.all()
        return redirect('home')
        # return render(request,'home.html',{'data':mydata})
    return render(request,'home.html')

def updateData(request,id):
    mydata=regist.objects.get(id=id)
    
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']

        mydata.name=name
        mydata.address=address
        mydata.contact=contact
        mydata.mail=mail

        mydata.save()

        return redirect('home')

    return render(request,'update.html',{'data':mydata})


def deleteData(request,id):
    mydata=regist.objects.get(id=id)  #object(9)
    mydata.delete()
    return redirect('home')







# def display_home(request):
#     my_data=datas.objects.all()
#     if (my_data!=''):
#         return render(request,'home.html',{'datas':my_data})
#     else:
#         return render(request,'home.html')
        

# def add_data(request):
#     if request.method=='POST':
#         name=request.POST['name']
#         # age=request.POST['age']
#         address=request.POST['address']
#         contact=request.POST['contact']
#         mail=request.POST['mail']

#         obj=datas()
#         obj.name=name
#         obj.address=address
#         obj.contact=contact 
#         obj.mail=mail
#         obj.save()
#         my_data=datas.objects.all()
#         return render(request,'home.html',{'datas':my_data})
#     return render(request,'home.html')
# # def view_(request):
# #     display=datas.objects.all()
# #     return render(request,'view.html',{'show':display})

# def update(request,id):
#     mydata=datas.objects.get(id=id)
#     if request.method=='POST':
#         name=request.POST['name']
#         # age=request.POST['age']
#         address=request.POST['address']
#         contact=request.POST['contact']
#         mail=request.POST['mail']

#         mydata.name=name
#         mydata.address=address
#         mydata.contact=contact
#         mydata.mail=mail

#         mydata.save()

#         return redirect('home')


#     return render(request,'update.html',{'datas':mydata})