from django.shortcuts import render, redirect

def counter(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    return render(request,"index.html")

def destroy(request):
    if 'counter' in request.session:
        del request.session['counter']
    return redirect('/')

# def destroy(request):
        # session.clear()
    # return redirect('/')

#  def destroy(request):
    # if 'counter' in request.session:
        # request.session['counter'] = 0
    # return redirect('/')