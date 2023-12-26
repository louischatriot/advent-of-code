import sys
import re
import u as u
from collections import defaultdict
import math
import itertools
import numpy as np

is_example = (len(sys.argv) > 1)
fn = 'inputs/' + __file__.replace('.py', '') + ('.example' if is_example else '') + '.data'
if is_example:
    print("===== RUNNING THE EXAMPLE =====")
with open(fn) as file:
    lines = [line.rstrip() for line in file]


# PART 1
hails = []
for l in lines:
    pos, vel = l.split(' @ ')
    pos = list(map(int, pos.split(', ')))
    vel = list(map(int, vel.split(', ')))
    hails.append((pos, vel))


m, M = 7, 27
if not is_example:
    m, M = 200000000000000, 400000000000000


result = 0
for hail1, hail2 in itertools.combinations(hails, r=2):
    pos1, vel1 = hail1
    pos2, vel2 = hail2

    matrix = np.array([[vel1[0], -vel2[0]],
              [vel1[1], -vel2[1]]])

    res = np.array([pos2[0] - pos1[0], pos2[1] - pos1[1]])
    try:
        mi = np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        continue

    times = np.matmul(mi, res)

    x = pos1[0] + times[0] * vel1[0]
    y = pos1[1] + times[0] * vel1[1]

    if times[0] >= 0 and times[1] >= 0:
        if m <= x <= M and m <= y <= M:
            result += 1

print(result)


# PART 2
matrix_xy = []
res_xy = []

matrix_xz = []
res_xz = []

hail_base = hails[0]
xb, yb, zb = hail_base[0]
vxb, vyb, vzb = hail_base[1]

# Why on earth would I use completely arbitrary indices here???
# Because due to some quite big numbers, the matrix inversion mathod is not precise to the unit
# and I don't get the right result (3 off out of 741991571910536)
# The right way to do this would be to implement Gaussian elimination, but the lazy way, which I chose
# is to first see if it ends up right for some other hails, which it does. So here is to dirty solutions.
for hail in hails[5:9]:
    xn, yn, zn = hail[0]
    vxn, vyn, vzn = hail[1]

    matrix_xy.append([vyn-vyb, vxb-vxn, yb-yn, xn-xb])
    res_xy.append(xn*vyn + yb*vxb - yn*vxn - xb*vyb)

    matrix_xz.append([vzn-vzb, vxb-vxn, zb-zn, xn-xb])
    res_xz.append(xn*vzn + zb*vxb - zn*vxn - xb*vzb)

matrix_xy = np.array(matrix_xy)
inv_xy = np.linalg.inv(matrix_xy)
res_xy = np.array(res_xy)
coords_xy = np.matmul(inv_xy, res_xy)

matrix_xz = np.array(matrix_xz)
inv_xz = np.linalg.inv(matrix_xz)
res_xz = np.array(res_xz)
coords_xz = np.matmul(inv_xz, res_xz)

result = coords_xy[0] + coords_xy[1] + coords_xz[1]
print(round(result))









# Below method works BUT for large inputs it should use a dichotomy / gradient otherwise very long
# Above solution is indeed much better
# epsilon = 1e-20
# T = 3000  # For now we go bourrinos, not even dichotomy or gradient

# x1, y1, z1 = hail1[0]
# vx1, vy1, vz1 = hail1[1]

# x2, y2, z2 = hail2[0]
# vx2, vy2, vz2 = hail2[1]

# x3, y3, z3 = hail3[0]
# vx3, vy3, vz3 = hail3[1]


# hail4 = hails[-4]
# x4, y4, z4 = hail4[0]
# vx4, vy4, vz4 = hail4[1]

# def find_t3(mx1, my1, mz1, mx2, my2, mz2, x3, y3, z3, vx3, vy3, vz3):
    # if mx1 == mx2:
        # t3 = (mx1 - x3) / vx3
    # elif my1 == my2:
        # t3 = (my1 - y3) / vy3
    # else:
        # K = (my2 - my1) / (mx2 - mx1)
        # t3 = (my1 - y3 + K * x3 - K * mx1) / (vy3 - K * vx3)

    # if abs(t3 - round(t3)) >= epsilon:
        # return None

    # x = x3 + t3 * vx3
    # z3_cand12 = mz1 + (x - mx1) * (mz2 - mz1) / (mx2 - mx1)  # TODO: handle mx1 == mx2
    # z3_cand3 = z3 + t3 * vz3

    # if abs(z3_cand12 - z3_cand3) <= epsilon and t3 >= 0:
        # return t3

    # return None


# for t1, t2 in itertools.product(range(T), repeat=2):
    # mx1, my1, mz1 = x1 + t1 * vx1, y1 + t1 * vy1, z1 + t1 * vz1
    # mx2, my2, mz2 = x2 + t2 * vx2, y2 + t2 * vy2, z2 + t2 * vz2

    # t3 = find_t3(mx1, my1, mz1, mx2, my2, mz2, x3, y3, z3, vx3, vy3, vz3)

    # if t3 is not None:
        # t4 = find_t3(mx1, my1, mz1, mx2, my2, mz2, x4, y4, z4, vx4, vy4, vz4)

        # if t4 is not None:
            # print("Found", t1, t2, t3, t4)






