stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    item_vals = list(inventory.values())
    item_total = sum(item_vals)
    
    print('Inventory:')

    for key in inventory:
        print(inventory[key], key)

    print('Total number of items: %d' % item_total)

if __name__ == "__main__":
    displayInventory(stuff)
