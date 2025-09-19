from django.http import HttpResponse


def hello(request):
    """
    Handles the incoming web request and returns an HTTP response with a greeting.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The HTTP response with a greeting message.
    :rtype: HttpResponse
    """
    return HttpResponse("<h1>Hello Django!</h1>")


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
    Handles HTTP requests to display a listing page.

    This function is used to return an HTTP response that contains a simple
    HTML heading indicating 'Listings'. It does not perform any other
    processing besides returning this static response.

    :param request: HttpRequest object representing the HTTP request made
        to the server.
    :type request: HttpRequest

    :return: HttpResponse containing a simple HTML content.
    :rtype: HttpResponse
    """
    return HttpResponse("<h1>Listings</h1>")


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