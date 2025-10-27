from flask import jsonify, request
from config.database import get_db
from models.order_model import Order
from models.order_item_model import OrderItem
from sqlalchemy.orm import Session

def add_order():
    db: Session = next(get_db())
    body = request.json
    # expected body: { "customer_name": "...", "total_price": 12345, "items": [ {menu_id, quantity, subtotal}, ... ] }
    new_order = Order(customer_name=body.get("customer_name"), total_price=body.get("total_price"))
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    order_id = new_order.id

    items = body.get("items", [])
    for it in items:
        oi = OrderItem(
            order_id = order_id,
            menu_id = it.get("menu_id"),
            quantity = it.get("quantity"),
            subtotal = it.get("subtotal")
        )
        db.add(oi)
    db.commit()
    return jsonify({"message": "Order created", "order_id": order_id})

def get_all_orders():
    db: Session = next(get_db())
    orders = db.query(Order).order_by(Order.id.desc()).all()
    data = []
    for o in orders:
        data.append({
            "id": o.id,
            "customer_name": o.customer_name,
            "total_price": o.total_price,
            "created_at": o.created_at
        })
    return jsonify(data)
