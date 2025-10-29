# controllers/OrderController.py
from flask import jsonify, request
from config.database import SessionLocal
from models.order_model import Order
from models.order_item_model import OrderItem

def add_order():
    db = SessionLocal()
    try:
        body = request.get_json(force=True) or {}

        customer_name = body.get("customer_name", "User")
        # jika total_price dikirim, gunakan, tapi kalau tidak ada -> hitung dari items
        items = body.get("items", [])

        # compute total from items if provided, else fallback to provided total_price or 0
        if items and isinstance(items, list):
            total_calc = 0.0
            for it in items:
                # cast aman
                qty = int(it.get("quantity", 1))
                subtotal = float(it.get("subtotal", 0))
                total_calc += subtotal
        else:
            total_calc = float(body.get("total_price") or 0)

        # buat order awal dengan total_price = total_calc (lebih aman)
        new_order = Order(customer_name=customer_name, total_price=total_calc)
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        order_id = new_order.id

        # insert items (jika ada)
        for it in items:
            menu_id = it.get("menu_id")
            quantity = int(it.get("quantity", 1))
            subtotal = float(it.get("subtotal", 0))
            # optional: price kalau dikirim
            price = it.get("price", None)
            if price is not None:
                price = float(price)

            oi = OrderItem(
                order_id=order_id,
                menu_id=menu_id,
                quantity=quantity,
                price=price,
                subtotal=subtotal
            )
            db.add(oi)

        db.commit()

        return jsonify({"message": "Order created", "order_id": order_id}), 201

    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()


def get_all_orders():
    db = SessionLocal()
    try:
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
    finally:
        db.close()
