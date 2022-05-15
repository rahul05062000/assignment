from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import item,bill,print
# from .form import billForm

# Create your views here.
def index(request):
    list=item.objects.all()
    return render(request,'first.html',{'list':list})

def save_list(request):
    if request.method == 'POST':
        s_no= request.POST.get('s_no')
        item1 = request.POST.get('item1')
        
        list_obj =bill(item1_quantity=item1,s_no=s_no)
        list_obj.save()
        return redirect(index)
 
def show(request):
    if request.method=="POST":
        price=item.objects.all()
        quant=bill.objects.all()
        print.objects.all().delete()
        for f in price:
          for k in  quant:
              if f.s_no==k.s_no:
                  print_obj=print(item_name=f.name,item_quantity=k.item1_quantity,item_price=f.price,item_total=int(f.price)*int(k.item1_quantity))
                  print_obj.save()
        
        ans=print.objects.all()
        sum=0
        for i in ans:
            sum=int(sum)+int(i.item_total)
            
        return render(request,'third.html',{'ans':ans,'sum':sum})
        

    return render(request,'first.html')  

def clear(request):
    if request.method=="POST":
        bill.objects.all().delete()
    return redirect(index)

from django import template
register = template.Library()

          

# importing the necessary libraries
# from django.http import HttpRespons
from django.views.generic import View
from .process import html_to_pdf 
from django.template.loader import get_template

#Creating a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        template = get_template('third.html')
        context = {}
        ans=print.objects.all()
        sum=0
        for i in ans:
            sum=int(sum)+int(i.item_total)
        # getting the template
        pdf = html_to_pdf('third.html',{'ans':ans,'sum':sum})
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

# def update(request):
#     bill_obj=bill.objects.all()
#     form=billForm(request.POST or None)
#     return render(request,'update_post.html',{'bill_obj':bill_obj,'form':form})


