class bag_o_loot():

    lootbag_dict = {}

    def add (self, gift, child_name):
        self.lootbag_dict[child_name] = gift
        print(self.lootbag_dict)
        with open('lootbag.txt', 'a') as text_file:
            text_file.write(f'Little {child_name} is getting a {gift} this year' + '\n')


    def remove(self, gift, child_name):
        text = open('lootbag.txt', 'r')
        lines = text.readlines()
        text.close()
        with open('lootbag.txt', 'w') as text_file:
            for line in lines:
                if line != f'Little {child_name} is getting a {gift} this year' + '\n':
                    text_file.write(line)

    def lootbag_list(self):
        lootbag = open('lootbag.txt').readlines()
        print(lootbag)

    def toys_for_child(self, child_name):
        list_of_toys = open('lootbag.txt').readlines()
        for name in list_of_toys:
            if name == f'{child_name}':
                print(name)