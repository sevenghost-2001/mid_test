#  Bài 1 (6đ).

# 1. Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bàn phím.

# 2. Viết chương trình nhập vào một số nguyên dương, tính tổng các chữ số của nó.

# 3. Viết hàm đếm số lần xuất hiện các ký tự trong một String.
# s =  str(input('nhập vào một chuỗi: '))
# print('ký tự lớn nhất là {} \n ký tự nhỏ nhất là {}'.format(max(s),min(s)))
# a = int(input('nhập vào một số nguyên dương '))
# sum = 0
# tmp = 0
# while a > 1 :
#     tmp = int(a % 10)
#     a = a /10
#     sum = sum + tmp
# print('tổng các chữ số có trong 1 số nguyên dương là ',sum)
s = str(input('nhập 1 chuỗi: '))

for i in range(len(s)):
    n = 0
    for j in range(len(s)):
        if s[i] == s[j] :
            n = n + 1
    print('{} : {}'.format(s[i],n))

