# -*- coding:utf-8 -*-

def is_power(a,b,count):
    if a%b == 0:
        count+=1
        print(count)
        is_power(a/b, b, count)
    else:
        if count > 0:
            print("{0} is the {1}th power of {2}".format(b**count, count, b))
            
        else:
            print("{0} is not a power of {1}".format(a,b))


if __name__ == "__main__":
    is_power(5,2,0)