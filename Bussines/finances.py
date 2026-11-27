from Restaurant.Bussines import menu, profile

restaurant_balance: float = 80000
transport_fee: float = 2.0
currency: str = 'EUR'
employee_salary: float = 1000



def display_menu():
    print("Welcome Financier")
    print("Balanca -> 1")
    print("Pay Employes -> 2")
    print("Inventory -> 3")

    ans = input (":")

    if (ans == "1"):
        print(f"Balanca e Biznesit eshte: {restaurant_balance}")
    elif (ans == "2"):
        pay_salaries()
    elif (ans == "3"):
        display_stock()
    else:
        print("Komande e pavlefshme")


def pay_salaries():
    #cdo employe do marre nga x leke (supozojme se kemi 10 punonjes nga 1000eu => 10k in total)
    global employee_salary
    global restaurant_balance

    total_salaries = employee_salary * profile.staff_number
    restaurant_balance -= total_salaries
    print("Sapo u paguan")
    print(f"Balanca e re e biznesit eshte: {restaurant_balance}")
    pass
#
def display_stock():
    # pass
    print("Stock i produkteve eshte:")
    print(menu.products_list)
    print(menu.products_quantities)