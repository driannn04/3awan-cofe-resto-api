from flask import Blueprint
from controllers.MenuController import *
from controllers.OrderController import *
from controllers.OrderItemController import *

web = Blueprint("web", __name__)

# Menus
web.route("/api/menus", methods=["GET"])(get_all_menus)
web.route("/api/menus/<int:id>", methods=["GET"])(get_menu)
web.route("/api/menus", methods=["POST"])(add_menu)
web.route("/api/menus/<int:id>", methods=["PUT"])(update_menu)
web.route("/api/menus/<int:id>", methods=["DELETE"])(delete_menu)

# Orders
web.route("/api/orders", methods=["GET"])(get_all_orders) 
web.route("/api/orders", methods=["POST"])(add_order)

# Order items
web.route("/api/order-items", methods=["POST"])(add_order_item)
