from django.shortcuts import render, redirect
from .models import Questionbase
import random
# Create your views here.
def index(request):
    noq=3
    all=Questionbase.objects.order_by('id')
    random_idx=random.sample(list(all), k=noq )
    a=["Please answer these questions"]
    b=["Result will be shown here"]
    if request.method == 'POST':
        a=[]
        for c in range(noq):
            UserAnswer=request.POST["UserAnswer"+str(c)]
            TrueAnswer=request.POST["TrueAnswer"+str(c)]
            if UserAnswer == TrueAnswer:
                a.append("Correct")
            else:
                a.append("Wrong")



    context={'qbase':random_idx,'a':a,'noq':3}
    
    return render(request,"homepage/index.html",context)
