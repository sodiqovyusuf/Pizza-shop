class Pizza:
    def __init__(self):
        self.orders = []
        self.order_id = 0
        self.revenue = 0

    def order(self, customer_name, pizza_type, quantity):
        pizza_types = {'margarita': 10, 'vegetable': 12, 'chicken': 15}

        if pizza_type in pizza_types:
            self.orders.append({'customer': customer_name, 'pizza type': pizza_type,
                                'pizza quantity': str(quantity), 'order id': self.order_id})
            print(f"{quantity} {pizza_type} pizza order from {customer_name} was successful!")

            if pizza_type == 'margarita':
                print(f"Total price is {quantity * 10}$")
                self.revenue += quantity * 10
            if pizza_type == 'vegetable':
                print(f"Total price is {quantity * 15}$")
                self.revenue += quantity * 15
            if pizza_type == 'chicken':
                print(f"Total price is {quantity * 12}$")
                self.revenue += quantity * 12

            self.order_id += 1
            print("Your order id is " + str(self.order_id) + ", please wait for the queue.")

        else:
            print(f"{pizza_type} pizza type not found.")
        print()

    def listOrders(self):
        for order_details in self.orders:
            print(order_details)
        print()

    def calculateRevenue(self):
        print(f"Total revenue for all orders is {self.revenue}$")
        print()

    def cancelOrder(self, order_id):
        for order in self.orders:
            if order['order id'] == order_id:
                print(f"Order {order_id} canceled.")
                self.orders.remove(order)
            else:
                print(f"Sorry order {order_id} not found.")


pizza = Pizza()
pizza.order("Yusuf", "margarita", 4)
pizza.order("Orash", "chicken", 1)
pizza.order("Nasim", "peperoni", 5)
pizza.listOrders()
pizza.calculateRevenue()
pizza.cancelOrder(0)
print()
pizza.listOrders()
pizza.cancelOrder(3)
