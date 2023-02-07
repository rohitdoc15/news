import PIL.Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np


def update(channel):
    # Your text data

    text = open(f'texts/{channel}.txt', 'r', encoding='utf8').read()
    stop = open('stop.txt', 'r', encoding='utf8').read()

    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    freq_list = Counter(words)

    for i in list(freq_list):
        if i in stop:
            freq_list.pop(i)

    # print(freq_list)

    # # Create a dictionary from the frequency list
    word_freq = dict(freq_list)

    python_mask = np.array(PIL.Image.open(f"logos/{channel}.jpg"))
    colormap = ImageColorGenerator(python_mask)
    # Generate word cloud
    wordcloud = WordCloud(font_path='Arya-Regular.ttf',
                          mask=python_mask,
                          min_word_length=200,
                          background_color=None,
                          max_words=400,
                          stopwords=set(list(STOPWORDS) + list(stop)),
                          min_font_size=5).generate_from_frequencies(word_freq)
    wordcloud.recolor(color_func=colormap)
    # Plot the word cloud
    plt.figure(figsize=(10, 10), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    svg_image = wordcloud.to_svg(embed_font=True)
    png_image = wordcloud.to_file(f"clouds/png/{channel}.png")
    with open(f"clouds/{channel}.svg", "w+", encoding='UTF-8') as f:
        f.write(svg_image)



channels = {'lallantop': 'UCx8Z14PpntdaxCt2hakbQLQ', 'aajtak': 'UCt4t-jeY85JegMlZ-E5UWtA',
            'abpnews': 'UCRWFSbif-RFENbBrSiez1DA', 'altnews': 'UCdDjoZAtt6PjQKAbr2FTOAQ',
            'indiatoday': 'UCYPvAwZP8pZhSMW8qs7cVCw', 'indiatv': 'UCttspZesZIDEwwpVIgoZtWQ',
            'ndtv': 'UC9CYT9gSNLevX5ey2_6CK0Q', 'theprint': 'UCuyRsHZILrU7ZDIAbGASHdA',
            'thequint': 'UCSaf-7p3J_N-02p7jHzm5tA', 'repulicbharat': 'UC7wXt18f2iA3EDXeqAVuKng',
            'timesnow': 'UC6RJ7-PaXg6TIH2BzZfTV7w', 'zeenews': 'UCIvaYmXn910QMdemBG3v1pQ',
            'wion': 'UC_gUM8rL-Lrg6O3adPW9K1g'}

for i in channels:

    # try:
    update(i)

    # except:
    #     print('erorr in', i)
