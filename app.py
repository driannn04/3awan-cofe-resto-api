from flask import Flask
from flask_cors import CORS
from config.database import engine, Base
from routes.web import web
import models.menu_model, models.order_model, models.order_item_model

app = Flask(__name__)
CORS(app)

# Buat tabel otomatis
Base.metadata.create_all(bind=engine)

# Register route
app.register_blueprint(web)

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    print("="*50)
    print("🚀  3awan-caferesto-api is running!")
    print(f"📡  Akses di: http://127.0.0.1:{port}")
    print("="*50)
    app.run(debug=True, host=host, port=port)
