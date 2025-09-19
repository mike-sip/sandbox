from django.http import HttpResponse
from django.shortcuts import render

from .models import Band, Listing


def hello(request):
    """
    Handles an HTTP request to display a welcome message and a list of favorite bands.

    This function queries all Band objects, retrieves their names, and dynamically generates
    an HTML response that displays a welcome message along with the names of the first three
    bands in the list.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: An HTTP response containing the generated HTML content with the welcome
        message and the list of bands.
    :rtype: HttpResponse
    """
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {"bands": bands})


def about(request):
    """
    Render the 'about' page.

    This function handles rendering the "about.html" template for the user.

    :param request: The HTTP request object.
    :return: A rendered "about.html" template as an HTTP response.
    """
    return render(request, "listings/about.html")


def listings(request):
    """
    Fetches and renders all the available listings.

    This function retrieves all the listings from the database using the
    Listing model and renders the listings page with the fetched data.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: Rendered HTML response with the listings information.
    :rtype: HttpResponse
    """
    listings = Listing.objects.all()
    return render(request, "listings/listings.html", {"listings": listings})


def contact(request):
    """
    Handles the request for the contact page and renders the corresponding HTML template.

    :param request: HttpRequest object representing the request context
    :type request: HttpRequest
    :return: HttpResponse object rendering the contact.html template
    :rtype: HttpResponse
    """
    return render(request, "listings/contact.html")
