from operator import truediv

from Restaurant.Client import order
from Restaurant.Bussines import menu, dashboard, profile, finances
ans = "open"

def display_main_menu():
    print(f"Miresevini ne {profile.restaurant_name}")
    print("Klient -> 1")
    print("Menaxher -> 2")
    print("Ekonomist -> 3")



while (ans != "exit"):
    display_main_menu()
    ans = input (":")

    if (ans == "1"):
        print("ju jeni futur si Klient")
        profile.display_menu()
        order.order_products()
    elif (ans == "2"):
        print("ju jeni futur si Menaxher")
        dashboard.display_menu()
    elif (ans == "3"):
        print("ju jeni futur si Ekonomist")
        finances.display_menu()
    elif (ans == "exit"):
        print("Bye")
    else:
        print("Komande e pavlefshme")