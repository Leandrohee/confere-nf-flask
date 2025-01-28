
from flask import Blueprint
from Services.confereFornecedor import confere_fornecedor_service

# Create a Blueprint for this route
confere_fornecedor_bp = Blueprint('confere_fornecedor', __name__)

# https://confere-nf-flask.vercel.app/
@confere_fornecedor_bp.route('/confereFornecedor')
def confereFornecedor():
    return confere_fornecedor_service()