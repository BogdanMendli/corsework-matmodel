from math import sqrt
import matplotlib.pyplot as plt


def frange(froom, to, step):
    while froom < to:
        yield froom
        froom += step


def solve_system(p2, p3, p5):
    res = {'x1': [], 'x2': [], 'p1': [], 'p4': []}
    for x1 in frange(0.1, 1.3, 0.01):
        a = -1
        b = -1 + 2 * x1 + ((1 + x1 ** p3) * p3 * x1 ** p3 * ((1 + x1 ** p3) - (p5 + x1 ** p3))) / \
            ((p5 + x1 ** p3) * ((1 + x1 ** p3) ** 2))
        c = x1 * (1 - p2 - x1) + (p3 * x1 ** (p3 + 1) * (p2 - 1) * (1 + x1 ** p3) * ((1 + x1 ** p3) - (p5 + x1 ** p3))) / \
            ((p5 + x1 ** p3) * ((1 + x1 ** p3) ** 2))


        discriminant = (b ** 2 - 4 * a * c)
        if discriminant >= 0:
            lambda_1 = (- b + sqrt(discriminant)) / (2 * a)
            lambda_2 = (- b - sqrt(discriminant)) / (2 * a)

            if lambda_1 > 0:
                x2 = x1 * p2 / (lambda_1 - x1)
                if x2 > 0:
                    p1 = x1 * (1 + x2) * (1 + x1 ** p3) / (p5 + x1 ** p3)
                    if p1 > 0:
                        if not (x1 == lambda_1 and x1 * x2 == 0):
                            res['x1'].append(x1)
                            res['x2'].append(x2)
                            res['p1'].append(p1)
                            res['p4'].append(lambda_1)
            if lambda_2 >= 0:
                x2 = x1 * p2 / (lambda_2 - x1)
                if x2 > 0:
                    p1 = x1 * (1 + x2) * (1 + x1 ** p3) / (p5 + x1 ** p3)
                    if p1 > 0:
                        if not (x1 == lambda_2 and x1 * x2 == 0):
                            res['x1'].append(x1)
                            res['x2'].append(x2)
                            res['p1'].append(p1)
                            res['p4'].append(lambda_2)

    print 'x1\t\t\tx2\t\t\t\tp1\t\t\t\t\tp4\t\t\t\tcheck\t\t\tlambda1\t\t\t\tlambda2'
    result1 = {'x1': [], 'x2': [], 'p1': [], 'p4': []}
    result2 = {'x1': [], 'x2': [], 'p1': [], 'p4': []}
    for i in range(0, len(res['x1']), 1):
        aa = 1
        bb = 0 - (((res['p1'][i] * p3 * res['x1'][i] ** (p3 - 1) * ((1 + res['x1'][i] ** p3) - (p5 + res['x1'][i] ** p3))) / ((1 + res['x1'][i] ** p3) ** 2)) - (1 + res['x2'][i])) \
            - (res['x1'][i] - res['p4'][i])
        cc = (((res['p1'][i] * p3 * res['x1'][i] ** (p3 - 1) * ((1 + res['x1'][i] ** p3) - (p5 + res['x1'][i] ** p3))) / ((1 + res['x1'][i] ** p3) ** 2)) - (1 + res['x2'][i])) \
            * (res['x1'][i] - res['p4'][i]) + res['x1'][i] * (p2 + res['x2'][i])
        discriminant = (bb ** 2 - 4 * aa * cc)
        if discriminant >= 0:
            lambda_1 = (- bb + sqrt(discriminant)) / (2 * aa)
            lambda_2 = (- bb - sqrt(discriminant)) / (2 * aa)
            # print 'd >= 0 ', '%0.2f' % res['x1'][i], '  ', '%0.10f' % lambda_1, ' ', '%0.10f' % lambda_2
            result1['x1'].append(res['x1'][i])
            result1['x2'].append(res['x2'][i])
            result1['p1'].append(res['p1'][i])
            result1['p4'].append(res['p4'][i])
        else:
            # print 'd < 0 ', '%0.2f' % res['x1'][i], '  ', ((- bb) / (2 * aa)), '  ', '%0.5f' % sqrt(-discriminant)
            result2['x1'].append(res['x1'][i])
            result2['x2'].append(res['x2'][i])
            result2['p1'].append(res['p1'][i])
            result2['p4'].append(res['p4'][i])

        print '%0.2f' % res['x1'][i], '  ', '%0.8f' % res['x2'][i], '  ', \
            '%0.8f' % res['p1'][i], '  ', '%0.8f' % res['p4'][i], '  ', \
            (res['p1'][i] * p3 * res['x1'][i] ** (p3 - 1) * (1 + res['x1'][i] ** p3) - res['p1'][i] * (
                    p5 + res['x1'][i] ** p3) * p3 * res['x1'][i] ** (p3 - 1)) / \
            ((1 + res['x1'][i] ** p3) ** 2) - (1 + res['x2'][i]) + res['x1'][i] - res['p4'][i]
    plt.title(u'Bifurcation diagram')
    plt.xlabel('p4')
    plt.ylabel('p1')
    plt.plot(result2['p4'], result2['p1'], 'g.')
    plt.plot(result1['p4'], result1['p1'], 'y.')
    plt.xlim(0, 3)
    plt.ylim(0, 30)
    plt.show()

    return res


result = solve_system(1.5, 3, 0.01)

# plt.title(u'Bifurcation diagram')
# plt.xlabel('p4')
# plt.ylabel('p1')
# plt.plot(result['p4'], result['p1'], 'r.')
# plt.xlim(0, 5)
# plt.ylim(0, 25)
#
# plt.show()