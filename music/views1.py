from django.http import HttpResponse
from .models import Album , Song
#from django.template import loader
from django.shortcuts import render ,get_object_or_404
from django.http import Http404

def index(request):
	all_album = Album.objects.all()


	'''html = ''
	for album in all_album:
		url = '/music/' + str(album.id) + '/'
		html += '<a href = "'+ url +'" >album.album_title</a><br>'
	return HttpResponse(html)'''
	#template = loader.get_template('music/index.html')

	#return HttpResponse(template.render(context,request))


	return render(request,'music/index.html',{'all_album' : all_album})



def detail(request,album_id):


	#return HttpResponse("<h2>Album ID "+str(album_id)+" </h2>")
	'''try:
		#album = Album.objects.get(pk = album_id)

	except Album.DoesNotExist:
		raise Http404("Not exist")'''

	album = get_object_or_404(Album,pk = album_id)
	return render(request, 'music/detail.html', {'album' : album})

def favourite(request,album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except (KeyError,Song.DoesNotExist):
		return render(request,'music/detail.html',
					  {
						'album':album,
						'error_message':"you did not select any song "
					  })
	else:
		selected_song.is_favourite = True
		selected_song.save()
		return render(request, 'music/detail.html', {'all_album': album})


