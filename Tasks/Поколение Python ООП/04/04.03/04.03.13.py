# Реализуйте класс Postman, описывающий почтальона. При создании экземпляра класс не должен принимать никаких аргументов.
# Экземпляр класса Postman должен иметь один атрибут:
# delivery_data — изначально пустой список адресов, по которым следует доставить письма
# Экземпляр класса Postman должен иметь три метода экземпляра:
# add_delivery() — метод, принимающий в качестве аргументов улицу, дом и квартиру, и добавляющий в список адресов эти данные в виде кортежа:
# (<улица>, <дом>, <квартира>)
# get_houses_for_street() — метод, принимающий в качестве аргумента улицу и возвращающий список всех домов на этой улице, в которые требуется доставить письма
# get_flats_for_house() — метод, принимающий в качестве аргументов улицу и дом и возвращающий список всех квартир в этом доме, в которые требуется доставить письма

class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, apart):
        self.delivery_data.append((street, house, apart))

    def get_houses_for_street(self, st):
        house_list = []
        for s, h, _ in self.delivery_data:
            if s == st and h not in house_list:
                house_list.append(h)
        return house_list

    def get_flats_for_house(self, target_st, target_house):
        apart_list = []
        for s, h, a in self.delivery_data:
            if s == target_st and h == target_house and a not in apart_list:
                apart_list.append(a)
        return apart_list
