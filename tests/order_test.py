import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_attributes():
    c = Customer("Eli")
    cf = Coffee("Mocha")
    o = Order(c, cf, 6.0)
    assert o.customer == c
    assert o.coffee == cf
    assert o.price == 6.0
