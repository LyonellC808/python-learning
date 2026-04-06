# ============================================
# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
# ============================================

# ----- Menu Data (do not modify) -----
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]

topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions",
"Sausage", "Bacon", "Extra Cheese", "Pineapple"]

topping_price = 1.50 # each topping, any size

# ----- Order Storage -----
order_descriptions = []
order_prices = []

# ===== YOUR ORIGINAL START (kept the same) =====
print("=" * 30)
print("PIZZA SIZES")
print("=" * 30)

for i in range(len(sizes)):
    print(f"{i+1}. {sizes[i]} ${size_prices[i]:>5}")

print("=" * 30)

# ===== ORDER LOOP =====
while True:

    # --- size selection (your version, slightly fixed) ---
    while True:
        size = input("Select a size for pizza: ")
        if not size.isdigit() or int(size) - 1 not in range(len(sizes)):
            print(f"Please pick a number: 1-{len(sizes)}")
            continue 
        size = int(size)
        break

    # --- toppings ---
    print(f"Available toppings (${topping_price:.2f})")
    for i in range(len(topping_names)):
        print(f"{i+1}. {topping_names[i]}")

    selected_topping = []

    while True:
        topping = input("Please select topping for pizza (or 'done'): ")

        if topping.lower() == 'done':
            break

        if not topping.isdigit():
            print("please select a number")
            continue

        if int(topping) -1 not in range(len(topping_names)):
            print(f"select a number between 1 to {len(topping_names)}")
            continue

        topping_name = topping_names[int(topping) - 1]

        if topping_name in selected_topping:
            print(f"{topping_name} already added")
            continue
        else:
            selected_topping.append(topping_name)
            print(f"Added {topping_name}")

    # --- price + description (fixed) ---
    base_price = size_prices[size - 1]
    price = base_price + len(selected_topping) * topping_price

    if selected_topping:
        description = sizes[size - 1] + " " + ", ".join(selected_topping)
    else:
        description = sizes[size - 1] + " Cheese"

    order_descriptions.append(description)
    order_prices.append(price)

    # --- order another ---
    while True:
        again = input("Order another pizza? (yes/no): ").lower()
        if again in ["yes", "y", "no", "n"]:
            break
        print("please enter yes or no")

    if again in ["no", "n"]:
        break

# ===== AFTER ORDERING =====
if len(order_descriptions) == 0:
    print("No pizzas ordered!")
else:

    # --- discount ---
    discount = 0
    tries = 0

    while tries < 3:
        code = input("Enter discount code (or 'none'): ").lower()

        if code == "none":
            break
        elif code == "student10":
            discount = 0.10
            break
        elif code == "halfoff":
            discount = 0.50
            break
        else:
            print("wrong code")
            tries += 1

    if tries == 3:
        print("No discount applied.")

    # --- receipt ---
    print("\nYOUR ORDER RECEIPT")
    print("=" * 30)

    subtotal = 0

    for i in range(len(order_descriptions)):
        print(f"{i+1}. {order_descriptions[i]}")
        print(f"${order_prices[i]:.2f}")
        subtotal += order_prices[i]

    discount_amount = subtotal * discount
    subtotal -= discount_amount

    tax = subtotal * 0.07
    total = subtotal + tax

    print("-" * 30)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")

    # --- most expensive ---
    max_price = order_prices[0]
    max_index = 0

    for i in range(len(order_prices)):
        if order_prices[i] > max_price:
            max_price = order_prices[i]
            max_index = i

    print(f"Most expensive: {order_descriptions[max_index]}")

    # --- size count ---
    counts = [0,0,0,0]

    for desc in order_descriptions:
        for i in range(len(sizes)):
            if sizes[i] in desc:
                counts[i] += 1

    print("\nPizza count:")
    for i in range(len(sizes)):
        print(f"{sizes[i]}: {counts[i]}")

    print("\nThank you!")