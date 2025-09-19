from django.http import HttpResponse

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
    return HttpResponse(f"""
            <h1>Hello Django !</h1>
            <p>Mes groupes préférés sont :<p>
            <ul>
                <li>{bands[0].name}</li>
                <li>{bands[1].name}</li>
                <li>{bands[2].name}</li>
            </ul>
    """)


def about(request):
    """
    Handles the 'About' page request and returns an HTTP response with
    the content of the 'About' page. This page typically includes a
    message regarding the purpose or goals of the website or organization.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: An HTTP response containing the 'About' page content.
    :rtype: HttpResponse
    """
    return HttpResponse("<h1>À propos</h1> <p>Nous adorons merch !</p>")


def listings(request):
    """
    Retrieves a list of all listings from the database, constructs an HTML
    response displaying their titles, and returns the response.

    :param request: The HTTP request object.
    :return: An HTTP response object containing an HTML representation
        of the listing titles.
    """
    listings = Listing.objects.all()
    return HttpResponse(f"""
            <h1>Listings</h1>
            <ul>
                <li>{listings[0].title}</li>
                <li>{listings[1].title}</li>
                <li>{listings[2].title}</li>
                <li>{listings[3].title}</li>
            </ul>
    """)


def contact(request):
    """
    Handles the contact page request and returns an HTTP response with a simple
    HTML content.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: An HTTP response with the contact page content.
    :rtype: HttpResponse
    """
    return HttpResponse("<h1>Contact</h1>")
