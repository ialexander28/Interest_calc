import math

def total_value():

    years = input('how many %s?' %('years'))
    amount = input('how much money?')
    additions = input('how much contributed after first year?')
    year_1 = (math.exp(.07)) * amount
    new_addition = (year_1 + additions)
    year_2 = (math.exp(.07)) * new_addition
    second_addition = input('How much contributed after second year?')

    if years == 1:
        print 'First year value :', year_1
    elif years == 2:
        print 'Second year value :', year_2
    elif years == 3:
        second_addition = input('How much contributed after second year?')
        print 'Value after ' + str(years) + ' years:', (year_2 + second_addition) * (math.exp(.07))
    elif years == 4:
        year_3 = (year_2 + second_addition) * (math.exp(.07))
        third_addition = input('How much contributed after third year?')
        print 'Value after' + str('%s' % ('years')) + ' years:', (year_3 + third_addition) * (math.exp(.07))

    return

total_value()
