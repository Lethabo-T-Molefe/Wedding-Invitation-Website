from django.shortcuts import render, redirect
from .forms import GuestAttendenceForm
from .models import GuestAttendence

def rsvp(request):
    if request.method == 'POST':
        form = GuestAttendenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = GuestAttendenceForm()
    return render(request, 'WeddingInvitationApp/rsvp.html', {'form': form})

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