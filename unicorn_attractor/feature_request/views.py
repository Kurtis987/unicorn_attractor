from django.shortcuts import render, get_object_or_404
from .models import Subject, FeatureRequest, FRPost, FRVote
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from .forms import FeatureRequestForm, PostForm
from django.forms import formset_factory 

def forum(request):
   return render(request, 'forum/feature_request_forum.html', {'subjects': Subject.objects.all()})

def feature_requests(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'forum/feature_requests.html', {'subject': subject})
 
@login_required
def new_feature_request(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id) 

    if request.method == "POST":
        feature_request_form = FeatureRequestForm(request.POST)
        post_form = PostForm(request.POST) 
 
        feature_request_valid = feature_request_form.is_valid() and post_form.is_valid() 
        if feature_request_valid: 
        	feature_request = save_feature_request(feature_request_form, post_form, subject, request.user)
        	messages.success(request, "You have created a new feature request!")
        	return redirect(reverse('feature_request', args=[feature_request.pk]))

    else:
        feature_request_form = FeatureRequestForm()
        post_form = PostForm() 

    args = {
        'feature_request_form': feature_request_form,
        'post_form': post_form,
        'subject': subject
    }

    args.update(csrf(request))

    return render(request, 'forum/feature_request_form.html', args)

def feature_request(request, feature_request_id):
    feature_request_ = get_object_or_404(FeatureRequest, pk=feature_request_id)
    args = {'feature_request': feature_request_}
    args.update(csrf(request))
    return render(request, 'forum/feature_request.html', args)

def save_feature_request(feature_request_form, post_form, subject, user):
    feature_request = feature_request_form.save(commit=False)
    feature_request.subject = subject
    feature_request.user = user
    feature_request.save()

    post = post_form.save(commit=False)
    post.user = user
    post.feature_request = feature_request
    post.save() 
    return feature_request


@login_required
def new_post(request, feature_request_id):
    feature_request = get_object_or_404(FeatureRequest, pk=feature_request_id)
 
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(False)
            post.feature_request = feature_request
            post.user = request.user
            post.save()
 
            messages.success(request, "Your post has been added to the feature_request!")
 
            return redirect(reverse('feature_request', args={feature_request.pk}))
    else:
        form = PostForm()
 
    args = {
        'form' : form,
        'form_action': reverse('new_feature_request_post', args={feature_request.id}),
        'button_text': 'Update Post'
    }
    args.update(csrf(request))
 
    return render(request, 'forum/post_form.html', args)

@login_required
def edit_post(request, feature_request_id, post_id):
   feature_request = get_object_or_404(FeatureRequest, pk=feature_request_id)
   post = get_object_or_404(FRPost, pk=post_id)
 
   if request.method == "POST":
       form = PostForm(request.POST, instance=post)
       if form.is_valid():
           form.save()
           messages.success(request, "You have updated your feature_request!")
 
           return redirect(reverse('feature_request', args={feature_request.pk}))
   else:
       form = PostForm(instance=post)
 
 
   args = {
       'form' : form,
       'form_action': reverse('edit_post',  kwargs={"feature_request_id" : feature_request.id, "post_id": post.id}),
       'button_text': 'Update Post'
   }
   args.update(csrf(request))
 
   return render(request, 'forum/post_form.html', args)


@login_required
def delete_post(request, feature_request_id, post_id):
   post = get_object_or_404(FRPost, pk=post_id)
   feature_request = post.feature_request.id
   post.delete()
 
   messages.success(request, "Your post was deleted!")
 
   return redirect(reverse('feature_request', args={feature_request_id}))

@login_required
def feature_request_vote(request, feature_request_id, subject_id):
    feature_request = FeatureRequest.objects.get(id=feature_request_id)
    
    
    vote = feature_request.feature_request_votes.filter(user=request.user) 
    if vote:
      messages.error(request, "You already voted on this! ... You’re not trying to cheat are you?")
      return redirect(reverse('feature_request', args={feature_request_id}))
    else:
      feature_request.feature_votes += 1
      feature_request.save()
      Vote.objects.create(feature_request=feature_request, user=request.user)  
      return redirect(reverse('feature_request', args={feature_request_id}))