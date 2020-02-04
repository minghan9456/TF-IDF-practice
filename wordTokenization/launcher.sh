#!/usr/bin/sh

echoLog()
{
  msg=$1
  dateTime=$(date +'%Y-%m-%d %H:%M:%S')
  echo "[ $dateTime ] : $msg"
}

echo "$PWD"

# Fetch Source
echoLog "Start download google news rss."

curl 'https://news.google.com/rss?hl=zh-TW&gl=TW&ceid=TW:zh-Hant' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H 'accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7' -o `pwd`'/wordTokenization/news.rss'

echoLog "Done"

# init output file
echoLog "Initial description.txt file."
echo "" > `pwd`/wordTokenization/description.txt
echoLog "Done"

echoLog "Initial output.txt file."
echo "" > `pwd`/wordTokenization/output.txt
echoLog "Done"

# Word Tokenization
echoLog "Excute Word Tokenization Program"

python ./wordTokenization/main.py

echoLog "Done"
