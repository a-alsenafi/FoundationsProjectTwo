# UTILS AND FUNCTIONALITY
from data import stores
from components import Store
from components import Cart

site_name = "orderer"  # Give your site a name


def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)


def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for x in stores:
        print("-", x.name)


def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    obj = Store("X")
    for x in stores:
        if x.name == store_name:
            return x
    return obj


def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    print("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes.")
    x = "abc"
    while x != "checkout":
        x = input()
        if x == get_store(x).name:
            return get_store(x)
        else:
            print("store not found")


def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!

    picked_store.print_products()
    print("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above. Type \"back\" to go back to the main menu where you can checkout")
    x = "abc"
    while x != "back":
        x = input()
        for y in picked_store.products:
            if y.name == x:
                cart.add_to_cart(y)
                print("Product has been added")
                break


def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    pick_products(cart, pick_store())
    cart.checkout()


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
