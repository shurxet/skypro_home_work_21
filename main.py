from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def __init__(self, items, company):
        self._items = items
        self._company = company

    @abstractmethod
    def add(self, title, count):
        pass

    @abstractmethod
    def remove(self, title, count):
        pass

    @property
    @abstractmethod
    def get_free_space(self):
        pass

    @property
    @abstractmethod
    def items(self):
        pass

    @property
    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    def add(self, title, count):
        if title in self._items:
            self._items[title] += count
        else:
            self._items[title] = count
        self._capacity -= count

    def remove(self, title, count):
        res = self._items[title] - count
        if res > 0:
            self._capacity += count
            self._items[title] = res
        else:
            del self._items[title]
        self._capacity += count

    @property
    def get_free_space(self):
        return self._capacity

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        self._items = new_items
        self._capacity -= sum(self._items.values())

    @property
    def get_unique_items_count(self):
        return len(self._items.keys())


class Shop(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    def add(self, title, count):
        if title in self._items:
            self._items[title] += count
        else:
            self._items[title] = count
        self._capacity -= count

    def remove(self, title, count):
        res = self._items[title] - count
        if res > 0:
            self._capacity += count
            self._items[title] = res
        else:
            del self._items[title]
        self._capacity += count

    @property
    def get_free_space(self):
        return self._capacity

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        self._items = new_items
        self._capacity -= sum(self._items.values())

    @property
    def get_unique_items_count(self):
        return len(self._items.keys())


class Request:
    def __init__(self, info):
        self.info = self._split_info(info)
        self.from_ = self.info[4]
        self.to = self.info[6]
        self.amount = int(self.info[1])
        self.product = self.info[2]

    @staticmethod
    def _split_info(info):
        return info.split(" ")

    def __repr__(self):
        return f"?????????????????? {self.amount} {self.product} ???? {self.from_} ?? {self.to}"


def main():
    while(True):
        #user_input = "?????????????????? 3 ???????????????? ???? ?????????? ?? ??????????????"
        user_input = input("?????????????? ????????????: ")

        if user_input == "stop":
            break

        request = Request(user_input)
        print(request)



        # from_ = store if request.from_ == "??????????" else shop
        # to = store if request.to == "??????????" else shop

        if request.from_ == request.to:
            print("?????????? ???????????????????? == ?????????? ????????????????")
            continue

        if request.from_ == "??????????":

            if request.product in store.items:
                print(f"???????????? ?????????? ???????? ?? ???????????? \"{request.from_}\"")
            else:
                print(f"?? ???????????? {request.from_} ?????? ???????????? ????????????")
                continue

            if store.items[request.product] >= request.amount:
                print(f"???????????? ???????????????????? ???????? ?? ???????????? \"{request.from_}\"")
            else:
                print(f"?? ???????????? {request.from_} ???? ?????????????? {request.amount - store.items[request.product]}")
                continue

            if shop.get_free_space >= request.amount:
                print(f"?? ???????????? \"{request.to}\" ???????????????????? ??????????")
                #print(to.get_free_space)
            else:
                #print(to.get_free_space)
                print(f"?? ???????????? {request.to} ???? ?????????????? {request.amount - shop.get_free_space} ")
                continue

            if request.to == "??????????????" and shop.get_unique_items_count == 5 and request.product not in shop.items:
                print("?? ???????????????? ???????????????????? ???????????????????? ????????????????")
                continue

            store.remove(request.product, request.amount)
            print(f"???????????? ???????????? {request.amount} {request.product} ???? ???????????? {request.from_}")
            print(f"???????????? ?????????? {request.amount} {request.product} ???? ???????????? {request.from_} ?? ?????????? {request.to}")
            shop.add(request.product, request.amount)
            print(f"???????????? ???????????????? {request.amount} {request.product} ?? ?????????? {request.to}")

        else:
            if request.product in shop.items:
                print(f"???????????? ?????????? ???????? ?? ???????????? \"{request.from_}\"")
            else:
                print(f"?? ???????????? {request.from_} ?????? ???????????? ????????????")
                continue

            if shop.items[request.product] >= request.amount:
                print(f"???????????? ???????????????????? ???????? ?? ???????????? \"{request.from_}\"")
            else:
                print(f"?? ???????????? {request.from_} ???? ?????????????? {request.amount - shop.items[request.product]}")
                continue

            if store.get_free_space >= request.amount:
                print(f"?? ???????????? \"{request.to}\" ???????????????????? ??????????")
                #print(to.get_free_space)
            else:
                #print(to.get_free_space)
                print(f"?? ???????????? {request.to} ???? ?????????????? {request.amount - store.get_free_space} ")
                continue

            store.remove(request.product, request.amount)
            print(f"???????????? ???????????? {request.amount} {request.product} ???? ???????????? {request.from_}")
            print(f"???????????? ?????????? {request.amount} {request.product} ???? ???????????? {request.from_} ?? ?????????? {request.to}")
            store.add(request.product, request.amount)
            print(f"???????????? ???????????????? {request.amount} {request.product} ?? ?????????? {request.to}")

        print("="*30)
        print("???? ????????????:")
        for title, count in store.items.items():
            print(f"{title}: {count}")
        print(f"???????????????????? ?????????? {store.get_free_space}")
        print("="*30)
        print("?? ????????????????:")
        for title, count in shop.items.items():
            print(f"{title}: {count}")
        print(f"???????????????????? ?????????? {shop.get_free_space}")
        print("=" * 30)





if __name__ == "__main__":
    store = Store()
    shop = Shop()

    store_items = {
        "????????": 5,
        "??????????????": 10,
        "????????????????": 38,
    }
    store.items = store_items

    # user_input = "?????????????????? 3 ???????????????? ???? ?????????? ?? ??????????????"

    main()






