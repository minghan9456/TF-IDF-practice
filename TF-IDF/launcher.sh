#!/usr/bin/sh

echoLog()
{
  msg=$1
  dateTime=$(date +'%Y-%m-%d %H:%M:%S')
  echo "[ $dateTime ] : $msg"
}

echo "$PWD"

# init output file
echoLog "Initial output.txt file."
echo "" > `pwd`/TF-IDF/output.txt
echoLog "Done"

# Word Tokenization
echoLog "Excute TF-IDF Program"

python ./TF-IDF/main.py

echoLog "Done"
