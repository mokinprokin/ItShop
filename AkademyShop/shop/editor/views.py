from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import *
def main(request):
    items=Item.objects.all()
    return render(request,"main.html",{"items":items})
@csrf_exempt
def adminPanel(request):
    if (request.method=="POST"):
        if 'action' in request.POST:
            action=str(request.POST.get("action"))
            if action=='change':
                name=str(request.POST.get("header"))
                cost=int(request.POST.get("cost"))
                add=int(request.POST.get("add"))
                try:
                    item=Item.objects.get(cost=cost,name=name)
                    if(add==0 and item.count>0):
                        item.count-=1
                        item.save()
                    elif(add==1 and item.count<99):
                        item.count+=1
                        item.save()
                except Item.DoesNotExist:
                    print("bad request")
            elif action=='edit':
                name=str(request.POST.get("OldName"))
                cost=int(request.POST.get("OldCost"))
                try:
                    item=Item.objects.get(name=name,cost=cost)
                    new_name=str(request.POST.get("NewHeader"))
                    new_description=str(request.POST.get("NewDescription"))
                    new_cost=int(request.POST.get("NewCost"))
                    item.name=new_name
                    item.description=new_description
                    item.cost=new_cost
                    item.save()
                except Item.DoesNotExist:
                    print("bad request")
    items=Item.objects.all()
    return render(request,"admin.html",{"items":items})