from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from accounts.models import UserProfile, HelperProfile
from hirings.models import Hiring, Review


@login_required
def create_hiring(request, helper_id):
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('accounts:signup')

    helper = get_object_or_404(HelperProfile, pk=helper_id)

    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        notes = request.POST.get('notes', '')

        hiring = Hiring.objects.create(
            user=user_profile,
            helper=helper,
            start_date=start_date,
            notes=notes,
            status='pending'
        )

        helper.availability_status = 'busy'
        helper.save()

        messages.success(request, 'হায়ার রিকোয়েস্ট পাঠানো হয়েছে!')
        return redirect('hirings:my_hirings')

    context = {
        'helper': helper,
    }
    return render(request, 'hirings/create_hiring.html', context)


@login_required
def my_hirings(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('accounts:signup')

    status_filter = request.GET.get('status', '')

    if profile.account_type == 'helper':
        helper_profile = profile.helper_profile
        hirings = helper_profile.hirings.all()
    else:
        hirings = profile.hirings.all()

    if status_filter:
        hirings = hirings.filter(status=status_filter)

    context = {
        'hirings': hirings,
        'current_status': status_filter,
    }
    return render(request, 'hirings/my_hirings.html', context)


@login_required
def submit_review(request, hiring_id):
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('accounts:signup')

    hiring = get_object_or_404(Hiring, pk=hiring_id, user=user_profile)

    if hiring.status != 'completed':
        messages.error(request, 'শুধুমাত্র সম্পন্ন হায়ারিং এর জন্য রিভিউ দেওয়া যায়।')
        return redirect('hirings:my_hirings')

    if hasattr(hiring, 'review'):
        messages.error(request, 'আপনি ইতিমধ্যে এই হায়ারিং এর জন্য রিভিউ দিয়েছেন।')
        return redirect('hirings:my_hirings')

    if request.method == 'POST':
        rating = int(request.POST.get('rating', 0))
        comment = request.POST.get('comment', '')

        if rating < 1 or rating > 5:
            messages.error(request, 'রেটিং ১-৫ এর মধ্যে হতে হবে।')
            return render(request, 'hirings/submit_review.html', {'hiring': hiring})

        Review.objects.create(
            hiring=hiring,
            rating=rating,
            comment=comment
        )

        helper = hiring.helper
        reviews = Review.objects.filter(hiring__helper=helper)
        from django.db.models import Avg
        avg = reviews.aggregate(Avg('rating'))['rating__avg']
        helper.average_rating = round(avg, 2) if avg else 0
        helper.total_reviews = reviews.count()
        helper.save()

        messages.success(request, 'আপনার রিভিউ সফলভাবে জমা দেওয়া হয়েছে!')
        return redirect('hirings:my_hirings')

    return render(request, 'hirings/submit_review.html', {'hiring': hiring})


@login_required
def cancel_hiring(request, hiring_id):
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('accounts:signup')

    hiring = get_object_or_404(Hiring, pk=hiring_id)

    is_helper = (user_profile.account_type == 'helper'
                 and hasattr(user_profile, 'helper_profile')
                 and hiring.helper == user_profile.helper_profile)

    if hiring.user != user_profile and not is_helper:
        messages.error(request, 'আপনি এই হায়ারিং বাতিল করতে পারবেন না।')
        return redirect('hirings:my_hirings')

    if hiring.status != 'pending':
        messages.error(request, 'শুধুমাত্র অপেক্ষমাণ হায়ারিং বাতিল করা যায়।')
        return redirect('hirings:my_hirings')

    hiring.status = 'cancelled'
    hiring.save()

    helper = hiring.helper
    if not helper.hirings.filter(status='active').exists():
        helper.availability_status = 'available'
        helper.save()

    messages.success(request, 'হায়ারিং বাতিল করা হয়েছে।')
    return redirect('hirings:my_hirings')


@login_required
def accept_hiring(request, hiring_id):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('accounts:signup')

    if profile.account_type != 'helper' or not hasattr(profile, 'helper_profile'):
        messages.error(request, 'শুধুমাত্র হেল্পাররা হায়ারিং গ্রহণ করতে পারেন।')
        return redirect('hirings:my_hirings')

    hiring = get_object_or_404(Hiring, pk=hiring_id, helper=profile.helper_profile)

    if hiring.status != 'pending':
        messages.error(request, 'শুধুমাত্র অপেক্ষমাণ হায়ারিং গ্রহণ করা যায়।')
        return redirect('hirings:my_hirings')

    hiring.status = 'active'
    hiring.save()

    messages.success(request, 'হায়ারিং রিকোয়েস্ট গ্রহণ করা হয়েছে!')
    return redirect('hirings:my_hirings')


@login_required
def complete_hiring(request, hiring_id):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('accounts:signup')

    if profile.account_type != 'helper' or not hasattr(profile, 'helper_profile'):
        messages.error(request, 'শুধুমাত্র হেল্পাররা হায়ারিং সম্পন্ন করতে পারেন।')
        return redirect('hirings:my_hirings')

    hiring = get_object_or_404(Hiring, pk=hiring_id, helper=profile.helper_profile)

    if hiring.status != 'active':
        messages.error(request, 'শুধুমাত্র সক্রিয় হায়ারিং সম্পন্ন করা যায়।')
        return redirect('hirings:my_hirings')

    hiring.status = 'completed'
    from datetime import date
    hiring.end_date = date.today()
    hiring.save()

    helper = hiring.helper
    if not helper.hirings.filter(status='active').exists():
        helper.availability_status = 'available'
        helper.save()

    messages.success(request, 'হায়ারিং সম্পন্ন হিসাবে চিহ্নিত করা হয়েছে!')
    return redirect('hirings:my_hirings')
