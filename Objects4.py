# Instance Variables Vs Class Variables
class Shop:
    Place = "GVR Mall"
    def __init__(self,name):
        self.name = name

buy1 = Shop('Dresses')
buy2 = Shop('Shoes')

print(buy1.name)
print(Shop.Place)
print(buy2.name)
print(Shop.Place)
print(buy1.Place)
