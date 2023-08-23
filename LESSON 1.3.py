class Item:
    def __init__(self,name,price,weight):
        self.name=name
        self.price=price
        self.weight=weight
    def __add__(self, other):
        if isinstance(other,Item) and isinstance(self,Item):
            return self.price+other.price
        if isinstance(other,int):
            return self.price+other

a=Item("Видеокарта",45000,0.3)
b=Item("Процессор",30000,0.1)
c=Item("Процессор",30000,0.1)
print(a+(b+c))   #Общая стоимость. С помощью add можно не добавлять .place в print