
# yuanxing2018  python3  utf-8
# 问题描述
# 给定一个整数 n ，你需要找到与它最近的回文数（不包括自身）。
# “最近的”定义为两个整数差的绝对值最小。
# 示例 1:
# 输入: "123"
# 输出: "121"
# 注意:
# n 是由字符串表示的正整数，其长度不超过18。
# 如果有多个结果，返回最小的那个。


# 基本完成了主要的  是以我们人类大脑看到一个数字然后判断的情况来写的这个流程
# 可能有疏漏 而且代码很烂 我也是初学者 想了很久  Leetcode上面击败了100%的python
# 当然 聪明的人能看出 还有一小部分n 不能正常返回 但是可以继续增加条件判断就行了
# 其实我感觉代码可以写的很好看 很顺畅的  只是最开始想得太简单了
# 也不想再重新弄整个结构了 所以 就每次提交测试 有不对的就改 哈哈 显得很痈肿。。
# 不过效率还是很高的～

# --------------------从这往下的可以直接复制进LeedCode
class Solution:
    # 不知道为什么写了很多注释反而不能通过了！
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
# ---------------------------------------从这往上的可以直接复制进LeedCode


#------------------------------------------ 这里是解释版
class Solution1(object):

    def find_num(self, n1):

        length = len(n1)  # 长度
        list1 = []
        for i in n1:  # 字符串转list
            list1.append(int(i))

        # 这个if判断 针对于 9 99 999 9999 .. 这类特殊情况
        if len(list(set(list1))) == 1 and list(set(list1))[0] == 9:  # 去重以后长度为1 且 只有一个元素 9
            lis_len = len(list1)   # 看看多长
            if lis_len == 1:
                return '8'   # 9 直接返回 8
            else:
                return str(int(n1) + 2)  # 99，999，9999要返回101，1001，10001  直接+2就可以了

        # 这个if判断 针对 100，1000，1000....这类特殊情况
        # 只有第一位是1 且  1后面的元素去重以后是0
        if list1[0] == 1 and length > 1 and list(set(list1[1:]))[0] == 0 and len(list(set(list1[1:]))) == 1:
            return str(int(n1) - 1)

        # 针对 101  1001 10001  这类特殊情况
        # 就判断他是不是 100+1 就行了 但是还要排除 2 这个可能
        if int(n1) == 1*10**(length - 1)+1 and n1 != '2':
            return str(int(n1) - 2)  # 直接 -2

        # n长度为1，2 的情况
        if length < 3:

            if n1[::-1] == n1:  # 如果是回文数（倒序和正序一样）
                if length == 1:
                    return str(int(n1) - 1)   # 这属于 12345678 这类直接-1
                else:
                    if n1 == '11':  # 2位数的回文数11 很特殊  直接返回9
                        return '9'
                    return str(int(n1) - 11)   # 其他情况就是 22  33  44 这类  直接 -11  另外 99 不算在内 在最开始就处理了
            else:  # 如果不是回文数
                if n1 == '10':
                    return '9'
                else:
                    return n1[0] + n1[0]   # 两位数的非回文数 13  35  89 这类 最近的就是  第二位和第一位相同的
        else:  # n长度为3和3以上的情况

            if n1[::-1] == n1:  # 如果n倒叙排序=n 那么n是回文数

                if length % 2 == 0:  # 长度是偶数

                    # 把最中间的两位数-11，如“123321”直接把最中间的33 -11
                    return str(int(n1) - 11 * 10 ** (length // 2 - 1))

                else:  # 长度是奇数

                    if n1[length // 2] == '0':  # 长度是奇数的这里又有一些比较特殊的 如 1110111
                        return str(int(n1) + 1 * 10 ** (length // 2))  # 最中间0 + 1

                    else:  # 最中间的那位数 -1 ，如“1234321”直接把最中间的4 -1         **但有一类情况没有处理到 如19991
                        return str(int(n1) - 1 * 10 ** (length // 2))

            else:  # 不是回文数

                if length % 2 == 0:  # 长度是偶数
                    left = n1[:length // 2]  # 取出最左边的数 如“123456” 取出123
                    left_r = left[::-1]  # 将其倒叙排序
                    x = left + left_r  # 字符串拼接  最左边 + 最左边的倒叙  123456>> 123321
                    y1 = n1[:(length // 2 - 1)] + str(int(n1[length // 2 - 1]) + 1)  # 123456>> 124
                    y1 = y1 + y1[::-1]    # 124>> 124421
                    y2 = str(int(x)-11*10**(length//2-1))    # 123456>>  122221
                    # 比较 y1 y2  哪个 合适
                    if abs(int(y1)-int(n1)) > abs(int(y2) - int(n1)):
                        y = y2
                    else:
                        y = y1
                    abx = abs(int(x) - int(n1))
                    aby = abs(int(y) - int(n1))
                    # 比较 x  y  哪个 合适
                    if abx > aby:
                        return str(y)
                    elif abx == aby:
                        if x < y:
                            return str(x)
                        else:
                            return str(y)
                    else:
                        return str(x)

                else:  # 长度是奇数
                    # 这里的思路和上面偶数的思路基本相同
                    left = n1[:length // 2]  # 取出中界最左边的数 如“12345” 取出12
                    left_r = left[::-1]  # 将其倒叙排序
                    mid = n1[length // 2]  # 中界
                    x = left + mid + left_r  # 结果拼起来  最左边 + 中界 + 最左边的倒叙

                    y1 = left + str(int(mid)+1) + left_r
                    y2 = left + str(int(mid)-1) + left_r
                    if abs(int(y1)-int(n1)) > abs(int(y2) - int(n1)):
                        y = y2
                    else:
                        y = y1
                    abx = abs(int(x) - int(n1))
                    print(abx)
                    aby = abs(int(y) - int(n1))
                    if abx > aby:
                        return str(y)
                    elif abx == aby:
                        if x < y:
                            return str(x)
                        else:
                            return str(y)
                    else:
                        return str(x)


# n的值
n = "1010101"
s = Solution1()
print(n)
print(s.find_num(n))
