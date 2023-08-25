'''
QA部門今天舉辦團康活動, 有n個人圍成一圈, 順序排號。
從第一個人開始報數(從1到3報數), 凡報到3的人退出圈子。
請利用一段程式計算出，最後留下的那位同事，是所有同事裡面的第幾順位?

輸入: n值(0-100)
輸出: 第幾順位
'''

def find_the_last_one(n: int) -> int:
    count = 3

    if n == 0:      #沒人玩，退出程式
        print(f'n = {n} - No one is playing the game.')
        return 0
    elif not str(n).isnumeric():    #輸入資料非數字，退出程式
        print(f'"{n}" is not a number, please check and input again.')
        return 0
    
    total = n
    r = [i for i in range(1, n+1)]
    while total > 1:                #迴圈執行到剩一個人為止
        for i in range(count-1):
            r.append(r.pop(0))      #算過的人，排到後面去
        r.pop(0)                    #算到3的那個人離開
        total -= 1                  #總人數減一
    print(f'n = {n} - With {n} people and count to {count}, the last one is No.{r[0]}')
    return r[0]

assert find_the_last_one(9) == 1
assert find_the_last_one(10) == 4
assert find_the_last_one(0) == 0
assert find_the_last_one('I want to play the game') == 0