# -*- coding:utf-8 -*-

def is_power(a,b,count): 
    """再帰的にべき乗判定する関数 3番目の引数には０を代入"""
    if a%b == 0:
        count+=1
        is_power(a//b, b, count)
    else:
        if a==1:
            if count == 1:
                print("{0} is the {1}st power of {2}".format(b**count, count, b))
            elif count == 2:
                print("{0} is the {1}nd power of {2}".format(b**count, count, b))
            elif count == 3:
                print("{0} is the {1}rd power of {2}".format(b**count, count, b))
            else:    
                print("{0} is the {1}th power of {2}".format(b**count, count, b))
            
        else:
            print("{0} is not a power of {1}".format(a*(b**count),b))

def is_power_nr(a,b): 
    """非再帰的にべき乗判定する関数"""
    count = 0
    if a == b:
        print("a = b")
    elif a < b:
        print("a is not power of b.")
    else:
        while(a>b):
            if a%b == 0:
                a = a//b
                count += 1
                if a == b:
                    count+=1
                    if count == 1:
                        print("{0} is the {1}st power of {2}".format(b**count, count, b))
                    elif count == 2:
                        print("{0} is the {1}nd power of {2}".format(b**count, count, b))
                    elif count == 3:
                        print("{0} is the {1}rd power of {2}".format(b**count, count, b))
                    else:    
                        print("{0} is the {1}th power of {2}".format(b**count, count, b))
            else:
                print("{0} is not a power of {1}.".format(a*(b**count),b))
                break
            
            
            
            
            

if __name__ == "__main__":
    is_power(16,4,0) 
    is_power_nr(16,2)