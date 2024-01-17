from .product import Product
from .recipe import Recipe
import json


class Fridge:
    def __init__(self):
        self.contents = []
        with open('fridge.json', 'r', encoding='utf-8') as fridge_file:
            contents = json.load(fridge_file)
        if contents and len(contents) > 0:
            for product_dict in contents:
                self.contents.append(Product(product_dict['name'], product_dict['quantity'], product_dict['unit of measurement']))

    def save(self):
        with open('fridge.json', 'w', encoding='utf-8') as fridge_file:
            contents = []
            for product in self.contents:
                contents.append({
                    'name': product.name,
                    'quantity': product.quantity,
                    'unit of measurement': product.unit_of_measurement
                })
            json.dump(contents, fridge_file)

    def check_product(self, product_name:str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name.lower() == product_name.lower():
                return product_id, product
        return None, None
    
    def check_product_quantity(self, product:Product, quantity:float):
        return product.quantity - quantity

    def add_product(self, name:str, quantity:float, unit_of_measurement:str):
        valid_units = ['kg', 'g', 'l', 'ml', 'vnt']
        if unit_of_measurement not in valid_units:
            print("Netinkamas vienetas! Galimi vienetai: kg, g, l, ml, vnt")
            return
        else:
            print('Iveskite tesinga pasirinkima')
        product_id, product = self.check_product(name) # nenaudojamus kintamuosius galima vadinti tiesiog _
        if product is not None:
            product.quantity += quantity
        else:
            self.contents.append(Product(name, quantity, unit_of_measurement))

    def remove_product(self, name:str, quantity:float): 
        product_id, product = self.check_product(name) # nenaudojamus kintamuosius galima vadinti tiesiog _
        if product:
            if product.quantity >= quantity:
                product.quantity -= quantity
   
            else:
                print(f'Nepakankamas kiekis {product.name} saldytuve yra {product.quantity}')
        else:
            print(f'Produktas {name} nerastas saldytuve')

    def print_contents(self):
        print("Saldytuvo turinys:")
        for product in self.contents:
            print(product)

    def create_recipe(self):
        recipe = Recipe()
        while True:
            print("Pridėkite ingredientą į receptą (irasykite zodi 'baigti' - kad iseiti is recepto kurimo)")
            ingredient_name = input("Koks ingredientas?: ")
            if ingredient_name.lower() == "baigti":
                break
            ingredient_quantity = float(input(f"Kiek {ingredient_name}?: "))
            recipe.add_ingredient(Product(ingredient_name, ingredient_quantity))
        return recipe

    def check_recipe(self, recipe: Recipe):
        missing_ingredients = []
        for ingredient in recipe.ingredients:
            _, product = self.check_product(ingredient.name)
            if product is not None:
                missing_quantity = product.quantity - ingredient.quantity
                if missing_quantity < 0:
                    missing_ingredients.append(Product(ingredient.name, abs(missing_quantity)))
            else:
                missing_ingredients.append(ingredient)
        if len(missing_ingredients) == 0:
            print('Jus turite reikiamus produktus')
        else:
            print(f'Jums truksta siu produktu: {missing_ingredients}') 