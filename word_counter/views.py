from django.shortcuts import render

# Create your views here.
def home(request):

    if request.method == 'POST':
        text = request.POST['text']
        amount_text = len(text.split())

        return render(request, 'index.html', {'amt' : amount_text})

    else:
        return render(request, 'index.html')    
    # return render(request, 'index.html')

# def count(request):
#     if request.method == 'POST':
#         text = request.POST['text']
#         amount_text = len(text.split())

#         return render(request, 'count.html', {'amt' : amount_text})
#     else:
#         return render(request, 'count.html')
            
    
        

