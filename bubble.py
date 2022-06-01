x = [1,8,3,2]

def switch(list, pointer1, pointer2):
    pos1 = list[pointer1]
    pos2 = list[pointer2]
    list[pointer2] = pos1
    list[pointer1] = pos2
    return list

def bubble_sort(list):
    length = len(list)
    while True:
        switched = False
        for pointer in range(length-1):
            if list[pointer] > list[pointer+1]:
                list = switch(list, pointer, pointer+1)
                switched = True
        if not switched: break
    return list

print(bubble_sort(x))
