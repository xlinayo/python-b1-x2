# Write your imports here
from bills.item import OrderType


class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    def find_top_sell_product(self) -> (Product, int):
        # Write here your code
        counter = {}
        for bill in self.bills:
            for product in bill.products:
                counter[product] = counter.get(product, 0) + 1

        top_product = max(counter, key=counter.get)
        return top_product, counter[top_product]
        pass

    def find_top_two_sellers(self) -> list:
        # Write here your code
        seller_totals = {}
        for bill in self.bills:
            seller = bill.seller
            seller_totals[seller] = seller_totals.get(seller, 0) + bill.calculate_total()
            
        ordered = sorted(seller_totals.items(), key=lambda x: x[1], reverse=True)
        return [seller for seller, _ in ordered[:2]]
        pass

    def find_buyer_lowest_total_purchases(self) -> (Buyer, float):
        # Write here your code
        buyer_totals = {}
        for bill in self.bills:
            buyer = bill.buyer
            buyer_totals[buyer] = buyer_totals.get(buyer, 0) + bill.calculate_total()

        buyer = min(buyer_totals, key=buyer_totals.get)
        return buyer, buyer_totals[buyer]
        pass

    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        # Write here your code
        products = {}
        for bill in self.bills:
            for product in bill.products:
                products[product] = product.calculate_total_taxes()

        reverse = order_type == OrderType.DES
        return sorted(products.items(), key=lambda x: x[1], reverse=reverse)
        pass

    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
