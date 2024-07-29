from django.shortcuts import render, redirect
from .forms import *
from .models import GuestAttendence

def rsvp(request):
    if request.method == "POST":
        form = GuestAttendenceForm(request.POST)
        plus_one_form = GuestsPlusOneForm(request.POST)
        
        if form.is_valid():
            guest_data = form.cleaned_data
            
            # Extract and remove plus_one data from guest_data
            plus_one_data = {
                'plus_one_name': guest_data.pop('plus_one_name', None),
                'plus_one_surname': guest_data.pop('plus_one_surname', None),
                'plus_one_relation': guest_data.pop('plus_one_relation', None),
            }
            
            cell = guest_data.get('cell')
            
            # Create or get the guest attendance record
            guest, created = GuestAttendence.objects.get_or_create(cell=cell, defaults=guest_data)
            
            # Handle plus one if provided
            if plus_one_data['plus_one_name'] and plus_one_data['plus_one_surname'] and plus_one_data['plus_one_relation']:
                plus_one, plus_one_created = GuestsPlusOne.objects.get_or_create(
                    plus_one_name=plus_one_data['plus_one_name'],
                    plus_one_surname=plus_one_data['plus_one_surname'],
                    plus_one_relation=plus_one_data['plus_one_relation']
                )
                guest.plus_one = plus_one
                guest.save()

            return redirect('success')
    else:
        form = GuestAttendenceForm()
        plus_one_form = GuestsPlusOneForm()

    return render(request, 'WeddingInvitationApp/rsvp.html', {'form': form, 'plus_one_form': plus_one_form})

def success(request):
    return render(request, 'WeddingInvitationApp/success.html')

def stats (request):
    attending_church = GuestAttendence.objects.filter(church_attendence=True, home_attendence=False)
    attending_home = GuestAttendence.objects.filter(home_attendence=True, church_attendence=False)
    both_ceremonies = GuestAttendence.objects.filter(church_attendence=True, home_attendence=True)
    no_attendance = GuestAttendence.objects.filter(church_attendence=False, home_attendence=False)


    num_attending_church = attending_church.count()
    num_attending_home = attending_home.count()
    num_both_ceremonies = both_ceremonies.count()
    num_no_attendance = no_attendance.count()

    context = {
        'attending_church': attending_church,
        'attending_home': attending_home,
        'both_ceremonies': both_ceremonies,
        'no_attendance': no_attendance,
        'num_attending_church' : num_attending_church,
        'num_attending_home' : num_attending_home,
        'num_both_ceremonies' : num_both_ceremonies,
        'num_no_attendance' : num_no_attendance,
    } 

    return render(request, 'WeddingInvitationApp/stats.html', context)