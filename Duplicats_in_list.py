# I have a list with duplicates inside , I have to remove the duplicates and keep the order of the list , normally anyone will turn the list into set as set revmoves duplicates and then turn it into a list .But the problem is that set don't mantain order so there won't be any order in the list. there is an easy solution to this by making a new empty list and with for loop check the given list and check if there is any item of the given list is in the empty list . If not then append the item in the empty list .
# But there is another claver way to do this, by turning the list into dictionary with the values of the given list as keys , and as dictionary keys shouldbe unique so there won't be any duplicates . so we only want the keys here and then we can turn the keys into a list .

li = ['a','b','a','c','b','a']

new = list(dict.fromkeys(li).keys())
print(new)