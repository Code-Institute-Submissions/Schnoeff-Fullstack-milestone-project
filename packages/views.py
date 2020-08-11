from django.shortcuts import render
from .models import Package
# Create your views here.


def all_packages(request):
    """ returns all of the packages available """

    packages = Package.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)
