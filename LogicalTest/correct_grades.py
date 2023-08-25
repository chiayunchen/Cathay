'''
國泰補習班中，有五位學生期中考的成績分別為[53, 64, 75, 19, 92]
但是老師在輸入成績的時候看反了，把五位學生的成績改成了[35, 46, 57, 91, 29]
請用一個函數來將學生的成績修正。

輸入: [35, 46, 57, 91, 29]
輸出: [53, 64, 75, 19, 92]
'''

def correct_grades(input: list[int]) -> list[int]:
    if len(input) == 0:             #沒輸入可處理資料，退出程式
        print(f'Please input data.')
        return None
    
    output = []
    for i in input:
        temp = str(i)               #把int轉成string
        if not temp.isnumeric():    #若有非數字輸入，不予處理並提醒使用者
            print(f'"{temp}" is not a number, please check and input again.')
            continue
        output.append(int(temp[::-1]))  #把string順序反轉之後，再轉回數字
    print(output)
    return output

assert correct_grades([35, 46, 57, 91, 29]) == [53, 64, 75, 19, 92]
assert correct_grades([135, 146, 157, 191, 129]) == [531, 641, 751, 191, 921]
assert correct_grades([]) == None
assert correct_grades(['try', 55, 23, 30, 98]) == [55, 32, 3, 89]