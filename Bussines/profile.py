from Restaurant.Bussines import menu

restaurant_name : str = "Il gusto italiano"
type_bussines : str = "Restaurant"

table_number : int = 30
has_card_payment : bool = True
has_shisha_included : bool = False
has_overdraft_payment : bool = True  # Lejon pagese me overdraft
allows_smoking : bool = True  # Lejohet duhanpirja
has_cocktails : bool = True  # Ka kokteile
no_music_after_midnight : bool = False  # Nuk lejohet muzika pas ores 12 te nates
allows_private_events : bool = True  # Lejohet organizimi i eventeve private
has_delivery_service : bool = True  # Ka sherbim delivery

has_beers: bool = True
has_energy_drinks: bool = False

staff_number : int = 15
staff_list: list[str] = []


def display_menu():
    print(f"Miresevini")
    # Printo produktet e menu-se biznesit
    print("Menuja e produkteve:")
    print(menu.products_list)
    print(menu.products_prices)


def display_staff():
    print(f"Staff List")
    if (len(staff_list) == 0):
        print("Nuk ka asnje te punesuar per momentin")
    else:
        print(staff_list)