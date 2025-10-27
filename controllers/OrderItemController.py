from flask import jsonify, request
from config.database import get_db
from models.order_item_model import OrderItem
from sqlalchemy.orm import Session

def add_order_item():
    db: Session = next(get_db())
    body = request.json
    oi = OrderItem(
        order_id = body.get("order_id"),
        menu_id = body.get("menu_id"),
        quantity = body.get("quantity"),
        subtotal = body.get("subtotal")
    )
    db.add(oi)
    db.commit()
    return jsonify({"message": "Order item added"})
