from matplotlib import pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud, ImageColorGenerator
import jieba

# 添加自己的词库分词，比如添加'金三胖'到jieba词库后，当你处理的文本中含有金三胖这个词，
# 就会直接将'金三胖'当作一个词，而不会得到'金三'或'三胖'这样的词
#jieba.add_word('中国人民')

text = open('./text.txt').read()

# 该函数的作用就是把屏蔽词去掉，使用这个函数就不用在WordCloud参数中添加stopwords参数了
# 把你需要屏蔽的词全部放入一个stopwords文本文件里即可


def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts, cut_all=False)  # 返回的是一个迭代器
    with open('stopwords.txt') as f:
        str_text = f.read()
        # unicode_text = unicode(str_text, 'utf-8')  # 把str格式转成unicode格式
        f.close()  # stopwords文本中词的格式是'一词一行'
    for word in word_generator:
        if word.strip() not in str_text:
            words_list.append(word)
    return ' '.join(words_list)  # 注意是空格


text = stop_words(text)

back_color = imread('./1.PNG')


font = r'C:\Windows\Fonts\LiHei Pro.TTF'
wc = WordCloud(font_path=font,  # 如果是中文必须要添加这个，否则会显示成框框
               background_color='white',
               max_words=500,  # 最大词数
               mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
               max_font_size=100,  # 显示字体的最大值
               random_state=42,
               # width=600,
               # height=600,
               ).generate(text)
image_colors = ImageColorGenerator(back_color)
plt.imshow(wc.recolor(color_func=image_colors))  # 用plt显示图片
wc.to_file('ss.png')  # 保存图片
plt.axis('off')  # 不显示坐标轴
plt.show()  # 显示图片
