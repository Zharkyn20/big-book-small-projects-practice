class Case:
    def __init__(self, number_of_names, list):
        self.cost = 0
        self.number_of_names = number_of_names
        self.list = list


    def sorting_cost_counter(self):
        cost = 0
        for i in range(len(list)):
            for next_name in list[i+1:]:
                if list[i] >= next_name:
                    cost += 1

        return cost
t = int(input())
for i in range(1, t+1):
    number_of_names = int(input())
    list = []
    for i in range(int(number_of_names)):
        list.append(input())

    case = Case(number_of_names, list)
    print('Case #{}: {}'.format(i, case.sorting_cost_counter()))