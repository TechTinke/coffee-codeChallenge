import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_orders_and_avg():
    c = Customer("Liam")
    cf = Coffee("Latte")
    c.create_order(cf, 3.0)
    c.create_order(cf, 7.0)
    assert cf.num_orders() == 2
    assert cf.average_price() == 5.0
