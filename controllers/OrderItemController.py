from flask import jsonify, request
from config.database import SessionLocal
from models.order_item_model import OrderItem
from models.order_model import Order

def add_order_item():
    db = SessionLocal()
    try:
        data = request.get_json()
        order_id = data.get("order_id")
        menu_id = data.get("menu_id")
        quantity = data.get("quantity", 1)
        price = data.get("price", 0)

        if not order_id or not menu_id:
            return jsonify({"error": "order_id dan menu_id wajib diisi"}), 400

        subtotal = price * quantity
        new_item = OrderItem(
            order_id=order_id,
            menu_id=menu_id,
            quantity=quantity,
            price=price,
            subtotal=subtotal
        )
        db.add(new_item)

        # 🔹 Update total harga otomatis di tabel orders
        order = db.query(Order).filter(Order.id == order_id).first()
        if order:
            if order.total_price is None:
                order.total_price = 0
            order.total_price += subtotal

        db.commit()
        return jsonify({
            "message": "Item pesanan berhasil ditambahkan",
            "subtotal": subtotal
        }), 201

    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()
