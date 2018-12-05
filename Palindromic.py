# 思路：分4种情况
# 1.n是回文数且是长度是奇数如“1234321”直接把最中间的4 替换为3

# 2.n是回文数且是长度是偶数如“123321”直接把最中间的33 替换为22

# 3.n不是回文数且长度是奇数如“12345” 直接把中间的3右边的45 让他等于最左边的12倒叙排列21  显然这样差的绝对值是最小的

# 4.n不是回文数且长度是偶数如“123456” 直接把最后3位（右边）的456 让他等于最左边的123的倒叙排列321 显然这样差的绝对值是最小的

# 还有一些特殊情况  比如 100  1000 100000 .... 和 9 99 999..   20002 1001
# n = 1  ,  99  100  11011  11911  10001  1283 12389  111111111  80001 -- 80008 79997

# print('s')
class Solution:

    def nearestPalindromic(self, n):
        length = len(n)
        list1 = []
        for i in n:
            list1.append(int(i))
        #print(list(set(list1)))
        # 针对9999
        if len(list(set(list1))) == 1 and list(set(list1))[0] == 9:
            lis_len = len(list1)
            if lis_len == 1:
                return '8'
            else:
                return str(int(n) + 2)

        # if list(set(list1))[1] == 0:
        #     pass
        # 只针对 100，1000，1000....
        if list1[0] == 1 and length > 1 and  list(set(list1[1:]))[0] == 0 and len(list(set(list1[1:]))) ==1:
            return str(int(n)-1)
        # 针对 10001  1001 10001
        #if list1[0] == 1 and length > 2 and  list1[length-1] == 1 and len(list(set(list1[1:length-1]))) == 1:
        if int(n) == 1*10**(length-1)+1 and n != '2':
            return str(int(n)-2)
        if length < 3 :
            if n[::-1] == n:
                if length == 1:
                    return str(int(n)-1)
                else:
                    if n == '11':
                        return '9'
                    return str(int(n)-11)
            else:
                if n == '10':
                    return '9'
                else:
                    return n[0] + n[0]
        else:

            if n[::-1] == n:  # 如果n倒叙排序=n 那么n是回文数

                if length % 2 == 0:  # 长度是偶数v

                    # 把最中间的两位数-11，如“123321”直接把最中间的33 -11
                    return str(int(n) - 11 * 10 ** (length // 2 - 1))



                else:  # 长度是奇数

                    if n[length // 2] == '0':
                        return str(int(n) + 1 * 10 ** (length // 2))  # + 'e'


                    # 最中间的那位数 -1 ，如“1234321”直接把最中间的4 -1
                    else:
                        return str(int(n) - 1 * 10 ** (length // 2))  # + 's'


            else:  # 不是回文数

                if length % 2 == 0:  # 长度是偶数
                    left = n[:length // 2]  # 取出最左边的数 如“123456” 取出123
                    left_r = left[::-1]  # 将其倒叙排序
                    x = left + left_r  # 字符串拼接  最左边 + 最左边的倒叙
                    y1 = n[:(length // 2-1)] + str(int(n[length // 2-1])+1)
                    y1 = y1 + y1[::-1]
                    y2 = str(int(x)-11*10**(length//2-1))
                    if abs(int(y1)-int(n)) > abs(int(y2)-int(n)):
                        y = y2
                    else:
                        y = y1
                    abx = abs(int(x) - int(n))
                    aby = abs(int(y) - int(n))

                    if abx > aby :
                        return str(y)
                    elif abx == aby:
                        if x < y:
                            return str(x)
                        else:
                            return str(y)
                    else:
                        return str(x)
                else:  # 长度是奇数
                    left = n[:length // 2]  # 取出中界最左边的数 如“12345” 取出12
                    left_r = left[::-1]  # 将其倒叙排序
                    mid = n[length // 2]  # 中界
                    x =  left + mid + left_r  # 结果拼起来  最左边 + 中界 + 最左边的倒叙

                    y1 =  left + str(int(mid)+1) + left_r
                    y2 =  left + str(int(mid)-1) + left_r
                    if abs(int(y1)-int(n)) > abs(int(y2)-int(n)):
                        y = y2
                    else:
                        y = y1
                    #print(y)
                    abx = abs(int(x) - int(n))
                    print(abx)
                    aby = abs(int(y) - int(n))
                    #print(aby)
                    if abx > aby :
                        return str(y)
                    elif abx == aby:
                        if x < y:
                            return str(x)
                        else:
                            return str(y)
                    else:
                        return str(x)

n = "123892133"  # >>>>>113311   ..  114411

s = Solution()
print(n)
print(s.nearestPalindromic(n))
