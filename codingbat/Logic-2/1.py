def make_bricks(small, big, goal): 
    number_of_fives = goal/5
    number_of_ones = goal - (5*number_of_fives)
    if number_of_fives <= big and number_of_ones <= small:
        return True
    elif (number_of_ones+5<=small) and (big*5 + number_of_ones + 5 == goal):
        return True
    else:
        return False
