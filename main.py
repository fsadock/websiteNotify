import requests
from time import strftime
from pushbullet import Pushbullet
from flask import Flask
from flask import request


# import os
app = Flask(__name__)


@app.route('/')
def homepage():

    the_time = strftime("%A, %d %b %Y %H:%M")

    checkWebPage()

    return """
    <h1>Oi, aqui é o sadogo</h1>
    <p>Hoje é: {time}.</p>
    <style>
        body{{
            text-align: center;
            background-color: pink;
    }}</style>
    <img src="http://loremflickr.com/600/400/dog" />
    """.format(time=the_time)


def checkWebPage():

    headers = {
        'headers': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    url = "Website" #the website's url 
    pb = Pushbullet("yourpbKey") # used pushbullet to receive notifications on my phone
    r = requests.get(url, headers=headers, timeout=5)

    time = strftime('%X')

    print("\nuser's IP: ", request.environ.get(
        'HTTP_X_REAL_IP', request.remote_addr))

    print(time, r.status_code)
    if r.status_code == 200:
        print("Tudo pronto!")
        # os.system('ntfy -t "SITE UP!!" send "%s"' % url)
        pb.push_note("title", "description") #notify the user


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
