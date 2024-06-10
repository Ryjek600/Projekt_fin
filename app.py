from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
        <head>
            <title>Hello Page</title>
        </head>
        <body>
            <button onclick="window.location.href='http://sp-8.pl/index.php/na-luzie-mainmenu-291/kaway-o-informatykach-mainmenu-294';">Kliknij mnie!</button>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')
