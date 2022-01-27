from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
import logging
from django.contrib import messages

# Create your views here.
def index(request):
    print("ran")
    return render(request, "app/index.html")

def index2(request):
    if request.method=="POST":
        # Get the post parameters
        name=request.POST['name']
        if name=='shan':
          messages.info(request, 'hello shan!')
          return render(request, "app/index2.html")
        else:
          messages.info(request, 'who r u? '+name)
          return render(request, "app/index2.html")
    return redirect("index")






##################################################
#logging 
# logging.debug('debugging.')
# logging.info('Relax!')
# logging.warning('Something')
# logging.error('unexpected')
# logging.critical('OMG!!!')
# lol= "123456789"
# logging.error('%s normal. Relax! %s',lol,42)