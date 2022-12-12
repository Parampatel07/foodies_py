number = ['one','two','three','four','five','six','seven','eight','nine','ten']
def divide_chunks(name_of_list, size_of_part):
    # looping till length l
    for i in range(0, len(name_of_list), size_of_part):
        yield name_of_list[i:i + size_of_part]
mylist= list(divide_chunks(number,3))        
print(mylist)