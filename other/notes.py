# Te dhenat e Biznesit
restaurant_name : str = "Il gusto italiano"
type_bussines : str = "Restaurant"
staff_number : int = 15
table_number : int = 30
has_card_payment : bool = True
has_shisha_included : bool = False
has_overdraft_payment : bool = True  # Lejon pagese me overdraft
allows_smoking : bool = True  # Lejohet duhanpirja
has_cocktails : bool = True  # Ka kokteile
no_music_after_midnight : bool = False  # Nuk lejohet muzika pas ores 12 te nates
allows_private_events : bool = True  # Lejohet organizimi i eventeve private
has_delivery_service : bool = True  # Ka sherbim delivery
products_list: list[str] = ["Pizza", "Spagetti", "Rizotto", "Lasagna", "Salad", "Burger", "Steak", "Fish & Chips", "Soup", "Ice Cream"]
products_prices: list[float] = [5.6, 8.9, 5.4, 7.5, 4.0, 6.5, 15.0, 12.0, 4.5, 3.0]
restaurant_balance: float = 800
has_beers: bool = True
has_energy_drinks: bool = False
transport_fee: float = 2.0
currency: str = 'USD'


# Te dhenat e klientit
client_cash_balance: float = 25
client_card_balance: float = 150
client_bag: list[str] = [] # Per momentin do jete bosh, dhe do mbushet kur klienti te porosise produkte
# Afishojme te dhenat e variablave, per te pare nese i kane marre vlerat sic duhet.
print("=== Informacionet e Restorantit ===")
print(f"Emri i restorantit: {restaurant_name}")
print(f"Tipi i biznesit: {type_bussines}")
print(f"Numri i punonjesve: {staff_number}")
print(f"Numri i tavolinave: {table_number}")
print("\n=== Informacionet e Sherbimeve ===")
print("Po, kemi pagese me karte" if has_card_payment else "Jo, nuk kemi pagese me karte")
print("Po, kemi shisha" if has_shisha_included else "Jo, fatkeqsisht nuk kemi shisha")
print("Po, kemi kokteile" if has_cocktails else "Jo, nuk kemi kokteile")
print("Po, lejohet duhanpirja" if allows_smoking else "Jo, nuk lejohet duhanpirja")
print("Po, kemi birra ose pije energjike" if (has_beers or has_energy_drinks) else "Me vjen keq por nuk kemi pije te tilla")
print("Po, kemi edhe birra dhe pije energjike" if (has_beers and has_energy_drinks) else "Jo, nuk i kemi te dyja pijet")
print("Jo, nuk lejohet muzika pas ores 12 te nates" if no_music_after_midnight else "Po, muzika eshte e lejuar pas ores 12 te nates")
print("Po, ofrojme sherbim delivery" if has_delivery_service else "Jo, nuk ofrojme sherbim delivery")
print("Po, lejojme organizimin e eventeve private" if allows_private_events else "Jo, nuk lejojme evente private")
# Meposhte fillon logjika e biznesit:
print("===============================================================================================================")
print(f"Miresevini ne: {restaurant_name} {type_bussines}")
# Printo produktet e menu-se biznesit
print("Menuja e produkteve:")
for idx, (product, price) in enumerate(zip(products_list, products_prices), start=1):
    print(f"{idx}. {product} ({price} {currency})")
# Lexojme produktet qe klienti deshiron te porosise
ordered_products = input("Porositni produktet duke shkruar emrat e tyre te ndare me presje: ").split(",")
ordered_products = [product.strip() for product in ordered_products]  # Hiq hapesirat e panevojshme
invalid_products = [product for product in ordered_products if product not in products_list]
# Kontrollojme nese ka produkte te pavlefshme ne porosi
if invalid_products:
    print("Me vjen keq, por nuk i kemi keto produkte:", ", ".join(invalid_products))
    exit(0)
# Llogarisim cmimin total te porosise
ordered_indices = [products_list.index(product) for product in ordered_products]
ordered_prices = [products_prices[i] for i in ordered_indices]
total_price = sum(ordered_prices)
# Afishojme balancat e restorantit dhe klientit, gjithashtu dhe canten e klientit
print("\n=== Balancat Fillestare ===")
print(f"Balanca e restorantit: {restaurant_balance} {currency}")
print(f"Balanca e klientit: Cash: {client_cash_balance} {currency}, Card: {client_card_balance} {currency}")
print(f"Canta e klientit: {client_bag}")
# Pyesim klientin se cfare menyre pagese ka deshire te perdore per transaksionin
ans = input("Si do e beni pagesen? (cash / card / overdraft / delivery): ").lower()
# Kontrollojme pergjigjen e klientit dhe realizojme pagesen
if ans == "cash":
    print("Ju keni zgjedhur pagesen me cash.")
    if client_cash_balance >= total_price:
        print("Pagesa u krye me sukses!")
        client_cash_balance -= total_price
        restaurant_balance += total_price
        client_bag.extend(ordered_products)  # Shto produktet e porositura ne canten e klientit
    else:
        print("Me vjen keq, por nuk keni para te mjaftueshme!")
elif ans == "card":
    print("Ju keni zgjedhur pagesen me karte.")
    if has_card_payment:
        if client_card_balance >= total_price:
            print("Pagesa u krye me sukses!")
            client_card_balance -= total_price
            restaurant_balance += total_price
            client_bag.extend(ordered_products)  # Shto produktet e porositura ne canten e klientit
        else:
            print("Me vjen keq, por nuk keni balance te mjaftueshme ne karte!")
    else:
        print("Me vjen keq, por nuk ofrojme pagesa me karte.")
elif ans == "overdraft":
    print("Ju keni zgjedhur pagesen me overdraft.")
    if has_overdraft_payment:
        print("Pagesa u krye me sukses me overdraft!")
        restaurant_balance += total_price
        client_bag.extend(ordered_products)  # Shto produktet e porositura ne canten e klientit
    else:
        print("Me vjen keq, por nuk ofrojme pagesa me overdraft.")
elif ans == "delivery":
    print("Ju keni zgjedhur sherbimin delivery.")
    if has_delivery_service:
        total_price += transport_fee
        print(f"Tarifa totale perfshire delivery eshte {total_price} {currency}.")
        if client_cash_balance >= total_price:
            print("Pagesa u krye me sukses!")
            client_cash_balance -= total_price
            restaurant_balance += total_price
            client_bag.extend(ordered_products)  # Shto produktet e porositura ne canten e klientit
        else:
            print("Me vjen keq, por nuk keni para te mjaftueshme per te perfituar delivery!")
    else:
        print("Me vjen keq, por nuk ofrojme sherbim delivery.")
else:
    print("Metode pagese e pavlefshme. Ju lutem, provoni perseri.")
    exit(0)
# Afishojme balancat e reja dhe permbajtjen e cantes se klientit
print("\n=== Balancat Pas Transaksionit ===")
print(f"Balanca e restorantit: {restaurant_balance} {currency}")
print(f"Balanca e klientit: Cash: {client_cash_balance} {currency}, Card: {client_card_balance} {currency}")
print(f"Canta e klientit: {client_bag}")
print(f"\nFaleminderit qe zgjodhet {restaurant_name} {type_bussines}. Ju urojme nje dite te mbare!")