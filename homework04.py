
def max_len_word(words):
    d = dict()
    for c in words:
        d[c] = len(c)
        
    sorted_list = sorted(d.items(),key=lambda x:-x[1])
    print('long length words')
    for i in range(10):
        print(sorted_list[i])

def most_used_alphabet(words):
    
    d = dict()    
    for c in words:
        for cc in c:
            if cc not in d:
                d[cc] = 1
            else:
                d[cc]+=1 
                
    sorted_list = sorted(d.items(),key=lambda x:-x[1])
    print('most used letter is '+sorted_list[0][0]+' for '+str(sorted_list[0][1])+'times')
    
if __name__ == "__main__":
    words = [line.strip() for line in open('words.txt').readlines()]
    #most_used_alphabet(words)
    max_len_word(words)
