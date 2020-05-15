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
            if start==0:
                return -1
            else:
                return index_list
if __name__ == '__main__':
    print (find_all("blablabla", "a"))
    print(find_all("blablabla", "x"))