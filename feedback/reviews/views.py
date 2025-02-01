from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import CreateView #automatically create data




class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = '/thankyou'
    #field = "__all__"  # us this 
    # can't add labels and error messages
    # this creates a form based on our definiting in the forms.py ReviewForm Model
    #will save
   
    #we don't need get and post  Need a succes URL. where to redirect
    #out of the box it won't save to database. Need to add it


    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     #we don't need get and post  Need a succes URL. where to redirect
#     #out of the box it won't save to database. Need to add it

#     success_url = '/thankyou'
    
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
    





# Create your views here.
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#         "form": form
#     })


#     def post(self, request):
#         form = ReviewForm(request.POST) # users to update an existing record
#         #existing_data = Review.objects.get(pk=1)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/thankyou')
#         #if here.. we aren't valid

#         return render(request, "reviews/review.html", {
#         "form": form
#     })

# a cleaner way to do this
class ThankyouView(TemplateView):
    template_name = "reviews/thank-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = 'This works'
        return context
        

# Much easier view but getting all
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "Movie_Reviews" # sets the variable to the name we can loop through in the HTML file
#can narrow down even more. ratings are > 3
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=3)
        return data
        
        
    




# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"
        
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context


# class ReviewDetailsView(DetailView):
#     template_name = "reviews/review_details.html"
        
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id=kwargs["review_id"] # cause we used review_id in teh urls.py path("review/<int:review_id>"
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context
    


        
class ReviewDetailsView(DetailView):
    template_name = "reviews/review_details.html"
    model = Review

        
    
    

