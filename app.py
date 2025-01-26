from flask import Flask

app = Flask(__name__)

#Route (get) https://confere-nf-flask.vercel.app/
@app.route('/')
def home():
    return {
        "success": "true",
        "msg": "This is message is on vercel serve"
    }

#Route (get) https://confere-nf-flask.vercel.app/teste
@app.route('/teste')
def teste():
    return {
        "success": "true",
        "msg": "This is a teste message"
    }

if (__name__ == "__main__"):
    app.run()