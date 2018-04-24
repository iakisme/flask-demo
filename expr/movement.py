from sympy import *


def cal_movement(_a, _b, _r0, _r1):
    r0, r1, a, b = symbols("r0,r1,a,b")
    pararm = {a: (pi * _a) / 180, b: (pi * _b) / 180, r0: _r0, r1: _r1}

    before_left = pi * tan(b) * tan(a)
    before_right = (r0 - r1) / (r0 + r1)

    ra = r0 * (-pi * tan(a) * tan(b) + 1) / (pi * tan(a) * tan(b) + 1)
    t1 = (5 * r0 ** 4 - 3 * r0 ** 2 * ra ** 2 + 6 * r0 ** 2 * (r0 + ra) ** 2 * ln(
        (r0 + ra) / (2 * r0)) - 2 * r0 * ra ** 3) / (3 * pi * r0 ** 2 * (r0 + ra) * tan(b) * tan(a) ** 2)
    y1 = (r0 - ra) / (tan(b) * tan(a))
    rb = r0 * (2 * r1 + (r0 + r1) * pi * tan(b) * tan(a)) / (2 * r0 - (r0 + r1) * pi * tan(b) * tan(a))
    t2 = (3 * r1 ** 2 * rb ** 2 - 2 * r1 * rb ** 3 - r1 ** 4) / (
        3 * pi * r0 ** 2 * (r0 + r1) * tan(b) * tan(a) ** 2) + (2 * (r0 + rb) ** 3 - 2 * (r0 + r1) ** 3 - 9 * r0 * (
        rb ** 2 - r1 ** 2) - 3 * r1 * (r0 - rb) ** 2 + 3 * r1 * (r0 - r1) ** 2 + 6 * r0 ** 2 * (r0 + r1) * ln(
        (r0 + r1) / (r0 + rb))) / (3 * pi * (r0 ** 2) * tan(b) * tan(a) ** 2) + (4 * (r0 ** 3 - rb ** 3) - 3 * (
        rb + r1) * (r0 ** 2 - rb ** 2)) / (6 * r0 ** 2 * tan(a))
    y2 = (r0 - r1) / (tan(b) * tan(a))
    e1 = (pi * (r0 + r1) * tan(b)) / 2
    t3 = (4 * r0 ** 3 - 6 * r0 ** 2 * r1 + 2 * r1 ** 3) / (6 * r0 ** 2 * tan(a)) + e1 * (r0 ** 2 - r1 ** 2) / (
        2 * r0 ** 2)
    y3 = (r0 - r1) / (tan(a) * tan(b)) + pi * (r0 + r1) / 2

    t5 = (5 * r0 ** 4 - 3 * r0 ** 2 * r1 ** 2 - 2 * r0 * r1 ** 3 + 6 * r0 ** 2 * (r0 + r1) ** 2 * ln(
        (r0 + r1) / (2 * r0))) / (3 * pi * r0 ** 2 * (r0 + r1) * tan(b) * tan(a) ** 2)
    y5 = (r0 - r1) / (tan(a) * tan(b))

    rc = r0 * (2 * r1 + (r0 + r1) * pi * tan(a) * tan(b)) / (2 * r0 - (r0 + r1) * pi * tan(b) * tan(a))
    e2 = (pi / 2) * (r0 + r1) * tan(b) - ((r0 - r1) * r0) / (2 * r0 * tan(a))
    t6 = ((e2 * tan(a) - r1) / (3 * pi * r0 ** 2 * (r0 + r1) * tan(b) * tan(a) ** 2)) * (
        3 * (e2 * tan(a) - r1) * (r0 ** 2 - r1 ** 2) + 2 * (r0 ** 3 - r1 ** 3)) - (
                                                                                      e2 / (pi * r0 ** 2 * tan(b) * tan(
                                                                                          a))) * (
                                                                                      (r0 - r1) ** 2 + 2 * r0 ** 2 * ln(
                                                                                          (r0 + r1) / (2 * r0))) + (
                                                                                                                       16 * r0 ** 3 - 2 * (
                                                                                                                           r0 + r1) ** 3 - 9 * r0 * (
                                                                                                                           r0 ** 2 - r1 ** 2) + 3 * r1 * (
                                                                                                                           r0 - r1) ** 2 + 6 * r0 ** 2 * (
                                                                                                                           r0 + r1) * ln(
                                                                                                                           (
                                                                                                                               r0 + r1) / (
                                                                                                                               2 * r0))) / (
                                                                                                                       3 * pi * r0 ** 2 * tan(
                                                                                                                           b) * tan(
                                                                                                                           a) ** 2)
    y6 = (r0 - r1) / (tan(b) * tan(a)) + (pi * (r0 + r1)) / 2 - ((r0 - r1) * r0) / (2 * r0 * tan(b) * tan(a))
    e3 = (pi * (r0 + r1) * tan(b)) / 2
    t7 = (4 * r0 ** 3 - 6 * r0 ** 2 * r1 + 2 * r1 ** 3) / (6 * r0 ** 2 * tan(a)) + (e3 * (r0 ** 2 - r1 ** 2)) / (
        2 * r0 ** 2)
    y7 = (r0 - r1) / (tan(b) * tan(a)) + (pi * (r0 + r1)) / 2
    e4 = (pi / 2) * (r0 + r1) * tan(b)

    t4 = (e4 / r0 ** 2) * (r0 ** 2 - r1 ** 2) - (pi * tan(b) * (r0 + r1) * (r0 ** 2 - r1 ** 2)) / (4 * r0 ** 2) + (
                                                                                                                      2 * r0 ** 3 - 3 * r0 ** 2 * r1 + r1 ** 3) / (
                                                                                                                      3 * r0 ** 2 * tan(
                                                                                                                          a))
    y4 = (e4 + (r0 - r1) * cot(a)) * cot(b)

    left = [ra, t1, y1, rb, t2, y2, e1, t3, y3, t4, y4]

    right = [rc, e2, t6, y6, e3, t7, y7, e4, t5, y5, t4, y4]

    flag = False
    if before_left.evalf(subs=pararm) > before_right.evalf(subs=pararm):
        flag = True
    if not flag:
        ra_result = ra.evalf(subs=pararm)
        t1_result = t1.evalf(subs=pararm)
        y1_result = y1.evalf(subs=pararm)
        rb_result = rb.evalf(subs=pararm)
        t2_result = t2.evalf(subs=pararm)
        y2_result = y2.evalf(subs=pararm)
        e1_result = e1.evalf(subs=pararm)
        t3_result = t3.evalf(subs=pararm)
        y3_result = y3.evalf(subs=pararm)
        t4_result = t4.evalf(subs=pararm)
        y4_result = y4.evalf(subs=pararm)

        result_left = {
            "判断": "否，左边逻辑",
            "r'a": ra_result,
            "t1": t1_result,
            "y1": y1_result,
            "rb": rb_result,
            "t2": t2_result,
            "y2": y2_result,
            "e1": e1_result,
            "t3": t3_result,
            "y3": y3_result,
            "y4": y4_result,
            "t4": t4_result,
        }
        return {k: round(v, 5) for k, v in result_left.items()}
    else:
        rc_result = rc.evalf(subs=pararm)
        e2_result = e2.evalf(subs=pararm)
        t6_result = t6.evalf(subs=pararm)
        y6_result = y6.evalf(subs=pararm)
        e3_result = e3.evalf(subs=pararm)
        t7_result = t7.evalf(subs=pararm)
        y7_result = y7.evalf(subs=pararm)
        e4_result = e4.evalf(subs=pararm)
        t5_result = t5.evalf(subs=pararm)
        y5_result = y5.evalf(subs=pararm)
        y4_result = y4.evalf(subs=pararm)
        t4_result = t4.evalf(subs=pararm)

        result_right = {
            "判断": "是，右边逻辑",
            "r'c": rc_result,
            "e2": e2_result,
            "y'1": y5_result,
            "t'1": t5_result,
            "t'2": t6_result,
            "y'2": y6_result,
            "e3": e3_result,
            "t'3": t7_result,
            "y'3": y7_result,
            "e4": e4_result,
            "y4": y4_result,
            "t4": t4_result,
        }
        return {k: round(v, 5) for k, v in result_right.items()}
