from flask import Flask
app = Flask(__name__)

@app.route('/') 
def test() -> str:
    return 'hi'

app.run()