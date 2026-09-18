from datetime import datetime


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate=0.05):
        self.items = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        self.items.append(product)

    def calculate_subtotal(self):
        return sum(item.get_total() for item in self.items)

    def calculate_tax(self):
        return self.calculate_subtotal() * self.tax_rate

    def calculate_grand_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def print_bill(self):
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        grand_total = self.calculate_grand_total()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\n" + "=" * 52)
        print("               INVOICE / RECEIPT")
        print(f" Date: {timestamp}")
        print("=" * 52)
        print(f"{'Item':<20}{'Qty':<8}{'Price':<12}{'Total':<10}")
        print("-" * 52)

        for item in self.items:
            print(
                f"{item.name:<20}{item.quantity:<8}₹{item.price:<11.2f}₹{item.get_total():<10.2f}"
            )

        print("-" * 52)
        print(f"{'Subtotal:':<40}₹{subtotal:.2f}")
        print(f"{f'Tax ({int(self.tax_rate * 100)}%):':<40}₹{tax:.2f}")
        print("=" * 52)
        print(f"{'Grand Total:':<40}₹{grand_total:.2f}")
        print("=" * 52)


def main():
    bill = Bill(tax_rate=0.05)

    print("Enter purchased products (type 'done' as item name to finish):")
    while True:
        name = input("\nItem name: ").strip()
        if name.lower() == "done":
            break
        try:
            price = float(input("Unit price (₹): "))
            qty = int(input("Quantity: "))
            bill.add_product(Product(name, price, qty))
        except ValueError:
            print("Invalid input! Price and quantity must be numbers.")

    if bill.items:
        bill.print_bill()
    else:
        print("No items entered. Invoice generation cancelled.")


if __name__ == "__main__":
    main()