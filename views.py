from django.shortcuts import render
from django.http import HttpResponse
from .models import feedback_Data
from .forms import feedbackform
from .models import Services_Data
from .models import Enquiry_Data
from .forms import EnquiryForm

import datetime
def feedback_view(request):
    if request.method=="POST":
        fform = feedbackform(request.POST)
        if fform.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')

            data = feedback_Data(
                name=name,
                rating=rating,
                date=date1
            )

            data.save()
            fform = feedbackform()
            feedbacks=feedback_Data.objects.all()
            return render(request, 'samsoft_feedback.html',{'fform':fform, 'feedbacks':feedbacks})
        else:
            return HttpResponse("User Invalid Data")
    else:
        feedbacks= feedback_Data.objects.all()
        fform=feedbackform()
        return render(request, 'samsoft_feedback.html',{'fform':fform, 'feedbacks':feedbacks})



def services_view(request):
    services = Services_Data.objects.all()
    return render(request, 'samsoft_services.html',{'services':services})

def home_view(request):
    return render(request, 'samsoft_home.html')


def enquiry_view(request):
    if request.method=="POST":
        eform = EnquiryForm(request.POST)
        if eform.is_valid():
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            gender = request.POST.get('gender')
            courses = eform.cleaned_data.get('courses')
            shifts = eform.cleaned_data.get('shifts')
            start_date = eform.cleaned_data.get('start_date')

            data = Enquiry_Data(
                name=name,
                mobile=mobile,
                email=email,
                gender=gender,
                courses=courses,
                shifts=shifts,
                start_date=start_date
            )
            data.save()
            eform=EnquiryForm()
            return render(request, 'samsoft_enquiry.html',{'eform':eform})
        else:
            return HttpResponse("Invalid Data")
    else:
        eform = EnquiryForm()
        return render(request, 'samsoft_enquiry.html', {'eform': eform})


def gallary_view(request):
    return render(request, 'samsoft_gallary.html')



