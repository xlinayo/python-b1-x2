from bills import *
import pytest
from util_package.bill_manager import BillManager

def test_create_bills_EX101():
    bill_manager = BillManager()
    bills = bill_manager.create_bills_EX101()
    statistics = Statistics(bills)
    top_product = statistics.find_top_sell_product()
    assert top_product[0].product_id == "P701", "Check the function: find_top_sell_product"
    assert top_product[1] == 1, "Check the function: find_top_sell_product"
    list_sellers = statistics.find_top_two_sellers()
    assert list_sellers[0].dni == "S501", "Check the function: find_top_two_sellers"
    assert len(list_sellers) == 1, "Check the function: find_top_two_sellers"
    tuple_buyer = statistics.find_buyer_lowest_total_purchases()
    assert tuple_buyer[0].dni == "B101", "Check the function: find_buyer_lowest_total_purchases"
    assert tuple_buyer[1] == 162.5, "CCheck the function: find_buyer_lowest_total_purchases"
    list_products = statistics.order_products_by_tax(order_type=OrderType.ASC)
    assert list_products[0][0].product_id == "P701", "Check the function: order_products_by_tax"
    assert len(list_products) == 1, "Check the function: order_products_by_tax"
    

def test_create_bills_EX102():
    bill_manager = BillManager()
    bills = bill_manager.create_bills_EX102()
    statistics = Statistics(bills)
    top_product = statistics.find_top_sell_product()
    assert top_product[0].product_id == "P702", "Check the function: find_top_sell_product"
    assert top_product[1] == 1, "Check the function: find_top_sell_product"
    list_sellers = statistics.find_top_two_sellers()
    assert list_sellers[0].dni == "S501", "Check the function: find_top_two_sellers"
    assert len(list_sellers) == 1, "Check the function: find_top_two_sellers"
    tuple_buyer = statistics.find_buyer_lowest_total_purchases()
    assert tuple_buyer[0].dni == "B101", "Check find_buyer_lowest_total_purchases"
    assert tuple_buyer[1] == 498.28, "Check find_buyer_lowest_total_purchases" 
    list_products = statistics.order_products_by_tax(order_type=OrderType.ASC)
    assert list_products[0][0].product_id == "P702", "Check the function: order_products_by_tax"
    assert len(list_products) == 2, "Check the function: order_products_by_tax"


def test_create_bills_EX103():
    bill_manager = BillManager()
    bills = bill_manager.create_bills_EX103()
    statistics = Statistics(bills)
    top_product = statistics.find_top_sell_product()
    assert top_product[0].product_id == "P701", "Check the function: find_top_sell_product"
    assert top_product[1] == 1, "Check the function: find_top_sell_product"
    list_sellers = statistics.find_top_two_sellers()
    assert list_sellers[0].dni == "S501", "Check the function: find_top_two_sellers"
    assert len(list_sellers) == 1, "Check the function: find_top_two_sellers"
    tuple_buyer = statistics.find_buyer_lowest_total_purchases()
    assert tuple_buyer[0].dni == "B102", "Check find_buyer_lowest_total_purchases"
    assert tuple_buyer[1] == 78.28, "Check find_buyer_lowest_total_purchases" 
    list_products = statistics.order_products_by_tax(order_type=OrderType.ASC)
    assert list_products[0][0].product_id == "P702", "Check the function: order_products_by_tax"
    assert len(list_products) == 2, "Check the function: order_products_by_tax"

def test_create_bills_EX104():
    bill_manager = BillManager()
    bills = bill_manager.create_bills_EX104()
    statistics = Statistics(bills)
    top_product = statistics.find_top_sell_product()
    assert top_product[0].product_id == "P704", "Check the function: find_top_sell_product"
    assert top_product[1] == 6, "Check the function: find_top_sell_product"
    list_sellers = statistics.find_top_two_sellers()
    assert len(list_sellers) == 2, "Check the function: find_top_two_sellers"
    assert list_sellers[0].dni == "S502", "Check the function: find_top_two_sellers"        
    assert list_sellers[1].dni == "S504", "Check the function: find_top_two_sellers"
    assert len(list_sellers) == 2, "Check the function: find_top_two_sellers"
    tuple_buyer = statistics.find_buyer_lowest_total_purchases()
    assert tuple_buyer[0].dni == "B101", "Check find_buyer_lowest_total_purchases"
    assert tuple_buyer[1] == 53.5, "Check find_buyer_lowest_total_purchases" 
    list_products = statistics.order_products_by_tax(order_type=OrderType.DES)
    assert list_products[0][0].product_id == "P702", "Check the function: order_products_by_tax"
    assert list_products[1][0].product_id == "P703", "Check the function: order_products_by_tax"
    assert list_products[2][0].product_id == "P704", "Check the function: order_products_by_tax"
    assert len(list_products) == 6, "Check the function: order_products_by_tax"