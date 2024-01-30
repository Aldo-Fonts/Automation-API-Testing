#!/bin/bash

# Brew installation
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Node installation
brew install node

# npm, newman and html reporter installation
npm install -g npm@10.2.4
npm install newman
npm install -g newman-reporter-htmlextra

# Python installation
brew install python@3.11

# Python behave installation
pip3 install behave

# Optional
pip3 install tkinter
pip3 install requests