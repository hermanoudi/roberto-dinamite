from crypt import methods
from flask import Blueprint

from .views import delete_service, index, login, logout, new_service, edit_service, delete_service, auth, create_service, image, update_service

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/login", view_func=login, endpoint="login")
bp.add_url_rule("/auth", view_func=auth, endpoint="auth", methods=["POST",])
bp.add_url_rule("/logout", view_func=logout, endpoint="logout")
bp.add_url_rule("/new_service", view_func=new_service, endpoint="new_service")
bp.add_url_rule("/create_service", view_func=create_service, endpoint="create_service", methods=["POST",])
bp.add_url_rule("/update_service", view_func=update_service, endpoint="update_service", methods=["POST",])
bp.add_url_rule("/edit-service/<int:id>", view_func=edit_service, endpoint="edit_service")
bp.add_url_rule("/delete-service/<int:id>", view_func=delete_service, endpoint="delete_service")
bp.add_url_rule("/uploads/<file_name>", view_func=image, endpoint="image")

# bp.add_url_rule(
#     "/product/<product_id>", view_func=product, endpoint="productview"
# )


def init_app(app):
    app.register_blueprint(bp)
