from bs4 import BeautifulSoup
import requests
import time 
from flask import *
app = Flask(__name__)


        


@app.route('/')
def index():
    while True: 
        URL = "https://www.worldometers.info/coronavirus/"
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find(id='maincounter-wrap').get_text()
        globally = title[21:28].rstrip()
        

        title_1 = soup.find(id='nav-tabContent').get_text()
        title_1 = title_1.splitlines()
        for i in range(len(title_1)):
            if title_1[i]=='India':
                india = title_1[i+1]    
                break
        return render_template('display.html',india=india,globally=globally)
        time.sleep(10)
    
    
        

if __name__ == '__main__':
    app.run(debug=True)

