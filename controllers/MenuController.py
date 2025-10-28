from flask import jsonify, request
from config.database import get_db
from models.menu_model import Menu
from sqlalchemy.orm import Session

from flask import request, jsonify
from models.menu_model import Menu
from config.database import db

def get_all_menus():
    try:
        search = request.args.get('search')
        category = request.args.get('category')

        query = db.query(Menu)

        # Jika ada parameter search
        if search:
            query = query.filter(Menu.name.ilike(f"%{search}%"))

        # Jika ada parameter kategori
        if category:
            query = query.filter(Menu.category.ilike(f"%{category}%"))

        menus = query.all()
        result = [
            {
                "id": menu.id,
                "name": menu.name,
                "description": menu.description,
                "price": menu.price,
                "category": menu.category,
                "image_url": menu.image_url,
            }
            for menu in menus
        ]

        return jsonify(result)
    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"error": str(e)}), 500


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
