def __greeting__():
    print('*' * 40)
    print('**     Welcome to the Snakes Cafe!    **')
    print('**     Please see our menu below.     **')
    print('**')
    print('** To quit at any time, type "quit"   **')
    print('*' * 40 + '\n')

    print("Appetizers")
    print("----------")
    print("Wings")
    print("Cookies")
    print("Spring Rolls\n")

    print("Entrees")
    print("-------")
    print("Salmon")
    print("Steak")
    print("Meat Tornado")
    print("A Literal Garden\n")


    print("Desserts")
    print("--------")
    print("Ice Cream")
    print("Cake")
    print("Pie\n")

    print("Drinks")
    print("------")
    print("Coffee")
    print("Tea")
    print("Unicorn Tears\n")

    print('*' * 35)
    print('** What would you like to order? **')
    print('*' * 35)

food = {
    'Wings': 0,
    'Cookies': 0,
    'Spring Rolls': 0,
    'Salmon': 0,
    'Steak': 0,
    'Meat Tornado': 0,
    'A Literal Garden' : 0,
    'Ice Cream': 0,
    'Cake' : 0,
    'Pie' : 0,
    'Coffee' : 0,
    'Tea': 0,
    'Unicorn Tears' : 0,
}



stopOrder = False
def __theOrder__():
    myOrder = input('> ')
    if myOrder == 'quit':
        global stopOrder
        stopOrder = True
    else:
        for item in food.keys():
            food[item] += 1
            amount = food[item]
        
        if amount == 1:
            print(f'**  ' + str(amount) + ' order of ' + myOrder + ' have been added to your meal**')
        
        elif amount > 1:
            print(f'**  ' + str(amount) + ' orders of ' + myOrder + ' have been added to your meal**')
__greeting__()
while stopOrder == False:
    __theOrder__()