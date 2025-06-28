from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def chat_echange(request):
    return render(request, 'Chat/chat_echange.html')

