from smartphone import Smartphone

Samsung = Smartphone("Samsung","A20","89994324141")
iPhone12 = Smartphone("iPhone","12 Pro Max","89880988998")
Xiaomi = Smartphone("Xiaomi","12T Pro","89770877887")
Huawei = Smartphone("Huawei","Pura 70 Ultra","89655656565")
Asus = Smartphone("Asus","ROG Phone 12","89322323223")

catalog = [Samsung, iPhone12, Xiaomi, Huawei, Asus]

for x in catalog:
    print(x.mark, x.model ,x.num)
    