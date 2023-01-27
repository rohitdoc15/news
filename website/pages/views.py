from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def click(request):
    return render(request, 'pages/afterclick.html')

def check_channel(request):
    channels = {'lallantop': 'UCx8Z14PpntdaxCt2hakbQLQ', 'aajtak': 'UCt4t-jeY85JegMlZ-E5UWtA',
                'abpnews': 'UCRWFSbif-RFENbBrSiez1DA', 'altnews': 'UCdDjoZAtt6PjQKAbr2FTOAQ',
                'indiatoday': 'UCYPvAwZP8pZhSMW8qs7cVCw', 'indiatv': 'UCttspZesZIDEwwpVIgoZtWQ',
                'ndtv': 'UC9CYT9gSNLevX5ey2_6CK0Q', 'theprint': 'UCuyRsHZILrU7ZDIAbGASHdA',
                'thequint': 'UCSaf-7p3J_N-02p7jHzm5tA', 'repulicbharat': 'UC7wXt18f2iA3EDXeqAVuKng',
                'timesnow': 'UC6RJ7-PaXg6TIH2BzZfTV7w', 'zeenews': 'UCIvaYmXn910QMdemBG3v1pQ','wion':'UC_gUM8rL-Lrg6O3adPW9K1g'}

    channel  = request.POST.get('q')
    if len(channel)>0:
        result = filter(lambda word: word.startswith((channel)), list(channels))
        context  = {'results':result}
        return render(request,'pages/searchlist.html', context)
    else:
        return HttpResponse("")


    # if channel in list(channels):
    #     return HttpResponse(channel)
    # else:
    #     return HttpResponse("channel not found")
