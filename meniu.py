import os
import pickle
from saldytuviukas.fridge import Fridge

FRIDGE_FILE = "fridge.pkl"
       
def load_fridge(FRIDGE_FILE=FRIDGE_FILE):
    if os.path.exists(FRIDGE_FILE):
        with open(FRIDGE_FILE, 'rb') as file:
            return pickle.load(file)
    else:
        return Fridge()

def save_fridge(fridge, FRIDGE_FILE=FRIDGE_FILE):
    with open(FRIDGE_FILE, 'wb') as file:
        pickle.dump(fridge, file)

def main():
    fridge = load_fridge()
    while True:
        print("---Violetinis šaldytuvas---")
        print("0: Išeiti")
        print("1: Pridėti produktą į šaldytuvą")
        print("2: Pašalinti produktą iš šaldytuvo")
        print("3: Patikrinti produkto kiekį")
        print("4: Parodyti šaldytuvo turinį")
        print("5: Patikrinti receptą")
        
        choice = input("Pasirinkite: ")

        if choice == "0":
            save_fridge(fridge)
            break
        elif choice == "1":
            product_name = input("Kokį produktą norite pridėti?: ")
            product_quantity = float(input("Kokį kiekį norite pridėti?: "))
            unit_of_measurement = input('Koks tai yra matavimo vienetas? (options: kg, g, l, ml, vnt)')
            valid_units = ['kg', 'g', 'l', 'ml', 'vnt']
            if unit_of_measurement not in valid_units:
                print('Iveskite teisinga matavimo vieneta! Pvz: kg, g, l, ml, vnt')
                continue
            fridge.add_product(product_name, product_quantity, unit_of_measurement)
            print(f'Sekmingai ideta {product_name} {product_quantity}: {unit_of_measurement}.')
        elif choice == "3":
            product_name = input("Kokio produkto kiekį norite patikrinti?: ")
            _, product = fridge.check_product(product_name)
            if product:
                print(f"Produkto {product.name} kiekis šaldytuve: {product.quantity}: {product.unit_of_measurement}")
            else:
                print("Toks produktas nerastas šaldytuve.")
        elif choice == "2":
            if len(fridge.contents) > 0:
                product_name = input("Kokį produktą norite pašalinti?: ")
                product_quantity = float(input("Kokį kiekį norite pašalinti?: "))
                fridge.remove_product(product_name, product_quantity)
                print(f'Sekmingai isimta {product_name} {product_quantity}: {unit_of_measurement}')
            else:
                print('Saldytuvas tuscias, nera ko ismesti')
        elif choice == "4":
            fridge.print_contents()
        elif choice == "5":
            recipe = fridge.create_recipe()
            fridge.check_recipe(recipe)
        else:
            print("Neteisingas pasirinkimas. Įveskite skaičių nuo 0 iki 5.")

if __name__ == "__main__":
    main()
