from Restaurant.Bussines import finances, menu, profile

def display_menu():
    print("Welcome Manager")
    print("Balanca -> 1")
    print("Puneso Punonjes te ri -> 2")
    print("Largo nje punonjes -> 3")
    print("Shto produkt te ri -> 4")
    print("Staff List -> 5")

    ans = input (":")

    if (ans == "1"):
        print(f"Balanca e Biznesit eshte: {finances.restaurant_balance}")
    elif (ans == "2"):
        hire_employee()
    elif (ans == "3"):
        fire_employee()
    elif (ans == "4"):
        add_new_product_in_menu()
    elif (ans == "5"):
        profile.display_staff()
    else:
        print("Komande e pavlefshme")


def hire_employee():
    print("Me jep te dhenat e punonjest te ri...")
    name = input("Emri i punonjesit te ri:")
    profile.staff_list.append(name)
    print(f"{name} sapo filloi pune")
    profile.display_staff()
    #@todo, kerkojni me shume te dhena per punonjesin...
    pass


def fire_employee():
    profile.display_staff()
    employee_name = input("Me jep te dhenat e punonjest qe deshiron te largosh nga puna:")
    if (employee_name not in profile.staff_list):
        print(f"Punonjesi {employee_name} nuk egziston!")
    else:
        profile.staff_list.remove(employee_name)
        print(f"{employee_name} sapo u pushua nga puna")
    profile.display_staff()



def add_new_product_in_menu():
    print("Jepni te dhenat e produktit te ri:")
    new_product_name = input("Emri i produktit te ri")
    new_product_price = float(input("Cmimi i produktit te ri"))
    new_product_quantity = int(input("Sasia stok:"))
    menu.products_list.append(new_product_name)
    menu.products_prices.append(new_product_price)
    menu.products_quantities.append(new_product_quantity)

    finances.display_stock()
    pass
