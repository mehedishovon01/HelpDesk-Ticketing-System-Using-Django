from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import TicketCreateForm, TicketUpdateForm
from django.contrib.auth.models import User
from .models import Ticket

# View for creating a new ticket
def ticket_create(request):
    """
    This function handles ticket creation by processing the ticket create form.
    If the http method is POST then it will create a new ticket otherwise it will show all the ticket for the user.
    HTTP Method: POST, GET
    """
    # Handle form submission
    if request.POST:
        form = TicketCreateForm(request.POST)
        # Validate the form
        if form.is_valid():
            # Save the form data to the database
            obj = form.save()
            # Set owner and status for the newly created ticket
            obj.user = request.user
            obj.status = "TODO"
            obj.save()
            # Redirect to the ticket creation page
            return redirect('create-ticket')
    else:
        # Display a blank form for ticket creation
        form = TicketCreateForm()
        # Retrieve and display existing tickets for the current user in descending order
        tickets = Ticket.objects.filter(user=request.user.id).order_by('-id')
    # Render the page with the form and ticket data
    return render(request, 'index.html', {'form': form, 'tickets': tickets})

# View for displaying and updating ticket details
def ticket_detail(request, ticket_id):
    """
    This function handles ticket details and edit by processing the ticket update form.
    If the http method is POST then it will update the ticket otherwise it will show the ticket's details.
    HTTP Method: POST, GET
    """
    # Retrieve the ticket by its ID
    data = Ticket.objects.get(id=ticket_id)
    # Handle form submission for updating ticket details
    if request.method == 'POST':
        form = TicketUpdateForm(request.POST, instance=data)
        # Validate the form
        if form.is_valid():
            # Save the updated form data to the database
            form.save()
            return redirect('create-ticket')
    else:
        # Display a form pre-filled with existing ticket data
        form = TicketUpdateForm(instance=data)
    # Pass the ticket object to the template
    return render(request, 'edit.html', {'ticket': form})

# Deleting a ticket
def ticket_delete(ticket_id):
    """
    This function handles ticket deletation by processing the delete method.
    HTTP Method: GET
    """
    # Retrieve the ticket by its ID or return a 404 error
    ticket = get_object_or_404(Ticket, id=ticket_id)
    # Delete the ticket
    ticket.delete()
    # Redirect to the ticket creation page after deletion
    return redirect('create-ticket')
