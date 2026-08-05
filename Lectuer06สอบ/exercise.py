inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]


def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
        if item[0] == item_name:
            item[1] -= quantity_sold
            print(item_name, "เหลือ", item[1], "ชิ้น")
            return

    print("ไม่พบสินค้า")


def calculate_total_value(inventory):
    total = 0

    for item in inventory:
        total += item[1] * item[2]

    return total


def find_most_expensive(inventory):
    most_expensive = inventory[0]

    for item in inventory:
        if item[2] > most_expensive[2]:
            most_expensive = item

    return most_expensive[0]


def add_item(inventory, item_name, quantity, price):
    for item in inventory:
        if item[0] == item_name:
            item[1] = quantity
            item[2] = price
            print("อัปเดตสินค้าแล้ว")
            return

    inventory.append([item_name, quantity, price])
    print("เพิ่มสินค้าแล้ว")


update_inventory(inventory, "Banana", 20)

print("Total value:", calculate_total_value(inventory))

print("Most expensive item:", find_most_expensive(inventory))

add_item(inventory, "Eggs", 30, 0.25)

add_item(inventory, "Eggs", 50, 0.30)

print("Final inventory:")
print(inventory)