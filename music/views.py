from django.views import generic
from django.views.generic.edit import CreateView , UpdateView ,DeleteView
from .models import Album ,Song
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Album
from .forms import User
from .forms import UserForm



class indexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_album'

    def get_queryset(self):
        return Album.objects.all()


class detailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'



class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre' , 'album_logo']


class UserformView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'


    #display a blank form

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})



    #process form data

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():


            user = form.save(commit=False)

            # cleaned (normalized)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)

            user.save()





            # return user Objects if credetial are correct

            user = authenticate(username = username , password = password)

            if user is not None :

                if user.is_active:
                    login(request,user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})
















