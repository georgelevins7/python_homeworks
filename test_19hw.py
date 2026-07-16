from Step.Homeworks.hw19hw import process_orders
import pytest

def test_product():
    with pytest.raises(ValueError):
        process_orders(
            [
            {"product": "apple", "quantity": 5},
            {"product": "orange", "quantity": 3},
            {"product": "cherry", "quantity": 2}
            ]
            ,
            
            {
            "apple": 9,
            "orange": 20,
            "pineapple": 40
            }
            )
        
def test_quantity():
    with pytest.raises(ValueError):
        process_orders(
            [
                {"product": "apple", "quantity": 9},
            ]
            ,
            {
                "apple": 5
            }
        )

def test_stock():
    orders = [{"product": "apple", "quantity": 9}]
    inventory = {"apple": 12}
    process_orders(orders, inventory)
    assert inventory["apple"] == 3