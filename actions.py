"""
Dummy class for testing functionality of funcion 'next_action'
"""
class dummy_object:
    action_cost=0
    base_cost=0
    name=""
    ready_to_action=False
    def __init__(self,name, cost):
        self.cost=cost
        self.base_cost=cost
        self.name=name
    def do_action(self):
        print(self.name+" did something")

"""
Sorting list of objects by actual action cost and then recursivly do actions in
a query until player will take his turn
"""
def next_action(list1, i=0):
    i = i+1
    list1.sort(key = lambda x : x.cost)
    list1[0].do_action()
    minus_cost = list1[0].cost
    for item2 in list1:
        item2.cost -=  minus_cost
    list1[0].cost = list1[0].base_cost
    if list1[0].name != 'Hero' and i < 10:
          next_action(list1, i)

#Some nasty test
list1 = [dummy_object("John",50), dummy_object("Joe",20),
         dummy_object("Alex",20),dummy_object("Hero",40)]
next_action(list1)
next_action(list1)
next_action(list1)
next_action(list1)
