class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.order_history = []

    def add_order(self, order):
        self.order_history.append(order)

    def view_order_history(self):
        print(f"Ім'я клієнта: {self.name}, Контактна інформація: {self.contact_info}")
        for order in self.order_history:
            print(f"Order ID: {order.id}, Items: {order.items}, Status: {order.status}, Доставка: {order.delivery.address}, Кур'єр: {order.delivery.courier_name}, Час доставки: {order.delivery.delivery_time}")


class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def get_items(self):
        return self.items


class Order:
    def __init__(self, customer, items, delivery):
        self.id = id(self) # Unique ID for each order
        self.customer = customer
        self.items = items
        self.delivery = delivery
        self.status = "Pending"

    def validate_items(self, menu):
        for item in self.items:
            if item not in menu.get_items():
                return False
        return True

    def validate_quantity(self, max_items=10):
        return len(self.items) <= max_items

    def confirm_order(self, menu):
        if not self.validate_items(menu) or not self.validate_quantity():
            return False
        self.status = "Confirmed"
        return True

    def view_order_details(self):
        print(f"Order ID: {self.id}, Items: {self.items}, Delivery: {self.delivery.address}, Кур'єр: {self.delivery.courier_name}, Час доставки: {self.delivery.delivery_time}, Статус: {self.status}")


class Delivery:
    def __init__(self, address, courier_name, delivery_time):
        self.address = address
        self.courier_name = courier_name
        self.delivery_time = delivery_time


# Глобальна змінна для зберігання поточного клієнта
current_customer = None

# Глобальна змінна для зберігання меню
menu = Menu()

# Глобальна змінна для відслідковування, чи вже користувач бачив меню
menu_shown = False

def register_customer():
    global current_customer
    name = input("Введіть ім'я: ")
    contact_info = input("Введіть контактну інформацію: ")
    current_customer = Customer(name, contact_info)
    print(f"Клієнт {name} зареєстрований.")

def view_menu():
    menu.add_item("Суп", 10)
    menu.add_item("Стейк", 20)
    print("Меню:")
    for item, price in menu.get_items().items():
        print(f"{item}: {price} грн")

def add_to_cart():
    global current_customer
    if current_customer is None:
        print("Спершу зареєструйтеся.")
        return
    items = input("Введіть назви страв через кому: ").split(',')
    delivery = Delivery("Вул. Прикладна, 10", "Іван", "15:00")
    order = Order(current_customer, items, delivery)
    if order.confirm_order(menu):
        print("Страви додано в кошик.")
        current_customer.add_order(order)
    else:
        print("Не вдалося додати страви в кошик.")

def place_order():
    global current_customer
    if current_customer is None or not current_customer.order_history:
        print("В кошику немає замовлень.")
        return
    last_order = current_customer.order_history[-1]
    last_order.view_order_details()
    print("Замовлення оформлено.")


def main_menu():
    global current_customer, menu_shown
    while True:
        if not menu_shown:
            print("1. Реєстрація клієнта")
            print("2. Перегляд меню")
            print("3. Вибір страв в кошик покупок")
            print("4. Оформлення замовлення")
            print("5. Вихід")
            print("")
            menu_shown = True
        selection = input("Введіть номер дії: ")

        if selection == "1":
            register_customer()
        elif selection == "2":
            view_menu()
        elif selection == "3":
            add_to_cart()
        elif selection == "4":
            place_order()
        elif selection == "5":
            print("Дякуємо за використання!")
            # Повернення до головного меню
            return
        else:
            print("Невірний вибір. Спробуйте знову.")
            print("")

if __name__ == "__main__":
    while True:
        main_menu()

