# class Markt:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.my_dii = {}
#
#     def add_items(self):
#         print("Mahsulot qo'shish (to'xtash uchun 'stop' deb yozing)")
#         while True:
#             name_itm = input("nima mahsulot: ").strip()
#
#             if name_itm.lower() == "stop":
#                 print("Qo'shish tugadi!\n")
#                 break
#
#             if name_itm == "":
#                 print("Iltimos, mahsulot nomini kiriting!\n")
#                 continue
#
#             try:
#                 price = int(input("narxi: "))
#             except:
#                 print("Narx faqat raqam bo'lishi kerak!\n")
#                 continue
#
#             self.my_dii[name_itm] = price
#             print(f"{name_itm} — {price} so'm qo'shildi!\n")
#
#     def show_itm(self):
#         if not self.my_dii:
#             print("Hozircha hech qanday mahsulot yo'q!\n")
#             return
#
#         print("\n          DO'KONDA BOR MAHSULOTLAR")
#         for nom, narx in self.my_dii.items():
#             print(f"{nom:<20} — {narx:>10} so'm")
#
#     def edit_item(self):
#         if not self.my_dii:
#             print("Do'kon bo'sh! O'zgartiradigan narsa yo'q.\n")
#             return
#
#         print("Hozirgi mahsulotlar:")
#         for i, j in self.my_dii.items():
#             print(f"{i} — {j} so'm")
#
#         s = input('\nQaysi mahsulotni o\'zgartirmoqchisiz? Ismini kiriting: ').strip()
#         if s not in self.my_dii:
#             print("Bunday mahsulot topilmadi!\n")
#             return
#
#         b = input('Yangi ismini kiriting (bo\'sh qoldirsangiz o\'zgarmaydi): ').strip()
#         try:
#             c_input = input('Yangi narxni kiriting (bo\'sh qoldirsangiz o\'zgarmaydi): ').strip()
#             if c_input == "":
#                 c = self.my_dii[s]
#             else:
#                 c = int(c_input)
#         except ValueError:
#             print("Narx raqam bo'lishi kerak!\n")
#             return
#
#         if b != "" and b != s:
#             self.my_dii[b] = self.my_dii.pop(s)
#             print(f"{s} → {b} ga o'zgartirildi! Narxi: {c} so'm\n")
#         else:
#             # Faqat narx o'zgaradi
#             self.my_dii[s] = c
#             print(f"{s} narxi {c} so'm ga yangilandi!\n")
#
#     def delete_item(self):
#         if not self.my_dii:
#             print("O'chiradigan mahsulot yo'q!\n")
#             return
#
#         self.show_itm()
#         ochir = input("Qaysi mahsulotni o'chirmoqchisiz? (nomini yozing): ").strip()
#
#         if ochir in self.my_dii:
#             del self.my_dii[ochir]
#             print(f"{ochir} muvaffaqiyatli o'chirildi!\n")
#         else:
#             print("Bunday mahsulot topilmadi!\n")
#
#
# dokon = Markt("Vali", 28)
#
# while True:
#     print("1. Mahsulot qo'shish")
#     print("2. Barcha mahsulotlarni ko'rish")
#     print("3. Mahsulot o'chirish")
#     print("5. Mahsulotni o'zgartirish (edit)")
#     print("4. Chiqish")
#     tanlov = input("Tanlang (1-5): ")
#
#     if tanlov == "1":
#         dokon.add_items()
#     elif tanlov == "2":
#         dokon.show_itm()
#     elif tanlov == "3":
#         dokon.delete_item()
#     elif tanlov == "5":
#         dokon.edit_item()
#     elif tanlov == "4":
#         print("Xayr! Do'kon yopildi.")
#         break
#     else:
#         print("Noto'g'ri tanlov!\n")

class Cmcmeneger:
    def __init__(self, phone_numbers:list, smss:list, my_number:list, from_to:dict):
        self.phone_numbers = phone_numbers
        self.smss = smss
        self.my_number = my_number
        self.from_to = from_to

    def my_num(self):
        a = input('input our phone number ')
        self.my_number.append(a)
        self.phone_numbers.append(a)
    def check_my_number(self):
        print(self.my_number)
    def add_num(self):
        a = input('input our phone number ')
        self.phone_numbers.append(a)
    def show_num(self):
        print(self.phone_numbers)
    def send_message(self):
        print(f'qaysi nomerga\n{self.phone_numbers}')
        a = input('nomerni kiriting')
        b = input('habarni kiriting')
        self.from_to[a] = b
class Cmcmeneger:
    def __init__(self, phone_numbers:list, smss:list, my_number:list, from_to:dict):
        self.phone_numbers = phone_numbers
        self.smss = smss
        self.my_number = my_number
        self.from_to = from_to

    def my_num(self):
        a = input('Bizning nomerni kiriting: ')
        self.my_number.append(a)
        self.phone_numbers.append(a)

    def check_my_number(self):
        print("Mening nomerlarim:", self.my_number)

    def add_num(self):
        a = input('Yangi nomer kiriting: ')
        self.phone_numbers.append(a)

    def show_num(self):
        print("Barcha nomerlar:", self.phone_numbers)

    def send_message(self):
        print(f"Qaysi nomerga yuborasiz?\n{self.phone_numbers}")
        a = input('Nomer: ')
        b = input('Habar: ')
        self.from_to[a] = b
        print("Xabar yuborildi!")

# Obyekt yaratamiz
manager = Cmcmeneger([], [], [], {})

while True:
    print("""
1. O'zimga nomer qo'shish
2. Nomerimni ko'rish
3. Umumiy nomer qo'shish
4. Barcha nomerlarni ko'rish
5. Habat yuborish
6. Chiqish
""")

    s = int(input('Tanlang: '))

    if s == 1:
        manager.my_num()
    elif s == 2:
        manager.check_my_number()
    elif s == 3:
        manager.add_num()
    elif s == 4:
        manager.show_num()
    elif s == 5:
        manager.send_message()
    elif s == 6:
        print("Dastur tugadi!")
        break
    else:
        print("Noto'g'ri tanlov!")
