class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }


class FoodItem(Product):
    def __init__(self, id, name, price, quantity, expiry_date=None, weight_kg=None):
        super().__init__(id, name, price, quantity)
        self.expiry_date = expiry_date
        self.weight_kg = weight_kg

    def to_dict(self):
        d = super().to_dict()
        d["expiry_date"] = self.expiry_date
        d["weight_kg"] = self.weight_kg
        return d


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.id] = item

    def remove_item(self, item_id):
        del self.items[item_id]

    def update_item(self, item_id, **fields):
        item = self.items[item_id]
        for k, v in fields.items():
            setattr(item, k, v)

    def list_items(self):
        return [it.to_dict() for it in self.items.values()]


import uuid
inv = Inventory()

while True:
    print("\n1. Qo'shish\n2. O'chirish\n3. O'zgartirish\n4. Ko'rish\n5. Chiqish")
    cmd = input("Tanlang: ")

    if cmd == "1":
        idd = str(uuid.uuid4())[:8]
        name = input("Nomi: ")
        price = float(input("Narxi: "))
        qty = int(input("Soni: "))
        expiry = input("Yaroqlilik muddati (bo'sh bo'lsa enter): ")
        weight = input("Vazn kg (bo'sh bo'lsa enter): ")
        expiry = expiry if expiry else None
        weight = float(weight) if weight else None
        item = FoodItem(idd, name, price, qty, expiry, weight)
        inv.add_item(item)
        print("Qo'shildi.")

    elif cmd == "2":
        rid = input("ID: ")
        inv.remove_item(rid)
        print("O'chirildi.")

    elif cmd == "3":
        uid = input("ID: ")
        field = input("Qaysi maydon (name, price, quantity): ")
        value = input("Yangi qiymat: ")
        if field in ["price", "quantity"]:
            value = float(value) if field == "price" else int(value)
        inv.update_item(uid, **{field: value})
        print("Yangilandi.")

    elif cmd == "4":
        print(inv.list_items())

    elif cmd == "5":
        break

    else:
        print("Noto‘g‘ri buyruq.")
