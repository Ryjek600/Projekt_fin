from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
        <head>
            <title>Hello Page</title>
            <style>
                .center {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    text-align: center;
                    flex-direction: column;
                }
                .button {
                    background-color: #4CAF50; /* Green */
                    border: none;
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    margin: 4px 2px;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <div class="center">
                <button class="button" onclick="window.location.href='http://sp-8.pl/index.php/na-luzie-mainmenu-291/kaway-o-informatykach-mainmenu-294';">Kliknij mnie!</button>
                <p>___________________________________¶¶¶¶<br>
                ________________________¶¶¶¶____¶¶¶¶11¶<br>
                ________________________¶¶1¶¶_¶¶¶¶1111¶<br>
                _______________________¶¶111¶¶¶1111111¶<br>
                ___________________¶¶¶_¶1111¶¶1111111¶<br>
                ___________________¶11¶¶111¶¶111111¶¶<br>
                ___________________¶11¶1111¶111111¶¶<br>
                __________________¶¶11¶111¶111111¶¶<br>
                __________________¶11¶111¶¶111111¶<br>
                __________________¶11¶111¶1111111¶<br>
                _________________¶11¶111¶11111111¶<br>
                _________________¶1¶111¶¶1111111¶¶<br>
                ________________¶1¶¶111¶1111111¶¶<br>
                _______________¶¶1¶111¶1111111¶¶<br>
                _______________¶¶¶111¶11111111¶<br>
                ______________¶¶¶11¶¶111111111¶<br>
                ______________¶¶11¶¶111111¶¶¶1¶¶<br>
                _____________¶11¶¶1111111¶111111¶¶<br>
                ___________¶¶¶¶¶1111111¶¶11111111¶¶¶<br>
                __________¶¶¶1111111¶¶1111111111111¶¶¶<br>
                _________¶¶111111¶¶¶11111111111111111¶¶¶¶<br>
                _________¶111111¶¶1111111111111111111111¶¶¶<br>
                _________¶111111¶1111111111¶¶¶1111111111111¶<br>
                ________¶11111111111111111¶¶_¶¶¶¶¶¶¶¶111111¶<br>
                _______¶¶111111111111111¶¶¶________¶111111¶¶<br>
                _______¶11111111111¶¶¶¶¶¶__________¶111111¶<br>
                ______¶¶11111111111¶¶_____________¶¶11111¶¶<br>
                ______¶111111111111¶______________¶¶11111¶<br>
                _____¶¶111111111111¶________________¶¶¶¶¶¶¶¶¶¶¶<br>
                _____¶1111111111111¶________________¶¶¶111111¶¶¶¶<br>
                _____¶1111111111111¶¶_____________¶¶¶111111¶¶¶11¶<br>
                ____¶¶1111111111111¶¶¶_________¶¶¶1111111¶¶11111¶<br>
                ____¶1111111111111111¶¶¶¶¶¶¶¶¶¶¶111111111¶1111¶¶<br>
                ____¶111111111111111111¶¶¶¶11111111111111¶¶¶¶¶¶<br>
                ___¶111111111111111111111111111111111111111¶¶¶<br>
                __¶111111111111111111111111111111111111111¶¶<br>
                ¶¶11111111111111111111111111111111111111¶¶¶<br>
                111111111111111111111111111111111¶¶¶¶¶¶¶¶<br>
                111111111111111111111111111111¶¶¶¶<br>
                1111111111111111111111111111¶¶¶<br>
                111111111111111111111111111¶¶<br>
                1111111111111111111111111¶¶<br>
                111111111111111111111111¶¶<br>
                1111111111111111111111¶¶<br>
                111111111111111111¶¶¶¶<br>
                111111111¶¶¶¶¶¶¶¶¶¶<br>
                111111¶¶¶<br>
                ¶¶¶¶¶¶¶
                </p>
            </div>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')


