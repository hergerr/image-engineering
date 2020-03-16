class Product:
    def __init__(self, price, name, quantity):
        self.price = price
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f'Nazwa: {self.name}\nIlość: {self.quantity}\nCena: {self.price}'

    def __len__(self):
        return 1


class Shop:
    def __init__(self, product_dict):
        self.product_dict = product_dict
        # nie jest możliwe zaimplementowanie __iter__ w oparciu o dict
        self.list_for_iter = ['jeden', 'dwa', 'trzy']

    def buy(self, product_name):
        self.product_dict[product_name].quantity += 1
        print(
            f'Obecnie jest {self.product_dict[product_name].quantity} {self.product_dict[product_name].name}')

    def sell(self, product_name):
        if self.product_dict[product_name].quantity > 0:
            self.product_dict[product_name].quantity -= 1
            print(
                f'Obecnie jest {self.product_dict[product_name].quantity} {self.product_dict[product_name].name}')
        else:
            print(
                f'Brak na stanie produktu {self.product_dict[product_name].name}')

    def get_total_price(self):
        for k, v in self.product_dict.items():
            print(
                f'Wartość wszystkich produktów {v.name}: {v.quantity * v.price}')

    def __str__(self):
        return 'Obiekt sklepu'

    def __len__(self):
        return len(self.product_dict)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        if(self.index >= len(self.list_for_iter)):
            self.index = 0
        return self.list_for_iter[self.index]


shop = Shop(product_dict={'maslo': Product(5, 'Masło Extra', 3),
                          'chleb': Product(4.5, 'Chleb żytni', 3),
                          'herbata': Product(5.95, 'Herbata Lipton', 10)})

shop.get_total_price()
shop.sell('chleb')
shop.buy('maslo')
shop.get_total_price()
print(len(shop))

shop_iter = iter(shop)
print(shop_iter)
print(next(shop_iter))
print(next(shop_iter))
print(next(shop_iter))
print(next(shop_iter))
