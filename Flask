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
            <button onclick="window.location.href='https://www.gry-online.pl/S043.asp?ID=11674285';">Kliknij mnie!</button>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')
