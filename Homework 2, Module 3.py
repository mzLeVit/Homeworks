import random 


def get_numbers_ticket(min_num, max_num, qntt):
    if min_num <= 0 or max_num >= 1001:
        return []
    lottery = set ()
    while len(lottery) != qntt:
        lottery.add(random.randint(min_num, max_num))
    
    return sorted(lottery)
    
lottery_nums = get_numbers_ticket (1, 1000, 33)
print (f"Winning numbers are: , {lottery_nums}")