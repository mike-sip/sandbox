from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactUsForm, BandForm
from .models import Band, Listing


def band_list(request):
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
    return render(request, "listings/band_list.html", {"bands": bands})


def band_detail(request, id):
    """
    Renders the band detail page with the specified ID.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param id: The unique identifier of the band.
    :type id: int
    :return: An HttpResponse object rendering the band detail page.
    :rtype: HttpResponse
    """
    band = Band.objects.get(id=id)
    return render(request, "listings/band_detail.html", {"band": band})


def band_create(request):
    """
    Handles the creation of a new band entry through an HTTP request. This function
    renders a form for creating a new band and facilitates user interaction to
    submit the form.

    :param request: HTTP request object that provides details about the incoming
        HTTP request from the client.
    :type request: HttpRequest
    :return: Rendered HTML template for the band creation form.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, "listings/band_create.html", {"form": form})


def about(request):
    """
    Render the 'about' page.

    This function handles rendering the "about.html" template for the user.

    :param request: The HTTP request object.
    :return: A rendered "about.html" template as an HTTP response.
    """
    return render(request, "listings/about.html")


def listing(request):
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
    return render(request, "listings/listing.html", {"listings": listings})


def listing_detail(request, id):
    """
    Retrieve detailed information for a specific listing by its ID and render it
    in the designated template.

    :param request: HttpRequest object containing metadata about the request.
    :type request: HttpRequest
    :param id: An integer representing the unique identifier of the listing.
    :type id: int
    :return: An HttpResponse object containing the rendered template with the
        context of the specific listing.
    :rtype: HttpResponse
    """
    listing = Listing.objects.get(id=id)
    return render(request, "listings/listing_detail.html", {"listing": listing})


def contact(request):
    """
    Handles the request for the contact page and renders the corresponding HTML template.

    :param request: HttpRequest object representing the request context
    :type request: HttpRequest
    :return: HttpResponse object rendering the contact.html template
    :rtype: HttpResponse
    """
    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )

            return redirect("email-sent")
    else:
        form = ContactUsForm()
    return render(request, "listings/contact.html", {"form": form})


def email_sent(request):
    """
    Renders the email sent confirmation page.

    This function is responsible for rendering a template that provides confirmation
    to the user that an email has been sent successfully.

    :param request: The HTTP request object.
    :return: Renders the `listings/email_sent.html` template as an HTTP response.
    """
    return render(request, "listings/email_sent.html")
