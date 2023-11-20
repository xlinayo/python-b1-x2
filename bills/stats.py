# Write your imports here



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
        pass

    def find_top_two_sellers(self) -> list:
        # Write here your code
        pass

    def find_buyer_lowest_total_purchases(self) -> (Buyer, float):
        # Write here your code
        pass

    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        # Write here your code
        pass

    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
