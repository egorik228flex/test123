class Product:
    def __init__(self, name, price, description, chislo=1, rating=0):
        self.name = name
        self.description = description
        self.price = price
        self.chislo = chislo
        self.rating = rating

    def display_info(self):
        return f"Товар: {self.name}, Цена: {self.price}₽, Описание: {self.description}, Рейтинг: {self.rating}"


class Cart:
    def __init__(self):
        self.products = []
        self.total_price = 0.0

    def add_product(self, product, chislo=1):
        if product.chislo >= chislo:
            self.products.append((product, chislo))
            self.total_price += product.price * chislo
            print(f"Добавлено: {product.name} x{chislo}")
        else:
            print("Недостаточно товара на складе")

    def display_products(self):
        if not self.products:
            print("Корзина пуста")
        else:
            for product, chislo in self.products:
                print(f"{product.name} x{chislo} = {product.price * chislo}₽")
            print(f"Итого: {self.total_price}₽")

    def delete_product(self, product_name):
        for i, (product, chislo) in enumerate(self.products):
            if product.name == product_name:
                self.total_price -= product.price * chislo
                del self.products[i]
                print("Товар удалён из корзины")
                return
        print("Товар не найден в корзине")


class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def checkout(self, cart):
        if cart.total_price > self.balance:
            print("Недостаточно средств")
        else:
            for product, chislo in cart.products:
                product.chislo -= chislo
            self.balance -= cart.total_price
            print(f"Покупка завершена. Остаток: {self.balance}₽")
            cart.products = []
            cart.total_price = 0.0

    def display_info(self):
        print(f"Покупатель: {self.name}, Баланс: {self.balance}₽")


class TovarTexnica(Product):
    def __init__(self, name, price, description, iron, chislo=1, rating=0):
        super().__init__(name, price, description, chislo, rating)
        self.iron = iron

    def display_info(self):
        return f"{super().display_info()}, Характеристика: {self.iron}"


class Sale:
    def get_final_price(self, price):
        discount = 30
        final_price = price * (1 - discount / 100)
        return round(final_price, 2)


# Товары
car = TovarTexnica("Белая машина", 132000, "Легковая машина", "50hp", chislo=3, rating=4.6)
notebook = TovarTexnica("Ноутбук ASUS", 50000, "Игровой ноутбук", "RTX 4070Ti", chislo=5, rating=4.9)
phone = TovarTexnica("Huawei P60 Pro", 18990, "Камерафон", "Snapdragon 8+ Gen1", chislo=10, rating=4.7)

# Применим скидки
sale = Sale()
car.price = sale.get_final_price(car.price)
notebook.price = sale.get_final_price(notebook.price)
phone.price = sale.get_final_price(phone.price)

products = [car, notebook, phone]

# Меню магазина
def show_menu():
    print("\n=== МЕНЮ МАГАЗИНА ===")
    print("1. Показать все товары")
    print("2. Отсортировать по цене (дешевые первыми)")
    print("3. Отсортировать по цене (дорогие первыми)")
    print("4. Отсортировать по рейтингу")
    print("5. Добавить товар в корзину")
    print("6. Показать корзину")
    print("7. Удалить товар из корзины")
    print("8. Оплатить покупки")
    print("9. Показать информацию о клиенте")
    print("0. Выход")


# Инициализация
cart = Cart()
client = Client("Андрей", 200000)

while True:
    show_menu()
    choice = input("Выберите действие: ")

    if choice == "1":
        for p in products:
            print(p.display_info())

    elif choice == "2":
        for p in sorted(products, key=lambda x: x.price):
            print(p.display_info())

    elif choice == "3":
        for p in sorted(products, key=lambda x: x.price, reverse=True):
            print(p.display_info())

    elif choice == "4":
        for p in sorted(products, key=lambda x: x.rating, reverse=True):
            print(p.display_info())

    elif choice == "5":
        for i, p in enumerate(products):
            print(f"{i + 1}. {p.name}")
        idx = int(input("Введите номер товара: ")) - 1
        chislo = int(input("Сколько штук добавить: "))
        if 0 <= idx < len(products):
            cart.add_product(products[idx], chislo)

    elif choice == "6":
        cart.display_products()

    elif choice == "7":
        name = input("Введите название товара для удаления: ")
        cart.delete_product(name)

    elif choice == "8":
        client.checkout(cart)

    elif choice == "9":
        client.display_info()

    elif choice == "0":
        print("До свидания!")
        break

    else:
        print("Неверный ввод")
