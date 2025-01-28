from flask import Flask
from routes.confereFornecedor import confere_fornecedor_bp 
from routes.main import main_bp 

app = Flask(__name__)

# Register Blueprints from my server
app.register_blueprint(confere_fornecedor_bp)                   # /confereFornecedor
app.register_blueprint(main_bp)                                 # /

#Starting the server
if (__name__ == "__main__"):
    app.run()