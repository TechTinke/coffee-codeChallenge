from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

c1.create_order(coffee1, 4.0)
c1.create_order(coffee2, 6.5)
c2.create_order(coffee1, 3.5)

print(f"{coffee1.name} has {coffee1.num_orders()} orders.")
print(f"Alice's coffees: {[c.name for c in c1.coffees()]}")
print(f"Most aficionado of {coffee1.name}: {Customer.most_aficionado(coffee1).name}")
