from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Event, Like
from profiles.models import Profile
from .forms import EventModelForm
from django.views.generic import UpdateView, DeleteView
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def event_create_and_list_view(request):
    qs = Event.objects.all()
    profile = Profile.objects.get(user=request.user)

    # initials
    e_form = EventModelForm()
    event_added = False

    profile = Profile.objects.get(user=request.user)

    if 'submit_e_form' in request.POST:
        print(request.POST)
        e_form = EventModelForm(request.POST, request.FILES)
        if e_form.is_valid():
            instance = e_form.save(commit=False)
            instance.author = profile
            instance.save()
            p_form = EventModelForm()
            post_added = True

    context = {
        'qs': qs,
        'profile': profile,
        'e_form': e_form,
        'post_added': event_added,
    }

    return render(request, 'events/main.html', context)


@login_required
def like_unlike_event(request):
    user = request.user
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        event_obj = Event.objects.get(id=event_id)
        profile = Profile.objects.get(user=user)

        if profile in event_obj.is_liked.all():
            event_obj.is_liked.remove(profile)
        else:
            event_obj.is_liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, event_id=event_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'

            event_obj.save()
            like.save()

        # data = {
        #     'value': like.value,
        #     'likes': event_obj.liked.all().count()
        # }

        # return JsonResponse(data, safe=False)
    return redirect('events:main-event-view')
