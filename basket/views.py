from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Basket
from .forms import BasketForm

# def create_basket_view(request):
#      if request.method == 'POST':
#         form = BasketForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/basket_list/')
#      else:
#         form = BasketForm()
#      return render(
#          request,
#          template_name='basket/create_basket.html',
#          context={"form": form}
#      )

class BasketCreateView(CreateView):
    model = Basket
    form_class = BasketForm
    template_name = 'basket/create_basket.html'
    success_url = reverse_lazy('basket_list')



# #READ
# def read_basket_view(request):
#     if request.method == 'GET':
#         basket = Basket.objects.all()
#     return render(request, template_name='basket/basket_list.html',
#                   context={'basket': basket})    

class BasketListView(ListView):
    model = Basket
    template_name = 'basket/basket_list.html'
    context_object_name = 'basket'



# #update
# def update_basket_view(request, id):
#     basket_id = get_object_or_404(Basket, id=id)
#     if request.method == 'POST':
#         form = BasketForm(request.POST, instance=basket_id)
#         if form.is_valid():
#             form.save()
#             return redirect('/basket_list/')
#     else: 
#         form = BasketForm(instance=basket_id)
#     return render(request,
#                   template_name='basket/update_basket.html',
#                   context={
#                       'form': form,
#                       'basket_id': basket_id
#                   }
#                 )

class BasketUpdateView(UpdateView):
    model = Basket
    form_class = BasketForm
    template_name = 'basket/update_basket.html'
    success_url = reverse_lazy('basket_list')



# #delete
# def delete_basket_view(request, id):
#     basket_id = get_object_or_404(Basket, id=id)
#     basket_id.delete()
#     return redirect('/basket_list/')

class BasketDeleteView(DeleteView):
    model = Basket
    template_name = 'basket/delete_confirm.html'
    success_url = reverse_lazy('basket_list')
