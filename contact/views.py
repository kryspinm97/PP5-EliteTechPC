from django.shortcuts import render

# Create your views here.


def contact_us(request):

    """ View function for the contact us form """

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactUsForm()

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context)
