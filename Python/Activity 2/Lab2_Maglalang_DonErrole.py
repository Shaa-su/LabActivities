products = {
    "P001": {"name": "Laptop", "price": 35000},
    "P002": {"name": "Smartphone", "price": 15000},
    "P003": {"name": "Headphones", "price": 2000},
    "P004": {"name": "USB Drive", "price": 500},
}

# === Calculations ===
def compute_subtotal(cart):
    #Compute subtotal from all items in the cart
    return sum(item["total"] for item in cart)

def compute_discount(subtotal):
    #Apply 10% discount if subtotal >= 20000
    if subtotal >= 20000:
        return subtotal * 0.10
    return 0

def compute_tax(subtotal, discount):
    #Compute 12% VAT after discount
    return (subtotal - discount) * 0.12

def compute_total(subtotal, discount, tax):
    #Compute final total
    return subtotal - discount + tax


# === MAIN PROGRAM ===
print("=== Welcome to BulSU E-Commerce Store ===")
print("")
print("Available Products:")
print("P001 - Laptop (₱35000)")
print("P002 - Smartphone (₱15000)")
print("P003 - Headphones (₱2000)")
print("P004 - USB Drive (₱500)")
print("")

cart = []

# === LOOP ===
while True:
    try:
        code = input("Enter product code (or '0' to checkout): ").strip().upper()
        if code == "0":
            break
        # pag mali nalagay
        if code not in products:
            raise KeyError("Invalid product code.")
                
        quantity = int(input("Enter Quantity: "))
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")  # to prevent negative number 

        product = products[code]
        total_price = product["price"] * quantity
        cart.append({
            "name": product["name"],
            "price": product["price"],
            "qty": quantity,
            "total": total_price
        })
        print(f" ✓ Added {quantity} x {product['name']} to cart.\n")

    except KeyError as e:  # == For catching error ==
        print(f"X {e}\n")
    except ValueError as e:
        print(f"X {e}\n")

# === CHECKOUT ===
print("\n=== OFFICIAL RECEIPT ===")
# if nothing got purchased 
if not cart:
    print("No items purchased.")
else:
    # Use the functions for computation
    subtotal = compute_subtotal(cart)
    discount = compute_discount(subtotal)
    tax = compute_tax(subtotal, discount)
    total = compute_total(subtotal, discount, tax)

    # Print items; the :<20 part is for alignment and formatting
    for item in cart:
        print(f"{item['name']:<15} x{item['qty']:<3} ₱{item['total']:>8,}")

    print("-" * 29)
    print(f"{'Subtotal:':<20} ₱{subtotal:>8,}")
    print(f"{'Discount:':<20} -₱{discount:>7,.0f}")
    print(f"{'Tax (12%):':<20} ₱{tax:>8,.0f}")
    print(f"{'Total:':<20} ₱{total:>8,.0f}")
    print("=" * 29)
    print("Thank you for shopping at BulSU E-Commerce Store!")
