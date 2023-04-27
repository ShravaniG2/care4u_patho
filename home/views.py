from curses import OK
import json
from json import JSONDecoder
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, auth
from math import ceil
from django.utils import timezone
from datetime import timedelta
from datetime import date, timedelta


from .models import test,package,adminmodel,Patient_List,Payment
from .models import User,feedback,Booking,doctor,appointment




"""def test_page(request):
    return render(request,'test_page.html')"""   

def testpage(request,id):
    tests=test.objects.filter(test_id=id)
    return render(request,'test_page.html',{'disptest':tests})

def packagepage(request,id):
    packages=package.objects.filter(package_id=id)
    return render(request,'package_page.html',{'disppackage':packages})

def profile(request): 
    return render(request,'profile.html')

"""def homepage(request):
    return render(request,'homepage.html') http://127.0.0.1:8000/login"""

"""def plejwork(request):
    return render(request,'profile.html')"""



def register(request):

    if request.method=="POST":
        FirstName=request.POST['FirstName']
        LastName=request.POST.get('LastName')
        email=request.POST.get('email')
        phone= request.POST.get('phone')
        username= request.POST.get('username')
        password= request.POST.get('password')
        repassword= request.POST.get('repassword')


        #regis=registermodel(first_name=FirstName,last_name=LastName,gender=gender,dob=dob,email=email,phone=phone,username=username,password=password)
        #regis.save()

        if password==repassword:
            if FirstName.isalpha() and LastName.isalpha():
                if User.objects.filter(username=email).exists():
                    messages.error(request, "Email already registered",extra_tags='error')
                    return render(request,'register.html')
                else:
                    user= User.objects.create_user(first_name=FirstName,last_name=LastName,username=email,password=password)
                    user.save()

                    #send_mail( FirstName +' '+ LastName +', here is your confirmation mail for registering at All Good Pathology', #subject
                    #'Thank you, for chooisng All Good Pathology. We assure that your experience with us would be wonderful. All Good Pathology is the most trusted and well known pathology in your area.\n\nYou can use the username and password entered at the time of registration to log in into your account. We have wide range of tests and packages to satisfy your need.\n\n We hope you will get well soon. \n\n\n Our best wishes,\n All Good Pathology.',
                    #'allgood.pathology@gmail.com', [email], )

            else:
                messages.error(request, "First name & Last name should be in letters",extra_tags='error')
                return render(request,'register.html')

            messages.success(request, "Your registration is now complete",extra_tags='success')
            return render(request,'register.html')
        else:
            messages.error(request, "Passwords not matched",extra_tags='error')
            return render(request,'register.html')

    return render(request,'register.html')


def login_p(request):

    if request.method=="POST":
        login_email=request.POST.get('login_email')
        login_password=request.POST.get('login_password')

        user = auth.authenticate(username=login_email,password=login_password)

        if user is not None:
            auth.login(request, user)
            #messages.success(request, "YSuccessflly logged in !!!",extra_tags='success')
            #return render(request,'login.html')
            return redirect('http://127.0.0.1:8000/')


        else:
            messages.error(request,"Wrong email or password entered",extra_tags='error')
            return render(request,'login.html')

    return render(request,'login.html')


@login_required
def logout_p(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000/')


def firstpage(request):
    
    tests=test.objects.all()
    print(tests)
    n=len(tests)
    nslides=n//4 + ceil((n/4)-(n//4))
    test_d={'noof_slides':nslides,'range':range(1,nslides),'mytest':tests}

    packages=package.objects.all()
    print(packages)
    n=len(packages)
    nslides2=n//4 + ceil((n/4)-(n//4))
    package_d={'noof_slides':nslides2,'range':range(1,nslides2),'mypackage':packages}

    list_d={**test_d,**package_d}

    if request.method=="POST":
        tests=test.objects.all()
        packages=package.objects.all()

        testcha=request.POST.get('testcha_nav')
        packagecha_nav=request.POST.get('packagecha_nav')
        cart=request.session.get('cart')

        #test_id=test.objects.get(id=test_id)

        """if cart:
            quantity=cart.get(testcha)
            if quantity:
                cart[testcha]= quantity+ 1
            else:
                cart[testcha]= 1

        else:
            cart={}
            cart[testcha]=1"""

        request.session['cart']= cart
        print(testcha)
        return render(request,'homepage.html',list_d)

    return render(request,'homepage.html',list_d)


def register_a(request):
    if request.method=="POST":
        first_n=request.POST.get('first_n')
        last_n=request.POST.get('last_n')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        phone= request.POST.get('phone')
        id= request.POST.get('id')
        password= request.POST.get('password')
        repassword= request.POST.get('repassword')


        if password==repassword:
            if first_n.isalpha() and last_n.isalpha():
                if adminmodel.objects.filter(id=id).exists():
                    messages.error(request, "ID already registered",extra_tags='error')
                    return render(request,'register_a.html')
                else:
                    regis=adminmodel(first_n=first_n,last_n=last_n,gender=gender,dob=dob,email=email,phone=phone,id=id,password=password)
                    regis.save() 

            else:
                messages.error(request, "First name & Last name should be in letters",extra_tags='error')
                return render(request,'register_a.html')

            messages.success(request, "Your registration is now complete",extra_tags='success')
            return render(request,'register_a.html')
        else:
            messages.error(request, "Passwords not matched",extra_tags='error')
            return render(request,'register_a.html')                  
       
    return render(request,'register_a.html')


def login_a(request):
    if request.method=="POST":
        id=request.POST.get('id')
        password=request.POST.get('password')

        user = auth.authenticate(id=id,password=password)

        if user is not None:
            login(request, user)
            return render(request,'homepage.html')
        else:
            messages.error(request,"Wrong phone number or password entered",extra_tags='error')
            return render(request,'login_a.html')
    else:
        return render(request,'login_a.html')
    

def forgertpassword(request):
    return render(request, 'forgetpassword.html')


@login_required
def edit_profile(request):
    user = request.user
    profile = User.objects.get(username=user)

    if request.method == 'POST':
        first_name = request.POST['FirstName']
        #email = request.POST['email']
        last_name = request.POST['LastName']

        profile.first_name = first_name
        #profile.email = email
        profile.last_name = last_name


        if first_name.isalpha() and last_name.isalpha():
            profile.save()
            #messages.success(request, 'Your profile was successfully updated!',extra_tags='success')
            return redirect('userprofile')
        else:
            messages.error(request, "First name & Last name should be in letters",extra_tags='error')
            return render(request,'edit_profile.html')
       

    context = {
        'profile': profile,
    }
    return render(request,'edit_profile.html',context)


def about(request):
    return render(request,'about.html')


@login_required
def userprofile(request):
    user = request.user

    relative=Patient_List.objects.filter(username=user)
    userdetails={'user':user}
    relativedetails={'relative':relative}
    content={
        **userdetails,
        **relativedetails
    }
    return render(request,'profile.html',content)

def cart(request):
    options=Patient_List.objects.filter(username=request.user)
    doctors=doctor.objects.all()

    if request.method == 'POST':

        selected_date = request.POST.get('selected_date')
        selected_time = request.POST.get('selected_time')
        address = request.POST.get('address')
        d_name = request.POST.get('d_name')
        d_email = request.POST.get('d_email')

        selected_patient = request.POST.getlist('options')
        selected_doctor = request.POST.getlist('doctors')
        items = request.POST.getlist('cart_data')
        items1 = json.dumps(items)
        items2 = json.loads(items1)



        user = request.user
        cart = Booking(username=user,sch_date=selected_date,sch_time=selected_time, address=address,items=items2,d_name=d_name,d_email=d_email)

        
        cart.save()
        cart.listof_patient.set(selected_patient)
        cart.doctors.set(selected_doctor)
        cart.save()
        
        return redirect('payment_p')
        

    dates = [date.today() + timedelta(days=i) for i in range(7)]
    schedule_dates={'dates': dates}
    patient={'options':options}
    doctorbro={'doctors':doctors}
    list={**schedule_dates,**patient,**doctorbro}

    return render(request,'cart.html',list)


@login_required
def feedback_u(request):
    if not request.user.is_authenticated:
        message = "Please log in to access this page"
        return render(request, 'login_required.html', {'message': message})
    else:
        if request.method=="POST":
            userchanav = request.user
            form = feedback(username=userchanav)

            form.experience=request.POST.get('experience')
            form.improvement=request.POST.get('improvement')
            form.rate=request.POST.get('rate')            
            
            form.save()
            messages.success(request, "Thank you for submitting your suggestings",extra_tags='success')
            return render(request,'feedback.html')

        return render(request,'feedback.html')

@login_required
def relatives(request):
    
    if request.method=="POST":
        userchanav = request.user
        form = Patient_List(username=userchanav)


        form.p_name=request.POST.get('p_name')
        form.p_age=request.POST.get('p_age')
             #form.p_gender=request.POST.get('gender')


       # if form.p_name.isalpha():
        if form.p_age.isnumeric():
            form.save()
            #messages.success(request, "Patient saved successfully",extra_tags='success')
            return redirect('userprofile')
        else:
            messages.error(request, "Enter age in correct format",extra_tags='error')
            return render(request,'relatives.html')
        #else:
            #messages.error(request, "Name should be in letters only",extra_tags='error')
            #return render(request,'relatives.html')     
             
        #username = User.objects.filter(userchename=username)
        #username = User.objects.get(username=user_all)

        #username_id=request.POST.get('username')
        #a=format(username_id)

        #user = request.user
        # form = Patient_List(user=user)

        #form.save()
        
        #forenkey = Patient_List(username=request.user.username)
        
        #p_list=Patient_List(p_name=p_name,p_age=p_age,p_gender=p_gender,username=username)
        #p_list.save()

        #p_list=Patient_List.objects.create(p_name=p_name,p_age=p_age,p_gender=p_gender,username_id=user)

    return render(request,'relatives.html')

@login_required
def orderhistory(request):
    user = request.user

    order_history=Booking.objects.filter(username=user).order_by('-id')

    return render(request, 'orderhistory.html',{'order_history':order_history})


@login_required
def appointment_history(request):
    user = request.user

    app_history=appointment.objects.filter(username=user).order_by('-id')
    return render(request, 'appointment_history.html',{'app_history':app_history})

@login_required
def appointment_p(request):
    
    if request.method == 'POST':
        user=request.user
        form=appointment(username=user)

        form.sch_date = request.POST.get('selected_date')
        form.sch_time = request.POST.get('selected_time')
        form.patient_name = request.POST.get('options')
        form.doc_name = request.POST.get('doctors')
        
        #user_selection = appointment(username=request.user,doc_name=selected_doctor,patient_name=selected_patient,sch_date=selected_date, sch_time=selected_time)
        #user_selection.save()

        form.save()

        messages.success(request, 'Your cart saved successfully!',extra_tags='success')
        return render(request, 'appointment.html')
    # Generate dates for the next seven days
    dates = [date.today() + timedelta(days=i) for i in range(7)]
    options=Patient_List.objects.filter(username=request.user)
    doctors=doctor.objects.all()
    return render(request, 'appointment.html',{'dates': dates,'options':options,'doctors':doctors})

@login_required
def edit_relatives(request,id):
    disprelatives=Patient_List.objects.filter(id=id)
    user = request.user
    form = Patient_List(username=user)
    

    profile = Patient_List.objects.get(id=id)

    if request.method == 'POST':  

        profile.p_name=request.POST.get('p_name')
        profile.p_age=request.POST.get('p_age')

        if profile.p_age.isnumeric():
            profile.save()
            #messages.success(request, "Patient saved successfully",extra_tags='success')
            return redirect('userprofile')
        else:
            messages.error(request, "Enter age in correct format",extra_tags='error')
            return render(request,'edit_relatives.html')        
       

    context = {'profile': profile}
    disprelatives={'disprelatives':disprelatives}

    list={**disprelatives,**context}
    
    return render(request, 'edit_relatives.html',list)


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        test1 = test.objects.filter(t_name__icontains=searched)
        package1 = package.objects.filter(package_name__icontains=searched)
        return render(request, 'search.html',{'searched':searched,'test1':test1,'package1':package1})
    else:
        return render(request,'search.html')
    
@login_required
def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Patient_List.objects.get(id=pk)
		delete_it.delete()
		return redirect('userprofile')
	else:
		return render(request,'profile.html')


@login_required
def payment_p(request):
    if request.method == 'POST':
        user=request.user
        form=Payment(username=user)
        form.payment_type = request.POST.get('payment_type')
        
        #payment = Payment(payment_type=payment_type,)
        form.save()
        
        #messages.success(request, "Payment done successfully",extra_tags='success')
        return redirect('orderhistory1')
    return render(request, 'payment_p.html')







