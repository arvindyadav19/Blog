from django.shortcuts import render,HttpResponse,redirect
from blogapp.models import Blog
import datetime

# Create your views here.

'''
syntax:

def functionname(request):

     return response object

To give response there are two functions 
1) HttpResponse()
2) render() 

'''

def Homepage(request):

    return HttpResponse("Hello From Home Page")


def Contactpage(request):

    return HttpResponse("Hello From contact page")

def edit(request,rid):

    # print("ID to be edited:",rid)

    # return HttpResponse("ID to be edited:"+rid)
    if request.method == "GET":
        b = Blog.objects.filter(id=rid)
        context = {}
        context['blog']=b  
        return render(request,'editblog.html',context)

    else:
        utitle = request.POST['title']
        udetail= request.POST['detail']
        ucat = request.POST['cat']
    
        # print("Updated title:",utitle)
        # print("Updated detail:",udetail)
        # print("Update cateogary:",ucat)

        b = Blog.objects.filter(id=rid)
        b.update(title=utitle,detail=udetail,cat=ucat)

    
        return redirect('/userdashboard')



def delete(request,rid):

    # print("ID to be deleted",rid)

    b = Blog.objects.filter(id=rid)

    b.delete()


    # print(b)

    # return HttpResponse("ID to be deleted:"+rid)
    # return HttpResponse("Object to be deleted fetched")
    return redirect('/userdashboard')

'''
def Homepage(request,x,y):

    print("value of x:",x)
    print("value of y:",y)


    return HttpResponse("Value Of x and y:"+x+" " +y)


'''


def helloview(request):

    context={}
    context['uname']="itvedant"
    context['x']=1000
    context['y']=200
    context['l']=[10,20,'Itvedant',90.8]
    return render(request,'hello.html',context)


#Blog application view function starts

def Homepage(request):

    return render(request,'home.html')

def user_dashboard(request):

    b = Blog.objects.all() #select * from blogapp_blog;
    # print(b)

    # for x in b:
    #     print(x)
    #     print("ID:",x.id)
    #     print("Title:",x.title)
    #     print("detail:",x.detail)
    #     print("Cat:",x.cat)
    #     print("Created At:",x.created_at)
    #     print()

    context = {}
    context['blogs'] = b

    return render(request,'dashboard.html',context)

def create_blog(request):

    print("Method Type:" , request.method)

    if request.method == "GET":
        print("In get section")
        return render(request,'create_blog.html')

    else:
        #print("In POST Section")
        btitle = request.POST["title"]
        bdet   = request.POST["detail"]
        bcat   = request.POST["cat"]

        print("Title:",btitle)
        print("Details:",bdet)
        print("Cateogary:",bcat)

        b = Blog.objects.create(title=btitle,detail=bdet,cat=bcat,created_at=datetime.datetime.now())

        b.save()


        # return HttpResponse("Data Inserted Succesfully")
        return redirect('/userdashboard')

def view_details(eq)

