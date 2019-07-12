# can't get input without sys. So i guess that's a built in library?
import sys

vocals = ['a','e','i','o','u']
vocalsu = ['A','E','I','O','U']
voc_len = 4

def something(text):
    i = 0
    la_list = []
    # loop through each letter in string
    while check_valid_index(text, i):
        c = text[i]
        # check if c is vocal
        if c in vocals or c in vocalsu:
            # Decide if uppercase or lowercase
            if c in vocals: la_list = vocals
            else: la_list = vocalsu
            # perform binary search
            vocal_index = find_index(la_list, c, 0, voc_len)
            # if u or U substitute for a or A
            if la_list[vocal_index] == la_list[-1]: vocal_index = 0
            # in any other case go to next vocal in list
            else: vocal_index +=1
            # rewrite text
            text = text[:i] + la_list[vocal_index] + text[i+1:]
        i += 1
    return text


# finds index of first occurance using binary search by ascii values
def find_index(dalist, d, lo, hi):
    while lo < hi:
        mid = (lo+hi)//2
        if dalist[mid] < d: lo = mid+1
        else: hi = mid
    return lo

# checks if index exists in collection by failing if not
def check_valid_index(ar, i):
    try:
        ar[i]
        return True
    except IndexError:
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        # My guess is that the print and exit functions don't count
        # mostly because both are c functions built into python and
        # print is here https://github.com/python/cpython/blob/762f93ff2efd6b7ef0177cad57939c0ab2002eac/Python/bltinmodule.c#L1820
        # exit is here https://github.com/python/cpython/blob/69150669f224a1fc47de483557736e725ac5b2a1/Python/clinic/sysmodule.c.h#L129
        print("There is no string for argument. Please input a string")
        exit()
    printable = sys.argv[1]
    arg_in = 2
    while check_valid_index(sys.argv, arg_in):
        printable = printable + sys.argv[arg_in]
        if check_valid_index(sys.argv, arg_in+1):
            printable = printable + ' '
        arg_in += 1
    printable = something(' '.join(sys.argv[1:]))
    print(printable)
    exit()