from flask import jsonify, request
from config.database import get_db
from models.menu_model import Menu
from sqlalchemy.orm import Session


def get_all_menus():
    db = get_db()
    query = db.query(Menu)

    # 🔍 Ambil parameter search dan category dari query string
    search = request.args.get("search")
    category = request.args.get("category")

    if search:
        query = query.filter(Menu.name.ilike(f"%{search}%") | Menu.description.ilike(f"%{search}%"))

    if category:
        query = query.filter(Menu.category.ilike(f"%{category}%"))

    menus = query.order_by(Menu.id.desc()).all()

    result = []
    for menu in menus:
        result.append({
            "id": menu.id,
            "name": menu.name,
            "price": menu.price,
            "category": menu.category,
            "description": menu.description,
            "image_url": menu.image_url
        })

    return jsonify(result), 200


def add_menu():
    db = get_db()
    data = request.get_json()

    # Pastikan menerima dictionary, bukan list
    if isinstance(data, list):
        return jsonify({"error": "Body request harus berupa JSON object, bukan list"}), 400

    new_menu = Menu(
        name=data.get("name"),
        price=data.get("price"),
        category=data.get("category"),
        description=data.get("description"),
        image_url=data.get("image_url")
    )

    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)

    return jsonify({
        "id": new_menu.id,
        "name": new_menu.name,
        "price": new_menu.price,
        "category": new_menu.category,
        "description": new_menu.description,
        "image_url": new_menu.image_url
    }), 201


def get_menu(id):
    db: Session = next(get_db())
    m = db.query(Menu).get(id)
    if not m:
        return jsonify({"message": "Menu not found"}), 404
    return jsonify({
        "id": m.id,
        "name": m.name,
        "price": m.price,
        "category": m.category,
        "description": m.description,
        "image_url": m.image_url
    })

def add_menu():
    db = next(get_db())
    body = request.json
    new = Menu(
        name = body.get("name"),
        price = body.get("price"),
        category = body.get("category"),
        description = body.get("description"),
        image_url = body.get("image_url")
    )
    db.add(new)
    db.commit()
    db.refresh(new)
    return jsonify({"message": "Menu added", "id": new.id})

def update_menu(id):
    db = next(get_db())
    m = db.query(Menu).get(id)
    if not m:
        return jsonify({"message": "Menu not found"}), 404
    body = request.json
    m.name = body.get("name", m.name)
    m.price = body.get("price", m.price)
    m.category = body.get("category", m.category)
    m.description = body.get("description", m.description)
    m.image_url = body.get("image_url", m.image_url)
    db.commit()
    db.refresh(m)
    return jsonify({"message": "Menu updated", "id": m.id})

def delete_menu(id):
    db = next(get_db())
    m = db.query(Menu).get(id)
    if not m:
        return jsonify({"message": "Menu not found"}), 404
    db.delete(m)
    db.commit()
    return jsonify({"message": "Menu deleted"})
