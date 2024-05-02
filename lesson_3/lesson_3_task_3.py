from Address import Address
from Mailing import Mailing

to_address = Address(487272, "Москва", "Новый Арбат", 40, 387)
from_address = Address(589019,"Омск", "Победная", 98, 412)
mailing = Mailing(to_address, from_address, 1200, "CBA2024")

print("Отправление ",mailing.track,"из", mailing.from_address.index,
      mailing.from_address.city,mailing.from_address.street,
      mailing.from_address.house,mailing.from_address.app,
      "в", mailing.to_address.index,mailing.to_address.city,
      mailing.to_address.street,mailing.to_address.house,
      mailing.to_address.app,".","Стоимость",mailing.cost,"рублей.")