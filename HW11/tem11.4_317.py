import sys
sys.set_int_max_str_digits(0)
def kara(x,y):
    x = str(x)
    y = str(y)

    if len(x) == 1 or len(y) == 1:
        return str(int(x) * int(y))

    while len(x) != len(y):
        if len(x) < len(y):
            x = "0" + x
        else:
            y = "0" + y

    n = len(x)
    m = n//2

    a = x[:n-m]
    b = x[n-m:]
    c = y[:n-m]
    d = y[n-m:]

    ac = int(kara(a,c))
    bd = int(kara(b,d))
    ab_cd = int(kara(str(int(a) + int(b)), str(int(c) + int(d))))

    ad_bc = ab_cd - ac - bd

    result = ac * (10 ** (2 * m)) + ad_bc * (10 ** m) + bd

    return str(result)
A, B = input().split()

res = kara(A, B)

res = res.lstrip('0')
if res == '':
    res = '0'

print(res)