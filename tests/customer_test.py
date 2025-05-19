import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name():
    c = Customer("Oscar")
    assert c.name == "Oscar"
    try:
        c.name = "ThisIsWayTooLongForName"
    except ValueError:
        assert True

def test_customer_orders_and_coffees():
    c = Customer("Anna")
    cf = Coffee("Espresso")
    c.create_order(cf, 5.0)
    assert cf in c.coffees()
