# =================================================================
# 1-TALAB: FRUIT KLASSI
# Atributlar: title, price, quantity
# Metodlar: Barcha atributlarni ko'rish (get) va o'zgartirish (set)
# =================================================================

# class Fruit:
#     def __init__(self, title: str, price: float, quantity: int):
#         # Atributlarni himoyalangan (protected) qilib belgilaymiz
#         self._title = title
#         self._price = price
#         self._quantity = quantity
#
#     # --- ATRIBUTLARNI KO'RISH (GETTER) METODLARI ---
#
#     def get_info(self):
#         """Barcha atributlarni ko'rsatish metodi."""
#         return {
#             "title": self._title,
#             "price": self._price,
#             "quantity": self._quantity
#         }

    # --- ATRIBUTLARNI O'ZGARTIRISH (SETTER) METODLARI ---

    # def set_title(self, new_title: str):
    #     """Mevalarning nomini o'zgartirish."""
    #     self._title = new_title
    #     print(f"✅ Nomi o'zgartirildi: {new_title}")
    #
    # def set_price(self, new_price: float):
    #     """Narxni o'zgartirish."""
    #     if new_price >= 0:
    #         self._price = new_price
    #         print(f"✅ Narx o'zgartirildi: {new_price}")
    #     else:
    #         print("❌ Xato: Narx manfiy bo'lishi mumkin emas.")
    #
    # def set_quantity(self, new_quantity: int):
    #     """Miqdorni o'zgartirish."""
    #     if isinstance(new_quantity, int) and new_quantity >= 0:
    #         self._quantity = new_quantity
    #         print(f"✅ Miqdor o'zgartirildi: {new_quantity}")
    #     else:
    #         print("❌ Xato: Miqdor butun son bo'lishi kerak.")


# =================================================================
# 2-TALAB: COMPANY KLASSI (SHIRINLIK ISHLAB CHIQARUVCHI)
# Atributlar: title, tarkibi (list), quantity (int), price (int)
# =================================================================

class Company:
    def __init__(self, title: str, tarkibi: list, quantity: int, price: int):
        # Talab qilingan turdagi tekshiruvlar (type checks)
        if not isinstance(tarkibi, list):
            raise TypeError("Tarkibi (ingredients) list turida bo'lishi kerak.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity (miqdor) butun son (int) bo'lishi kerak.")
        if not isinstance(price, int):
            raise TypeError("Price (narx) butun son (int) bo'lishi kerak.")

        self.title = title
        self.tarkibi = tarkibi
        self.quantity = quantity
        self.price = price

shirinlik=Company('napalyon',10,15000)
print(shirinlik)

    # def get_info(self):
    #     """Kompaniya mahsuloti haqida ma'lumot."""
    #     tarkib_str = ", ".join(self.tarkibi)
    #     return (f"\n--- Kompaniya Mahsuloti ---\n"
    #             f"Nomi: {self.title}\n"
    #             f"Tarkibi: {tarkib_str}\n"
    #             f"Miqdori: {self.quantity} dona\n"
    #             f"Narxi: {self.price} so'm")
    #

# =================================================================
# KODNI SINAB KO'RISH (DEMONSTRATSIYA)
# =================================================================

# print("--- 1. FRUIT KLASSINI SINASH ---")
# # Fruit obyektini yaratish
# apple = Fruit(title="Olma", price=1.5, quantity=100)
# print("Boshlang'ich holat:", apple.get_info())
#
# # Atributlarni o'zgartirish (Setters)
# apple.set_price(2.0)
# apple.set_quantity(50)
# apple.set_title("Qizil Olma")

# O'zgartirishdan keyingi holatni ko'rish (Getters)
# print("O'zgartirilgan holat:", apple.get_info())
#
# print("\n--- 2. COMPANY KLASSINI SINASH ---")
# # Company obyektini yaratish
# sweet_product = Company(
#     title="Shokolad Bar",
#     tarkibi=["kakao", "shakar", "sut", "yong'oq"],
#     quantity=500,
#     price=15000
# )

# Ma'lumotni ko'rish
# print(sweet_product.get_info())

# Agar noto'g'ri turdagi ma'lumot berilsa (masalan, quantity float bo'lsa)
# try:
#     bad_product = Company(
#         title="Jelly",
#         tarkibi=["jelatin", "shakar"],
#         quantity=10.5,  # Xato: int bo'lishi kerak
#         price=5000
#     )
# except TypeError as e:
#     print(f"\n❌ Kompaniya obyektini yaratishda xato yuz berdi: {e}")
