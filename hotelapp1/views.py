from django.shortcuts import render,redirect
from .models import guesttable
from .forms import GuestForm
from .models import staffprofile
from .forms import StaffForm
from .forms import RoomForm
from .models import roomtable
from .forms import BookingForm
from .models import bookingtable
from datetime import datetime
from django.contrib.auth import authenticate, login as log,logout
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from .models import feedback
from .forms import FeedbackForm
# Create your views here.
def home(request):
    return render(request,"home.html")

def loginop(request):
    return render(request,"loginop.html")

def signupop(request):
    return render(request,"signupop.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    form = FeedbackForm(request.POST)
    if request.method == 'POST':
        form = FeedbackForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            # Save feedback to database
            feedback_instance = form.save()
        send_mail(
                "Subject here",
                "Here is the message.",
                "adithya54756@gmail.com",
                ["adithya54756@gmail.com"],
                fail_silently=False,
                )
            # Send email
            # subject = 'New Feedback Submitted'
            # message = f'Topic: {topic}\nEmail: {email}'
            # from_email = 'adithya54756@gmail.com'  # Update with your email address
            # recipient_list = ['adith54756@gmail.com']  # Update with the admin's email address
            # send_mail(subject, message, from_email, recipient_list)
        return redirect('contact')  # Redirect to a th
    return render(request,"contact.html",{'form':form})
#####################################################################################################################################################
# def guestsignup(request):
#     form = GuestForm(request.POST)
#     if request.method == 'POST':
        
#         if form.is_valid():
#             form.save()
#             return redirect('guestlogin')
#         else:
#             ermsg = "Password must be greater than 6 letters and passwords must be same."
#             return render(request, 'signup.html', {'form': form,'ermsg':ermsg})
#     else:
#         return render(request, 'guestsignup.html', {'form': form})

def guestsignup(request):
    form = GuestForm()
    if request.method == "POST":
        form = GuestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('guestlogin')
    return render(request,"guestsignup.html",{'form':form})
    
def guestlogin(request):
    return render(request,"guestlogin.html")

def guestloginfunc(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        cr = guesttable.objects.filter(username=username,password=password)
        if cr:
            user_details = guesttable.objects.get(username=username,password=password) 
            id = user_details.id
            username = user_details.username
            email = user_details.email
            
            request.session['id']= id 
            request.session['username']=username
            request.session['email']=email
            return redirect("guestprofile") 
        else:
            cb = 'invalid login'
            return render(request,"guestlogin.html",{'cb':cb})
    else:
        return render(request,"guestlogin.html")

def guestprofile(request):
    id=request.session['id']
    username=request.session['username']
    profile=guesttable.objects.get(pk=id)
    return render(request,"guestprofile.html",{'username':username,'profile':profile,'id':id})

def guestupdate(request,pk):
    gu=guesttable.objects.get(id=pk)
    form = GuestForm(instance = gu)
    if request.method=="POST":
        form = GuestForm(request.POST,instance=gu)
        if form.is_valid:
            form.save()
            return redirect("guestprofile") 
    return render(request,"guestupdate.html",{'form':form})

def deleteguest(request,pk):
    dg=guesttable.objects.get(id=pk)
    dg.delete()
    return redirect("guestlogin")

def guestlogout(request):
    logout(request) 
    return redirect("guestlogin")
    
    
###################################################################################################################################################
def staffsignup(request):
    form = StaffForm()
    if request.method == "POST":
        form = StaffForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stafflogin')
    return render(request,"staffsignup.html",{'form':form})

def stafflogin(request):
    return render(request,"stafflogin.html")


def staffloginfunc(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        cr = staffprofile.objects.filter(username=username,password=password,approval=True)
        if cr:
            user_details = staffprofile.objects.get(username=username,password=password) 
            id = user_details.id
            username = user_details.username
            email = user_details.email
            
            request.session['id']= id 
            request.session['username']=username
            request.session['email']=email
            return redirect("staffprofiles") 
        else:
            cb = 'invalid login or request not approved'
            return render(request,"stafflogin.html",{'cb':cb})
    else:
        return render(request,"stafflogin.html")

def staffprofiles(request):
    id=request.session['id']
    username=request.session['username']
    profile=guesttable.objects.get(pk=id)
    return render(request,"staffprofiles.html",{'id':id,'profile':profile,'username':username})

def staffupdate(request,pk):
    gu=staffprofile.objects.get(id=pk)
    form = StaffForm(instance = gu)
    if request.method=="POST":
        form = StaffForm(request.POST,instance=gu)
        if form.is_valid:
            form.save()
            return redirect("staffviewforupdate") 
    return render(request,"staffupdate.html",{'form':form})

def deletestaff(request,pk):
    dg=staffprofile.objects.get(id=pk)
    dg.delete()
    return redirect("stafflogin")

def stafflogout(request):
    logout(request) 
    return redirect("stafflogin")

def staffviewforupdate(request):
    br = roomtable.objects.all()
    return render(request,"staffupdateview.html",{'br':br})
#################################################################################################

def addroom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staffprofiles')
    return render(request,"addrooms.html",{'form':form})

def roomupdate(request,pk):
    ru=roomtable.objects.get(id=pk)
    form = RoomForm(instance = ru)
    if request.method=="POST":
        form = RoomForm(request.POST,instance=ru)
        if form.is_valid:
            form.save()
            return redirect("staffprofiles")
    return render(request,"updateroom.html",{'form':form})

def checkbooking(request):
    br=bookingtable.objects.all()
    return render(request,"checkbookings.html",{'br':br})

##############################################################################################################

def bookrooms(request):
    br=roomtable.objects.all()
    return render(request,"bookrooms.html",{'br':br})
    
def bookingroom(request):
    if request.method == 'POST':
        guest_id = request.POST.get('guest_id')
        room_id = request.POST.get('room_id')
        check_in_date = datetime.strptime(request.POST.get('check_in_date'), '%Y-%m-%d').date()
        check_out_date = datetime.strptime(request.POST.get('check_out_date'), '%Y-%m-%d').date()
        guest = guesttable.objects.get(id=guest_id)
        room = roomtable.objects.get(id=room_id)
        booking = bookingtable.objects.create(guest=guest, room=room, checkindate=check_in_date, checkoutdate=check_out_date)

        room.availability = False
        room.save()
        return redirect('bookrooms')
    else:
        guests = guesttable.objects.all()
        rooms = roomtable.objects.filter(availability=True)
        return render(request, 'bookingroom.html', {'guests': guests, 'rooms': rooms})
    
##################################################################################################################################
def approveroom(request,pk):
    ru=bookingtable.objects.get(id=pk)
    form = BookingForm(instance = ru)
    if request.method=="POST":
        form = BookingForm(request.POST,instance=ru)
        if form.is_valid:
            form.save()
            return redirect("checkbooking")
    return render(request,"approveroom.html",{'form':form})

def guestbookingstatus(request):
    br=bookingtable.objects.all()
    return render(request,"guestbookingstatus.html",{'br':br})