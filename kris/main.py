class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.order_history = []

    def add_order(self, order):
        self.order_history.append(order)

    def update_order(self, order_id, new_order):
        for i, order in enumerate(self.order_history):
            if order.id == order_id:
                self.order_history[i] = new_order
                return True
        return False

    def cancel_order(self, order_id):
        for i, order in enumerate(self.order_history):
            if order.id == order_id:
                del self.order_history[i]
                return True
        return False

    def view_order_history(self):
        print(f"Ім'я клієнта: {self.name}, Контактна інформація: {self.contact_info}")
        for order in self.order_history:
            print(f"Номер замовлення: {order.id}, Страви: {order.items}, Статус замовлення: {order.status}, Доставка: {order.delivery.address}, Кур'єр: {order.delivery.courier_name}, Час доставки: {order.delivery.delivery_time}")


class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def get_item(self, name):
        return self.items.get(name)

    def get_items(self):
        return self.items


class Order:
    def __init__(self, customer, items, delivery):
        self.id = id(self) # Unique ID for each order
        self.customer = customer
        self.items = items
        self.delivery = delivery
        self.status = "В очікуванні"

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
        self.status = "Підтверджено"
        return True

    def view_order_details(self):
        print(f"Номер замовлення: {self.id}, Страви: {self.items}, Доставка: {self.delivery.address}, Кур'єр: {self.delivery.courier_name}, Час доставки: {self.delivery.delivery_time}, Статус: {self.status}")


class Delivery:
    def __init__(self, address, courier_name, delivery_time):
        self.address = address
        self.courier_name = courier_name
        self.delivery_time = delivery_time



menu = Menu()
menu.add_item("Суп", 10)
menu.add_item("Стейк", 20)


customer = Customer("Христина", "Телефон: 123456789")


order = Order(customer, ["Суп", "Стейк"], Delivery("Вул. Коновальця, 34", "Андрій", "15:00"))


if order.confirm_order(menu):
    print("Замовлення підтверджено.")
    order.view_order_details()
else:
    print("Замовлення не підтверджено.")

new_order = Order(customer, ["Піца", "Кола"], Delivery("Вул. Коновальця, 34", "Андрій", "16:00"))
customer.add_order(new_order)


customer.view_order_history()
