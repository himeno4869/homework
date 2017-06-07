# -*- coding: utf-8 -*-

def max_len_word(words):
    '''文字数の多い単語を探す関数'''
    d = dict()
    for c in words:
        d[c] = len(c)
        
    sorted_list = sorted(d.items(),key=lambda x:-x[1])
    print('---longest length words(Top10)---')
    for i in range(10):
        print(sorted_list[i])
        
    print('''
    ''') 

def times_of_alphabet(words):
    '''アルファベット毎の出現回数'''
    d = dict()    
    for word in words:
        for letter in word:
            if letter not in d:
                d[letter] = 1
            else:
                d[letter]+=1 
                
    sorted_list = sorted(d.items(),key=lambda x:-x[1])
    print("---letter's number of times(decreasing order)---")
    print(sorted_list)
    print('''
    ''')
    
def most_used_length(words):
    '''何文字の単語が最も多いかを示す関数'''
    d = dict()
    for word in words:
        n = len(word)
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
            
    sorted_list = sorted(d.items(),key=lambda x:-x[1])
    print("most used word's length is "+str(sorted_list[0][0])+'('+str(sorted_list[0][1])+'words)')
    print('''
    ''')
    
def different_letter(words):
    '''同じ文字を含まない単語を探す関数'''
    d = dict()
    for word in words:
        letters = dict()
        boolean = 0 #同じ文字を含む単語かどうかの真理値
        for letter in word:
            if letter not in letters:
                letters[letter] = 1
            else:
                boolean = 1 #同じ文字を含む単語
        if boolean == 0:
            d[word] = len(word)
            
    sorted_list = sorted(d.items(),key=lambda x:-x[1])
    print("---the longest word in which all different letters are used---")    
    print('word: '+sorted_list[0][0])
    print('length: '+str(sorted_list[0][1]))

if __name__ == "__main__":
    words = [line.strip() for line in open('words.txt').readlines()]
    times_of_alphabet(words)
    max_len_word(words)
    most_used_length(words)
    different_letter(words)