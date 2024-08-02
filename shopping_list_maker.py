shopping_cart = []

def main():
    while True:
        action = input("what would you like to do with your shopping cart today? (add/remove/view/quit)").lower()
        if action == 'add':
            add(input(f'What would you like to {action} today?'))
        elif action == 'remove':
            remove(input(f'What would you like to {action} today?'))
        elif action == 'view':
            quit_view(shopping_cart,False)
        elif action == 'quit':
            quit_view(shopping_cart,True)
            break
        else:
            print("Unkown command, please try again.")


def add(item):
    shopping_cart.append(item)


def remove(item):
    shopping_cart.remove(item)


def quit_view(cart,quit):
    for item in cart:
        print(f'Item {cart.index(item) + 1}: {item}')
    if quit:
        print("This is your shopping list! Have a great time at the store!")


def view(cart):
    for item in cart:
        print(f'Item {cart.index(item) + 1}: {item}')

main()