from bs4 import BeautifulSoup
from datetime import datetime
from ckiptagger import WS, construct_dictionary 

def main():
    ws = WS("./data")

    descFile = open("./wordTokenization/description.txt","w+")
    outputFile = open("./wordTokenization/output.txt","w+")

    with open("./wordTokenization/news.rss") as fp:
        soup = BeautifulSoup(fp, features="lxml")
    
    items = soup.find_all("item")
    
    echoLog("Google news rss item count is : %d" %len(items))
    
    articleCount = 0
    
    for item in items:
        descObj = item.find('description')
        desc = descObj.getText()
    
        htmlSoup = BeautifulSoup(desc, features="lxml")
        aObjs = htmlSoup.find_all("a")
    
        aCount = len(aObjs)
        if aCount > 1:
            for x in range(aCount-2):
                articleCount+=1
    
                article = aObjs[x].getText()
                descFile.write(article + "\n")
    
                ws_results = ws([article])

                oneLineStr = ''
                if len(ws_results) >= 1:
                    for word in ws_results[0]:
                        word = word.rstrip()
                        if word:
                            oneLineStr += word + ' '

                outputFile.write(oneLineStr.rstrip() + "\n")
                #print(oneLineStr)
    
    echoLog("Article count is : %d" %articleCount)
    del ws
    descFile.close()
    outputFile.close()

def echoLog(msg):
    now = datetime.now()
    current_time = now.strftime("[ %Y-%m-%d %H:%M:%S ]")
    print(current_time, ":", msg)

if __name__ == "__main__" :
    main()
