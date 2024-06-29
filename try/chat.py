import nltk
import jieba
import jiagu
import jieba.analyse
while True:
    Greetings = ["你好"]
    text = input("请输入:")
    #print(jieba.)
    jieba_cut = jieba.cut(text)
    jiea_keyworlds = jieba.analyse.extract_tags(text, topK=20)
    jieba_keyworlds_textrank = jieba.analyse.textrank(text, topK=20, withWeight=False)
    jiagu_keyworlds = jiagu.keywords(text, 5)
    jiagu_sentiment = jiagu.sentiment(text)
    keywords = jiea_keyworlds + jieba_keyworlds_textrank + jiagu_keyworlds
    #print(", ".join(jieba.cut(text)))
    #print(jieba.analyse.extract_tags(text, topK=20))
    #print(jieba.analyse.textrank(text, topK=20, withWeight=False))
    #print(jiagu.keywords(text, 5))
    #print(jiagu.sentiment(text))
    world = []
    match keywords:
        case ["你好"]:
            print("你好")
        case ["鼠标"]:
            pass
        case ["壁纸"]:
            pass
        case ["电脑"]:
            pass