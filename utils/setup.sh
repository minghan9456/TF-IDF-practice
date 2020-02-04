#!/usr/bin/sh

echoLog()
{
  msg=$1
  dateTime=$(date +'%Y-%m-%d %H:%M:%S')
  echo "[ $dateTime ] : $msg"
}

echo "$PWD"

# install beautifulsoup4, scikit-learn
echoLog "Install beautifulsoup4, scikit-learn."

pip3 install -U beautifulsoup4 scikit-learn

echoLog "Done"

# install ckiptagger
echoLog "Install ckiptagger."

pip3 install -U ckiptagger[tf,gdown]

echoLog "Done"

# Fetch Source
echoLog "Download model files."

python ./utils/downloadCkipTaggerModel.py

rm ./data.zip

echoLog "Done"
