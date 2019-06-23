def NumberOf1(n):
    # write code here
    """https://www.nowcoder.com/questionTerminal/8ee967e43c2c4ec193b040ea7fbb10b8"""
    one_c = 0
    while n:
        y = n & 1
        if y == 1:
            one_c += 1
        n = n >> 1
    return one_c

def Power(base, exponent):
    """
    给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
    https://www.nowcoder.com/practice/1a834e5e3e1a4b7ba251417554e07c00?tpId=13&tqId=11165&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
    :param base:
    :param exponent:
    :return:
    """
    # write code here
    if base == 0:
        return 0

    def p_power(base, exponent):
        if exponent == 1:
            return base
        if exponent % 2 == 0:
            return p_power(base, int(exponent / 2)) * p_power(base, int(exponent / 2))
        else:
            return p_power(base, int(exponent / 2)) * p_power(base, int(exponent / 2)) * base

    if exponent > 0:
        return p_power(base, exponent)
    elif exponent < 0:
        return 1 / p_power(base, -1 * exponent)
    else:
        return 1




if __name__ == '__main__':
    flag = 1
