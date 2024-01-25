from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect
from .models import Parkingspace,Login,Bookedspc
import urllib
import random
import json
from datetime import date
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect,JsonResponse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from django import template

current_Logedin_user = ""
loginstatus = 'NotLogedin'
cardclicked = ""
upbtnclicked = 0
delbtnclicked = 0
username = ''
genotp = 0
emailcheck = ''
cardpickedprice = 0
expdate = ""
adminlogin = ""
adminloginstatus = ""
cncclicked = 0
def jsonfileupdate():
    dashboardview = Parkingspace.objects.all().filter(status = "Approved")
    parkingdb = serializers.serialize("json", dashboardview)
    with open("C:\\Users\\admin\\Desktop\\ParkItDown\\mysite\\main\\static\\mysite\\dash.json", "w") as f:
        jasoned = json.loads(parkingdb)
        json.dump(jasoned, f)

def jsonfileupdatedash():
    dashboardview = Parkingspace.objects.all().filter(status = "Approved",availslots__gt = 0)
    parkingdb = serializers.serialize("json", dashboardview)
    with open("C:\\Users\\admin\\Desktop\\ParkItDown\\mysite\\main\\static\\mysite\\dash.json", "w") as f:
        jasoned = json.loads(parkingdb)
        json.dump(jasoned, f)
def dashboard(response):
    global current_Logedin_user,cardclicked,loginstatus
    context = {}
    search_city = ""
    #parkingdb = serializers.serialize("json", Parkingspace.objects.all())
    parkingdb = Parkingspace.objects.all()
    #dashboardjson = json.dumps(parkingdb)
    #print(dashboardjson)
    cardclicked = response.POST.get("dashbtn")
    #current_Logedin_user = 'Aman'
    if response.POST.get("dashbtn"):
        return redirect('/Details')
    jsonfileupdatedash()
    nameofuser = ""
    user_details = Login.objects.filter(email=str(current_Logedin_user)).first()
    if user_details != None:
        nameofuser = user_details.name
    if response.POST.get("logout"):
        current_Logedin_user = ""
        loginstatus = "NotLogedin"

        with open("C:\\Users\\admin\\Desktop\\ParkItDown\\mysite\\main\\static\\mysite\\dash.json", "w") as f:
            f.truncate()
        return HttpResponseRedirect('sign')
    return render(response, "main/dashboard.html", {'nameofuser':nameofuser,'parkingspc' : parkingdb,'search_city' : search_city,'loginstatus':loginstatus})

def addandmgspace(response):
    global upbtnclicked,current_Logedin_user,loginstatus
    uploaded_img = ''
    uploaded_doc = ''
    print(len(current_Logedin_user))
    if len(current_Logedin_user) > 1:
        dashboardview = Parkingspace.objects.filter(email=str(current_Logedin_user))
        parkingdb = serializers.serialize("json", dashboardview)
        with open("C:\\Users\\admin\\Desktop\\ParkItDown\\mysite\\main\\static\\mysite\\dash.json", "w") as f:
            jasoned = json.loads(parkingdb)
            json.dump(jasoned, f)
    else:
        with open("C:\\Users\\admin\\Desktop\\ParkItDown\\mysite\\main\\static\\mysite\\dash.json", "w") as f:
            f.truncate()
    if response.POST.get("spacesubmit"):
        addspace = Parkingspace()
        addspace.name = username
        addspace.email = current_Logedin_user
        uploaded_img = response.FILES["parkingImg"]
        fs = FileSystemStorage()
        imagetodb = fs.save(uploaded_img.name,uploaded_img)
        urlimg = fs.url(imagetodb)
        addspace.image = urllib.parse.unquote(urlimg)
        print(addspace.image)
        uploaded_doc = response.FILES["landDoc"]
        doctodb = fs.save(uploaded_doc.name, uploaded_doc)
        urldoc = fs.url(doctodb)
        addspace.document = urllib.parse.unquote(urldoc)

        addspace.type = response.POST.get('category')
        print(response.POST.get('category'))
        addspace.city = response.POST.get('spacecity')
        addspace.title = response.POST.get('spacetitle')
        addspace.price = response.POST.get('spaceprice')
        addspace.landmark = response.POST.get('spacelm')
        addspace.address = response.POST.get('spaceadd')
        addspace.slots = response.POST.get('spacenos')
        addspace.discription = response.POST.get('spacedsc')
        addspace.status = 'Pending'
        addspace.availslots = response.POST.get('spacenos')
        addspace.save()
        return HttpResponseRedirect('Lend Space')
    if response.POST.get("pudatespace"):
        getid = upbtnclicked
        print(getid)
        upadedetails = Parkingspace.objects.get(sid=int(getid))
        upadedetails.title = response.POST.get('uptitle')
        upadedetails.city = response.POST.get('upcity')
        upadedetails.address = response.POST.get('upaddress')
        upadedetails.landmark = response.POST.get('uplandmark')
        uploaded_img = response.FILES["newimg"]
        fs = FileSystemStorage()
        imagetodb = fs.save(uploaded_img.name, uploaded_img)
        urlimg = fs.url(imagetodb)
        upadedetails.image = urllib.parse.unquote(urlimg)
        upadedetails.discription = response.POST.get('updisc')
        upadedetails.price = response.POST.get('upprice')
        upadedetails.save()
        jsonfileupdate()
        return HttpResponseRedirect('Lend Space')
    if response.POST.get("delclick"):
        getid = delbtnclicked
        print(getid)
        upadedetails = Parkingspace.objects.get(sid=int(getid))
        filetodel = upadedetails.image
        doctodel = upadedetails.document
        if len(filetodel) > 0:
            filetodel = "C:\\Users\\admin\\Desktop\\ParkItDown\\mysite" +filetodel
            os.remove(filetodel)
        if len(doctodel) > 0:
            doctodel = "C:\\Users\\admin\\Desktop\\ParkItDown\\mysite" + doctodel
            os.remove(doctodel)
        upadedetails.delete()
        return HttpResponseRedirect('Lend Space')
    nameofuser = ""
    user_details = Login.objects.filter(email=str(current_Logedin_user)).first()
    if user_details != None:
        nameofuser = user_details.name

    if response.POST.get("logout"):
        current_Logedin_user = ""
        loginstatus = "NotLogedin"

        return HttpResponseRedirect('sign')
    return render(response, "main/lend_your_space.html", {'current_Logedin_user':current_Logedin_user,'nameofuser':nameofuser,'loginstatus':loginstatus})

def parking_Details(response):
    global current_Logedin_user,cardpickedprice,expdate,loginstatus
    carddetail = Parkingspace.objects.all().filter(sid = int(cardclicked)).first()
    pagedetail={
        "carddetail" : carddetail,
        'current_Logedin_user': current_Logedin_user,
        'loginstatus': loginstatus
    }
    if response.POST.get("book"):
        fromdate = response.POST.get('fromDate')
        todate = response.POST.get('toDate')
        expdate = todate
        fromdate = fromdate.split('-')
        firsty = int(fromdate[0])
        firstm = int(fromdate[1])
        firstd = int(fromdate[2])
        fromdate = date(firsty,firstm,firstd)

        todate = todate.split('-')
        todatey = int(todate[0])
        todatem = int(todate[1])
        todated = int(todate[2])
        todate = date(todatey,todatem,todated)
        print(fromdate)
        print(todate)
        noofdays = todate - fromdate
        noofdays = noofdays.days
        print(noofdays)
        cardpickedprice = noofdays * carddetail.price
        cardpickedprice = cardpickedprice
        print(cardpickedprice)
        return HttpResponseRedirect("payment")
    if response.POST.get('loginorup'):
        return HttpResponseRedirect("sign")


    if response.POST.get("logout"):
        current_Logedin_user = ""
        loginstatus = "NotLogedin"

        return HttpResponseRedirect('sign')
    return render(response, "main/parking_details.html", pagedetail)

def Payment(response):
    global current_Logedin_user,cardpickedprice,expdate
    if response.POST.get("transactionsucc"):
        txnsucc = Bookedspc()
        txnsucc.sid_id = cardclicked
        txnsucc.email = current_Logedin_user
        txnsucc.expires = expdate
        txnsucc.save()

        subcardclicked = Parkingspace.objects.get(sid = cardclicked)
        subcardclicked.availslots = subcardclicked.availslots - 1
        subcardclicked.save()
        return HttpResponseRedirect("booked")
    return render(response, "main/cardPayment.html", {'cardpickedprice':cardpickedprice})


def updateclicked(response):
    global upbtnclicked , delbtnclicked
    upbtnclicked = response.POST.get('upclicked')
    delbtnclicked = response.POST.get('delclicked')
    print(delbtnclicked)
    return render(response, "main/parking_details.html", {'current_Logedin_user':current_Logedin_user})

def cancelclicked(response):
    global cncclicked
    cncclicked = response.POST.get('cancelorder')
    return render(response, "main/your_booked_spaces.html", {'current_Logedin_user':current_Logedin_user,'nameofuser':username,'loginstatus':loginstatus})

def sign_up_in(response):
    global current_Logedin_user,loginstatus,username,adminlogin,adminloginstatus
    email_not_found = ""
    invalidcred = ""
    if response.POST.get("login"):
        email = response.POST.get('lemail')
        password = response.POST.get('lpass')
        ldbemail = Login.objects.filter(email=email).first()
        if email == "admin@gmail.com" and password == "Admin@123":
            adminloginstatus = "admin here"
            current_Logedin_user = "admin@gmail.com"
            return HttpResponseRedirect("adminlog")
        else:
            if (not(ldbemail)):
                email_not_found = "noemail"
            else:
                ldbemail = Login.objects.get(email=email)
                email_not_found = "noemail"
                if ldbemail.password == password:
                    email_not_found = ""
                    current_Logedin_user = email
                    loginstatus = 'Logedin'
                    user_details = Login.objects.filter(email=str(current_Logedin_user)).first()
                    if user_details != None:
                        username = user_details.name
                    return HttpResponseRedirect("/")
                else:
                    invalidcred = 'invalid'
                    email_not_found = ""
    if response.POST.get('signup'):
        name = response.POST.get('fullname')
        semail = response.POST.get('semail')
        spassword = response.POST.get('spass')
        sdbemail = Login.objects.filter(email=semail)
        if len(sdbemail) > 0:
            print('User Alerady Exist')
        else:
            newsign = Login()
            newsign.name = name
            newsign.email = semail
            newsign.password = spassword
            newsign.save()
    if response.POST.get("rthome"):
        return HttpResponseRedirect('')
    return render(response, "main/sign_up_in.html", { 'loginstatus':loginstatus,'invalidcred':invalidcred,'current_Logedin_user':current_Logedin_user,'email_not_found':email_not_found})

def adminlog(response):
    global adminloginstatus
    dashboardview = Parkingspace.objects.all().filter(status="Pending")
    parkingdb = serializers.serialize("json", dashboardview)
    with open("C:\\Users\\admin\\Desktop\\ParkItDown\\mysite\\main\\static\\mysite\\dash.json", "w") as f:
        jasoned = json.loads(parkingdb)
        json.dump(jasoned, f)
    if response.POST.get('spaceapprove'):
        aprovespc = Parkingspace.objects.get(sid=int(response.POST.get('spaceapprove')))
        aprovespc.status = "Approved"
        aprovespc.save()
        return HttpResponseRedirect('adminlog')
    if response.POST.get('spacereject'):
        rejectspc = Parkingspace.objects.get(sid=int(response.POST.get('spacereject')))
        rejectspc.status = "Rejected"
        rejectspc.save()
        return HttpResponseRedirect('adminlog')
    if response.POST.get('adminlogout'):
        current_Logedin_user = ""
        adminloginstatus = ""
        print(response.POST.get('adminlogout'))
        return HttpResponseRedirect('/')
    return render(response,"main/admin_ui.html",{"adminloginstatus": adminloginstatus})

def booked_slots(response):
    global username,current_Logedin_user,loginstatus,cncclicked
    sidlist = []
    booked_spaces = Bookedspc.objects.filter(email=str(current_Logedin_user)).values('sid')
    for book in booked_spaces:
        sidlist.append(book['sid'])
    queryset = Bookedspc.objects.all().filter(email=str(current_Logedin_user)).values('bid','sid__sid','sid__title','sid__name','sid__landmark','sid__city','sid__type','sid__image','sid__price','expires')
    #parkingdb = serializers.serialize("json",queryset)

    with open("C:\\Users\\admin\\Desktop\\ParkItDown\\mysite\\main\\static\\mysite\\dash.json", "w") as f:
        #jasoned = json.loads(parkingdb)
        json.dump(list(queryset),f, cls=DjangoJSONEncoder)

    if response.POST.get("logout"):
        current_Logedin_user = ""
        loginstatus = "NotLogedin"
        with open("C:\\Users\\admin\\Desktop\\ParkItDown\\mysite\\main\\static\\mysite\\dash.json", "w") as f:
            f.truncate()
        return HttpResponseRedirect('sign')

    if response.POST.get("safuu"):
        cancelorder = Bookedspc.objects.all().filter(bid = int(cncclicked)).first()
        subcardclicked = Parkingspace.objects.get(sid=cancelorder.sid_id)
        subcardclicked.availslots = subcardclicked.availslots + 1
        subcardclicked.save()
        cancelorder.delete()
        return HttpResponseRedirect('booked')

    chkdateinooked =Bookedspc.objects.all()
    for chk in chkdateinooked:
        if chk.expires == date.today():
            if len(chk.mail) == 0:
                sendmailexp(chk.expires,chk.email,chk.sid_id,chk.bid)
            else:
                pass
    return render(response,"main/your_booked_spaces.html",{'nameofuser':username,'loginstatus':loginstatus})
def sendmailexp(date,email,sid,bid):
    global loginstatus
    if loginstatus == 'Logedin':
        emailcheck = email
        emailentdt = Login.objects.get(email=emailcheck)
        titleofspc = Parkingspace.objects.get(sid=sid)
        title = titleofspc.title
        location = titleofspc.landmark
        to = emailcheck
        mailfrom = 'parkitdown@gmail.com'
        your_pass = "Aman@123"
        body = """
                        Hi,{}
        
                        Your parking space at {} of {} has been expired on {}
                        If the above detail is incorrect please contact the vendor.
            
                                                         Thank You For Using Our Site
                                                                    -Admin
                    """.format(emailentdt.name, location, title, date)
        subject = 'Alert for expired parking space'
        message = MIMEMultipart()
        message['From'] = mailfrom
        message['To'] = to
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        text = message.as_string()

        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(mailfrom, your_pass)
        mail.sendmail(mailfrom, to, text)
        mail.close()
        mailsent = Bookedspc.objects.get(bid = bid)
        mailsent.mail = "sent"
        mailsent.save()
def forgetPass(response):
    global genotp,emailcheck
    emailstatus = 'NotEntered'
    otpcheck = 'wait'
    passset = 'wait'

    if response.POST.get('emailent'):
        emailcheck = response.POST.get('emailret')
        emailentdt = Login.objects.get(email=emailcheck)
        genotp = random.randint(1111, 9999)
        emailstatus = 'wait'
        otpcheck = 'NotValid'
        to = emailcheck
        mailfrom = 'parkitdown@gmail.com'
        your_pass = "Aman@123"
        body = """
                Hi,{}
                
                Your OTP to reset the password is :{}
                Please don't share your OTP with anyone
                                        
                                        Thank You For Using Our Site
                                                 -Admin
            """.format(emailentdt.name,genotp)
        subject = 'Password Reset OTP'
        message = MIMEMultipart()
        message['From'] = mailfrom
        message['To'] = to
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        text = message.as_string()

        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(mailfrom, your_pass)
        mail.sendmail(mailfrom, to, text)
        mail.close()

    if response.POST.get('otpent'):
        otpcheck = response.POST.get('otpret')
        print(otpcheck)
        print(genotp)
        if int(otpcheck) == genotp:
            otpcheck = 'wait'
            emailstatus = 'wait'
            passset = 'otpValid'
    if response.POST.get('passclicked'):
        newpassset = response.POST.get('newpass')
        connewpassset = response.POST.get('connewpass')

        if newpassset == connewpassset:
            newpassword = Login.objects.all().filter(email=emailcheck).first()
            newpassword.password = newpassset
            newpassword.save()
            return HttpResponseRedirect('sign')
    return render(response,'main/forgotpassword.html',{'emailstatus':emailstatus,'otpcheck':otpcheck,'passset':passset})