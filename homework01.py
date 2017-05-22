# -*- coding: utf-8 -*-
import numpy as np

OFF, ON = 0, 1

def dec2bin(n): #１０進数を２進数に変換
    bit_list = np.zeros(8)
    for i in range(8):
        bit_list[i] = n%2
        n = int(n/2)
    return bit_list

def ca(width, height, rulenum): #一次元セルオートマトンの配列生成
    results = np.zeros((height, width))
    first_row = np.zeros(width)
    first_row[int(width/2)] = ON #初期状態の設定
    results[0] = first_row
    #ルールの番号から次の状態のビット列を得る
    rule = dec2bin(rulenum)

    for i in range(1, height):
        old_row = results[i-1]
        new_row = np.zeros(width)
        for j in range(width):
            n = 4 * old_row[(j-1)%width] + 2 * old_row[j] + old_row[(j+1)%width]
            new_row[j] = rule[int(n)]
        results[i] = new_row
    return results

def render(results, width, height):
    #セルオートマトン
    for y in range(height):
        line = []
        for x in range(width):
            if results[y][x] == ON:
                character = "W"
            else:
                character = " "
            line.append(character)
        print("".join(line), end='\n')

if __name__ == "__main__":
    width, height = 75, 50
    rulenum = 210 #ルール番号
    results = ca(width, height, rulenum)
    render(results, width, height)
    
