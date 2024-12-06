from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer
from .forms import ContactForm

class ContactListAPI(APIView):
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactDetailAPI(APIView):
    def get(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def put(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# List all contacts
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_manager/contact_list.html', {'contacts': contacts})

# Create a new contact
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contact_manager/contact_form.html', {'form': form})

# Edit an existing contact
def contact_edit(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_manager/contact_form.html', {'form': form})

# Delete a contact
def contact_delete(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contact_manager/contact_confirm_delete.html', {'contact': contact})