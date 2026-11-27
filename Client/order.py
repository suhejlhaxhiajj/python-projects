
from Restaurant.Bussines import menu
from Restaurant.Bussines import finances
from Restaurant.Bussines import profile as business_profile #(ALIAS)
from Restaurant.Client import profile as client_profile


def order_products():
    # Lexojme emrin  e produktit nga perdoruesi dhe vleren e tij e ruajme tek variabli "ordered_product"
    ordered_product = input("Porosit nje produkt duke shkruar emrin e tij: ")
    print("ju porositet produktin: " + ordered_product)

    # Kontrollojme, nese produkti qe perdoruresi ka porositur, nuk ndodhet ne listen e menuse qe ne ofrojme, atehere do te mbyllim programin!
    if (ordered_product not in menu.products_list):
        print("me vjen keq por nuk e kemi kete produkt, te lutem zgjidh nje produkt nga menuja!")
        exit(
            0)  # exit eshte per te nderprere exekutimin e kodit me poshte, persa kohe ne nuk e e kemi kete produkt ne menu.

    # Ne fillim afishojme  balancat e restorantit, dhe klientit, gjithashtu dhe canten e klientit, per te pare se ne cfare gjendje jemi
    print(f"balanca e vjeter e restorantit eshte: {finances.restaurant_balance}")
    print(f"balanca e vjeter e klientit eshte: cash: {client_profile.cash_balance}, card: {client_profile.card_balance}")
    print(client_profile.bag)

    # Pyesim klientin se cfare menyre pagese ka deshire te perdore per transaksionin:
    ans = input("Si do e beni pagesen? (cash / card)")

    # kontrollojme pergjigjen e klientit:
    # nese klienti kerkon pagese me cash, ath do ja zbresim leket nga balanca cash
    if (ans == "cash"):
        print("proceed with cash")
        if (client_profile.cash_balance >= menu.product_price):
            print("proceed with payment")
            client_profile.cash_balance = client_profile.cash_balance - menu.product_price
            finances.restaurant_balance = finances.restaurant_balance + menu.product_price
            client_profile.bag.append(ordered_product)  # shto produktin e porositur ne canten e klientit
        else:
            print("Me vjen keq por nuk keni para mjaftueshem!")

    # nese kleinti kerkon pagese me card, ath do ja zbresim leket nga balanca card
    elif (ans == "card"):
        print("proceed with card")
        if (business_profile.has_card_payment):
            if (client_profile.card_balance >= menu.product_price):
                print("proceed with payment")
                client_profile.card_balance = client_profile.card_balance - menu.product_price
                finances.restaurant_balance = finances.restaurant_balance + menu.product_price
                client_profile.bag.append(ordered_product)  # shto produktin e porositur ne canten e klientit
            else:
                print("Ju lutem kontrolloni limitin e kartes tuaj!")
        else:
            print("Ne nuk ofrojme pagesa me card!")


    # nese klienti ka shkruar ndonje metode pagese qe nuk e kemi ose qka shkruar metoden gabim, atehere i themi qe nuk e ofrojme kete metode pagese dhe dalim nga programi
    else:
        print("nuk e ofrojme kete lloje metode pagese...")

    print(f"Bags client:", client_profile.bag)