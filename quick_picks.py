import random


NUM_PER_LINE = 6
MAX_NUM = 45
MIN_NUM = 1


def generate_num():
    valid_input = False
    while not valid_input:
        try:
            amount = int(input("How many quick picks? "))
            for x in range(amount):
                num_list = []
                for y in range(NUM_PER_LINE):
                    random_num = random.randint(MIN_NUM, MAX_NUM)
                    while random_num in num_list:
                        random_num = random.randint(MIN_NUM, MAX_NUM)
                    num_list.append(random_num)
                num_list.sort()
                print(" ".join(f"{num:2}" for num in num_list))
                valid_input = True
        except ValueError:
            print("Please input a number!")


generate_num()