# Function to find and list all substrings in a string
def find_all(string, x):
    index_list = []
    start = 0
    while True:
        index = string.find(x, start)
        if index != -1:
            index_list.append(index)
            start = index+1
        else:
            break
    return index_list
print (find_all("atra ajta", "a"))