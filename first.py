

def anonymous_filter(some_list):
    sum_23 = 0
    for i in some_list:
        if i.isalpha():
            if i.lower() == 'я':
                sum_23 += 1
    return sum_23 >= 23


print(anonymous_filter('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))
