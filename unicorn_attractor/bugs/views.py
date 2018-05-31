from django.shortcuts import render, get_object_or_404
from .models import Subject, Bug, Post, Vote
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from .forms import BugForm, PostForm
from django.forms import formset_factory 

def forum(request):
   return render(request, 'forum/forum.html', {'subjects': Subject.objects.all()})

def bugs(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'forum/bugs.html', {'subject': subject})
 
@login_required
def new_bug(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    #poll_subject_formset_class = formset_factory(PollSubjectForm, extra=1)

    if request.method == "POST":
        bug_form = BugForm(request.POST)
        post_form = PostForm(request.POST)
        #poll_form = PollForm(request.POST)
        #poll_subject_formset = poll_subject_formset_class(request.POST)

        #is_a_poll = request.POST.get('is_a_poll')
        bug_valid = bug_form.is_valid() and post_form.is_valid()
        #poll_valid = poll_form.is_valid() and poll_subject_formset.is_valid()

        bug = save_bug(bug_form, post_form, subject, request.user)
        messages.success(request, "You have created a new bug!")
        return redirect(reverse('bug', args=[bug.pk]))

    else:
        bug_form = BugForm()
        post_form = PostForm()
        #poll_form = PollForm()
        #poll_subject_formset = poll_subject_formset_class()

    args = {
        'bug_form': bug_form,
        'post_form': post_form,
        'subject': subject
    }

    args.update(csrf(request))

    return render(request, 'forum/bug_form.html', args)
def bug(request, bug_id):
    bug_ = get_object_or_404(Bug, pk=bug_id)
    args = {'bug': bug_}
    args.update(csrf(request))
    return render(request, 'forum/bug.html', args)

def save_bug(bug_form, post_form, subject, user):
    bug = bug_form.save(commit=False)
    bug.subject = subject
    bug.user = user
    bug.save()

    post = post_form.save(commit=False)
    post.user = user
    post.bug = bug
    post.save()
    return bug

'''
def save_poll(poll_form, poll_subject_formset, bug):
    poll = poll_form.save(commit=False)
    poll.bug = bug
    poll.save()

    for subject_form in poll_subject_formset:
        subject = subject_form.save(commit=False)
        subject.poll = poll
        subject.save()
'''

@login_required
def new_post(request, bug_id):
    bug = get_object_or_404(Bug, pk=bug_id)
 
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(False)
            post.bug = bug
            post.user = request.user
            post.save()
 
            messages.success(request, "Your post has been added to the bug!")
 
            return redirect(reverse('bug', args={bug.pk}))
    else:
        form = PostForm()
 
    args = {
        'form' : form,
        'form_action': reverse('new_post', args={bug.id}),
        'button_text': 'Update Post'
    }
    args.update(csrf(request))
 
    return render(request, 'forum/post_form.html', args)

@login_required
def edit_post(request, bug_id, post_id):
   bug = get_object_or_404(Bug, pk=bug_id)
   post = get_object_or_404(Post, pk=post_id)
 
   if request.method == "POST":
       form = PostForm(request.POST, instance=post)
       if form.is_valid():
           form.save()
           messages.success(request, "You have updated your bug!")
 
           return redirect(reverse('bug', args={bug.pk}))
   else:
       form = PostForm(instance=post)
 
 
   args = {
       'form' : form,
       'form_action': reverse('edit_post',  kwargs={"bug_id" : bug.id, "post_id": post.id}),
       'button_text': 'Update Post'
   }
   args.update(csrf(request))
 
   return render(request, 'forum/post_form.html', args)


@login_required
def delete_post(request, bug_id, post_id):
   post = get_object_or_404(Post, pk=post_id)
   bug_id = post.bug.id
   post.delete()
 
   messages.success(request, "Your post was deleted!")
 
   return redirect(reverse('bug', args={bug_id}))

@login_required
def bug_vote(request, bug_id, subject_id):
    bug = Bug.objects.get(id=bug_id)
    
    
    vote = bug.votes.filter(user=request.user) 
    if vote:
      messages.error(request, "You already voted on this! ... You’re not trying to cheat are you?")
      return redirect(reverse('bug', args={bug_id}))
    else:
      bug.bug_votes += 1
      bug.save()
      Vote.objects.create(bug=bug, user=request.user)  
      return redirect(reverse('bug', args={bug_id}))

'''
    
   subject = bug.poll.votes.filter(user=request.user)
 
   if subject:
       messages.error(request, "You already voted on this! ... You’re not trying to cheat are you?")
       return redirect(reverse('bug', args={bug_id}))
 
   subject = PollSubject.objects.get(id=subject_id)
 
   subject.votes.create(poll=subject.poll, user=request.user)
 
   messages.success(request, "We've registered your vote!")
 
   return redirect(reverse('bug', args={bug_id}))
'''