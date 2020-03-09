class Product:
    def __init__(self, price, name, quantity):
        self.price = price
        self.name = name
        self.quantity = quantity

    
class Shop:
    def __init__(self, product_dict):
        self.product_dict = product_dict

    def buy(self, product_name):
        self.product_dict[product_name].quantity += 1
        print(f'Obecnie jest {self.product_dict[product_name].quantity} {self.product_dict[product_name].name}')
    
    def sell(self, product_name):
        if self.product_dict[product_name].quantity > 0: 
            self.product_dict[product_name].quantity -= 1
            print(f'Obecnie jest {self.product_dict[product_name].quantity} {self.product_dict[product_name].name}')
        else:
            print(f'Brak na stanie produktu {self.product_dict[product_name].name}')

    def get_total_price(self):
        for k, v in self.product_dict.items():
            print(f'Wartość wszystkich produktów {v.name}: {v.quantity * v.price}')
    


shop = Shop(product_dict={'maslo': Product(5, 'Masło Extra', 3),
                            'chleb': Product(4.5, 'Chleb żytni', 3),
                            'herbata': Product(5.95, 'Herbata Lipton', 10)})

shop.get_total_price()
shop.sell('chleb')
shop.buy('maslo')
shop.get_total_price()
