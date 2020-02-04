# Set up

follow https://github.com/ckiplab/ckiptagger
- python>=3.6
- tensorflow>=1.13.1,<2 / tensorflow-gpu>=1.13.1,<2 (one of them)
- gdown (optional, for downloading model files from google drive)

1. Install ckiptagger, beautifulsoup4, scikit-learn
2. Downloading model file (require 2GB disk space)

`sh ./utils/setup.sh`

# testing ckiptagger (WS) word segmentation feature
`python ./tests/ckiptaggerTest.py`

# Word Tokenization
`sh ./wordTokenization/launcher.sh`

output files : 
- `./wordTokenization/description.txt`
- `./wordTokenization/output.txt`

# TF-IDF
`sh ./TF-IDF/launcher.sh`

output files : 
- `./TF-IDF/output.txt`
