from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import uuid

app = Flask(__name__)
api = Api(app)

# Sample shoe data with 15 detailed entries
shoes = [
    {
        "id": str(uuid.uuid4()),
        "name": "Air Max",
        "brand": "Nike",
        "size": 42,
        "color": "Black/White",
        "price": 120,
        "stock": 10,
        "description": "Classic Nike Air Max with cushioned sole for comfort."
    },
    {
        "id": str(uuid.uuid4()),
        "name": "UltraBoost",
        "brand": "Adidas",
        "size": 41,
        "color": "Gray",
        "price": 180,
        "stock": 5,
        "description": "Adidas UltraBoost for maximum running comfort and performance."
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Chuck Taylor All Star",
        "brand": "Converse",
        "size": 40,
        "color": "White",
        "price": 65,
        "stock": 20,
        "description": "Timeless Converse sneakers with high ankle design."
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Gel-Kayano",
        "brand": "ASICS",
        "size": 43,
        "color": "Blue/Orange",
        "price": 160,
        "stock": 8,
        "description": "ASICS Gel-Kayano for stability and support during runs."
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Old Skool",
        "brand": "Vans",
        "size": 39,
        "color": "Black",
        "price": 60,
        "stock": 15,
        "description": "Classic Vans Old Skool with durable suede and canvas uppers."
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Gel-Lyte III",
        "brand": "ASICS",
        "size": 42,
        "color": "Green",
        "price": 120,
        "stock": 7,
        "description": "Retro ASICS Gel-Lyte III with split-tongue design."
    },
    {
        "id": str(uuid.uuid4()),
        "name": "NMD_R1",
        "brand": "Adidas",
        "size": 42,
        "color": "Black/White",
        "price": 140,
        "stock": 9,
        "description": "Adidas NMD with boost cushioning for everyday wear."
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Jordan 1",
        "brand": "Nike",
        "size": 44,
        "color": "Red/Black",
        "price": 200,
        "stock": 4,
        "description": "Iconic Air Jordan 1 with premium leather construction."
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Classic Leather",
        "brand": "Reebok",
        "size": 40,
        "color": "White",
        "price": 75,
        "stock": 12,
        "description": "Reebok Classic Leather shoes for a clean, timeless look."
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Gel-Nimbus 23",
        "brand": "ASICS",
        "size": 43,
        "color": "Blue",
        "price": 150,
        "stock": 6,
        "description": "ASICS Gel-Nimbus for plush cushioning and smooth ride."
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Blazer Mid '77",
        "brand": "Nike",
        "size": 42,
        "color": "White/Black",
        "price": 100,
        "stock": 10,
        "description": "Retro Nike Blazer Mid with classic basketball styling."
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Stan Smith",
        "brand": "Adidas",
        "size": 41,
        "color": "White/Green",
        "price": 85,
        "stock": 18,
        "description": "Adidas Stan Smith with minimalist design and leather upper."
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Slip-On",
        "brand": "Vans",
        "size": 40,
        "color": "Checkerboard",
        "price": 55,
        "stock": 13,
        "description": "Iconic Vans Slip-On with checkerboard pattern."
    },
    {
        "id": str(uuid.uuid4()),
        "name": "ZoomX Vaporfly",
        "brand": "Nike",
        "size": 42,
        "color": "Blue/White",
        "price": 250,
        "stock": 3,
        "description": "Nike ZoomX Vaporfly for elite running performance."
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Continental 80",
        "brand": "Adidas",
        "size": 41,
        "color": "Cream",
        "price": 100,
        "stock": 11,
        "description": "Adidas Continental 80 with retro look and feel."
    }
]

class ShoeList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "success",
            "count": len(shoes),
            "shoes": shoes
        }, 200

    def post(self):
        data = request.get_json()
        new_shoe = {
            "id": str(uuid.uuid4()),
            "name": data.get("name"),
            "brand": data.get("brand"),
            "size": data.get("size"),
            "color": data.get("color"),
            "price": data.get("price"),
            "stock": data.get("stock"),
            "description": data.get("description")
        }
        shoes.append(new_shoe)
        return {"error": False, "message": "Shoe added successfully", "shoe": new_shoe}, 201

class ShoeDetail(Resource):
    def get(self, shoe_id):
        shoe = next((s for s in shoes if s["id"] == shoe_id), None)
        if shoe:
            return {"error": False, "message": "success", "shoe": shoe}, 200
        return {"error": True, "message": "Shoe not found"}, 404

    def put(self, shoe_id):
        shoe = next((s for s in shoes if s["id"] == shoe_id), None)
        if shoe:
            data = request.get_json()
            shoe.update({
                "name": data.get("name", shoe["name"]),
                "brand": data.get("brand", shoe["brand"]),
                "size": data.get("size", shoe["size"]),
                "color": data.get("color", shoe["color"]),
                "price": data.get("price", shoe["price"]),
                "stock": data.get("stock", shoe["stock"]),
                "description": data.get("description", shoe["description"])
            })
            return {"error": False, "message": "Shoe updated successfully", "shoe": shoe}, 200
        return {"error": True, "message": "Shoe not found"}, 404

    def delete(self, shoe_id):
        global shoes
        shoes = [s for s in shoes if s["id"] != shoe_id]
        return {"error": False, "message": "Shoe deleted successfully"}, 200

api.add_resource(ShoeList, '/shoes')
api.add_resource(ShoeDetail, '/shoes/<string:shoe_id>')

if __name__ == '__main__':
    app.run(debug=True)
