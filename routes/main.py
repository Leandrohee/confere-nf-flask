from flask import Blueprint

# Create a Blueprint for this route
main_bp = Blueprint('main', __name__)

# https://confere-nf-flask.vercel.app/
@main_bp.route('/')
def confereFornecedor():
    return {
        "success": "true",
        "msg": "Msg for the main route - Teste"
    }