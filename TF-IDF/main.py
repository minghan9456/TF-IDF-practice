import os
import sys
from datetime import datetime
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

def main():
    corpus = []
    articleCount = 0

    outputFile = open("./TF-IDF/output.txt","w+")

    file = open("./wordTokenization/output.txt", "r") 
    for line in file: 
        line = line.rstrip()
        if line:
            corpus.append(line) 
            articleCount+=1

    echoLog("Article count is : %d" %articleCount)

    vectorizer=CountVectorizer()
    transformer=TfidfTransformer()
    tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))
    word=vectorizer.get_feature_names()
    weight=tfidf.toarray()

    for i in range(len(weight)):
        outputFile.write(corpus[i] + "\n")

        for j in range(len(word)):
            oneLine = '{word} : {weight}'.format(word = word[j], weight = weight[i][j])
            outputFile.write(oneLine + "\n")

def echoLog(msg):
    now = datetime.now()
    current_time = now.strftime("[ %Y-%m-%d %H:%M:%S ]")
    print(current_time, ":", msg)

if __name__ == "__main__" :
    main()

"""
if __name__ == "__main__":
    corpus=[
        "武漢 肺炎 》 疫情 仍 不斷 蔓延 湖北省 單日 增加 56 死",
        "為何 武漢 肺炎 都 死 在 湖北 ？ 知情人 曝 「 2 致命 主因 」, ！",
        "武漢 下令 集中 隔離 確診 疑似 發熱 接觸者 4, 類, 人員",
        "滯武漢 200 台人 武漢 台協 會長 ：18時 辦 手續 返台",
    ]
    for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
        print(u"-------这里输出第",i,u"类文本的词语tf-idf权重------")
        print(corpus[i])
        for j in range(len(word)):
            print(word[j],weight[i][j])
"""
