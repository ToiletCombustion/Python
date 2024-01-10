





def insertion_sort(items):
    n = len(items)
   
    for i in range (1,n):
        current = items[i]
        index2 = i
       




        while index2 > 0 and items[index2 - 1] > current:
            items[index2] = items[index2 - 1]
            index2 = index2 - 1
            items[index2] = current



    return items
   
items = ["Hamburger", "Fries", "Potato", "Bread", "Milk"]
print(insertion_sort(items))
