
class Purchase:
    list_of_items = ["Cake", "Soap", "Jam", "Cereal", "Hand Sanitizer", "Biscuits", "Bread"]
    list_of_count_of_each_item_sold = [0,0,0,0,0,0,0]
    def __init__(self):
        self.__items_purchased = []
        self.__item_on_offer = None

    def get_items_purchased(self):
        return self.__items_purchased

    def get_item_on_offer(self):
        return self.__item_on_offer

    def sell_items(self,list_of_items_to_be_purchased):
        sold = 0
        for i in range(0,len(list_of_items_to_be_purchased)):
            for j in range(0,len(Purchase.list_of_items)):
                if Purchase.list_of_items[j].lower() == list_of_items_to_be_purchased[i].lower():
                    if list_of_items_to_be_purchased[i].lower() == "soap":
                        self.provide_offer()
                    Purchase.list_of_count_of_each_item_sold[j] += 1
                    self.__items_purchased.append(list_of_items_to_be_purchased[i])

    def provide_offer(self):
        item = "Hand Sanitizer".lower()
        index = 0
        for i in range(0,len(Purchase.list_of_items)):
            if Purchase.list_of_items[i].lower() == item:
                index = i
        if index >= 0:
            Purchase.list_of_count_of_each_item_sold[index] += 1
        self.__item_on_offer = "HAND SANITIZER"

    @staticmethod
    def find_total_items_sold():
        sold = 0
        for number in Purchase.list_of_count_of_each_item_sold:
            sold += number
        return sold

one=Purchase()
one.sell_items([JAM, CHOcolates, Ghee, Soap])

