# Automated orbitz.com website test case #
This is functional automated test for orbitz website
# Requirements: #
[Python 3.7+](https://www.python.org/downloads/) \
AND\
[Docker (only for selenoid)](https://www.docker.com/products/docker-desktop) \
OR\
[Google Chrome (only for local run)](https://www.google.ru/intl/ru/chrome)
# Installation: #
`git clone git@github.com:mpolynskyi/orbitz_seleniumbase.git&&\`\
`cd orbitz_seleniumbase&&\`\
`pip3 install virtualenv&&\`\
`virtualenv venv --python=python3&&\`\
`source venv/bin/activate python&&\`\
`pip install -r requirements.txt`
# How to run test #
## If you want local broser run: ##
`seleniumbase install chromedriver`\
`pytest -s`\
![local-run-process](https://user-images.githubusercontent.com/12695133/82375829-d4a2d800-9a29-11ea-8f5b-5fdeeb4042b5.gif)
## If you want to use selenoid: ##
`docker pull selenoid/vnc_chrome:81.0`\
`docker-compose up`\
Run in different terminal window:\
`pytest -s --server=127.0.0.1 --port=4444 --cap_file=cap.py `\
Check run process in selenoid-ui: 127.0.0.1:8080
<img width="640" alt="Selenoid UI 2020-05-20 13-02-57" src="https://user-images.githubusercontent.com/12695133/82434401-7a425f80-9a9b-11ea-9d0e-ebfabd6a2eec.png">\
## "venv" deactivation/activation. Use "activate" in installation folder: ##
Deactivation venv command: `deactivate`  
Activation venv command: `source venv/bin/activate python`
