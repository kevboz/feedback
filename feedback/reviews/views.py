from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm



# Create your views here.
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()

            
            review.save() #saves to the DB
            return HttpResponseRedirect('/thankyou')

    # not a post so lets render the template
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


def thankyou(request):
    return render(request, "reviews/thank-you.html")
