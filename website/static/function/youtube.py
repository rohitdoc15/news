from googleapiclient.discovery import build

api_key = "AIzaSyCitwCx37bwvi-PoCXm3xzRAhNyycVCptc"
youtube = build('youtube', 'v3', developerKey=api_key)

def update(name , id):
    channel_id = id
    request = youtube.search().list(part="snippet", channelId=channel_id, order='date', maxResults=200)
    response = request.execute()
    text = ' '

    for video in response['items']:
        answer = (video["snippet"]["title"])
        text = text + answer

    with open(f"texts/{name}.txt", "w" , encoding='utf8') as file:
        file.write(text)

channels = {'lallantop': 'UCx8Z14PpntdaxCt2hakbQLQ', 'aajtak': 'UCt4t-jeY85JegMlZ-E5UWtA' , 'abpnews': 'UCRWFSbif-RFENbBrSiez1DA','altnews':'UCdDjoZAtt6PjQKAbr2FTOAQ' , 'indiatoday':'UCYPvAwZP8pZhSMW8qs7cVCw','indiatv':'UCttspZesZIDEwwpVIgoZtWQ','ndtv':'UC9CYT9gSNLevX5ey2_6CK0Q','theprint':'UCuyRsHZILrU7ZDIAbGASHdA' ,'thequint':'UCSaf-7p3J_N-02p7jHzm5tA' , 'repulicbharat':'UC7wXt18f2iA3EDXeqAVuKng','timesnow':'UC6RJ7-PaXg6TIH2BzZfTV7w' , 'zeenews':'UCIvaYmXn910QMdemBG3v1pQ','wion':'UC_gUM8rL-Lrg6O3adPW9K1g'}

for i in channels:
    try:
        update(i, channels[i])
    except:
        print('erorr')



