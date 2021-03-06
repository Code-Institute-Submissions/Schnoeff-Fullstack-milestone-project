from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_bag(request):
    """ returns shopping basket """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_bag_item(request, item_id):

    bag = request.session.get('bag', {})
    del bag[item_id]

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
