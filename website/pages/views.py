from django.shortcuts import render
from django.http import HttpResponse , JsonResponse ,FileResponse
from . import templates

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def click(request):
    result = request.POST.get('name')
    print(result)
    context = {'results': result}
    return render(request, 'pages/afterclick.html',context)

def check_channel(request):
    channels = {'lallantop': 'UCx8Z14PpntdaxCt2hakbQLQ', 'aajtak': 'UCt4t-jeY85JegMlZ-E5UWtA',
                'abpnews': 'UCRWFSbif-RFENbBrSiez1DA', 'altnews': 'UCdDjoZAtt6PjQKAbr2FTOAQ',
                'indiatoday': 'UCYPvAwZP8pZhSMW8qs7cVCw', 'indiatv': 'UCttspZesZIDEwwpVIgoZtWQ',
                'ndtv': 'UC9CYT9gSNLevX5ey2_6CK0Q', 'theprint': 'UCuyRsHZILrU7ZDIAbGASHdA',
                'thequint': 'UCSaf-7p3J_N-02p7jHzm5tA', 'repulicbharat': 'UC7wXt18f2iA3EDXeqAVuKng',
                'timesnow': 'UC6RJ7-PaXg6TIH2BzZfTV7w', 'zeenews': 'UCIvaYmXn910QMdemBG3v1pQ','wion':'UC_gUM8rL-Lrg6O3adPW9K1g'}

    channel  = request.POST.get('q')
    result = filter(lambda word: word.startswith(channel.lower()), list(channels))
    result = list(result)
    while len(result) >0 and len(result)<4:
        print(result)

        context = {'results': result}


        return render(request, 'pages/searchlist.html', context)

    if len(channel) ==0:
        return HttpResponse('')



    else:
        return render(request, 'pages/nf.html')

def channel_name(request):
    channel = request.POST.get('name')
    context = {'channel': channel}
    print(channel)


    return render(request, 'pages/channelname.html' , context)

def cloud(request):
    result = request.POST.get('name')
    print(result)
    context = {'results': result}
    return render(request, 'pages/cloud.html',context)
