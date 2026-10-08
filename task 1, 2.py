import numpy as np
from math import *
import altair as alt

alt.renderers.enable("browser")

#==================TASK1=========================================

def stretch(X,a,b):
    newx = matrixtransformer(X)
    STR = np.array([[a, 0],[0,b],])
    print("Stretch matrix:\n", STR)
    return matrixtransformer(STR @ newx)

def shear(X,a,b):
    newx = matrixtransformer(X)
    SHR = np.array([[1, a], [b, 1], ])
    print("Shear matrix:\n", SHR)
    return matrixtransformer(SHR @ newx)

def reflection(X,a,b):
    newx = matrixtransformer(X)
    REF = np.array([
    [a**2 - b**2, 2*a*b],
    [2*a*b, b**2 - a**2]
    ], dtype=float) / (a**2 + b**2)
    print("Reflection matrix:\n", REF)
    return matrixtransformer(REF @ newx)

def rotation(X,angle):
    newx = matrixtransformer(X)
    ROT = np.array([[cos(angle), -sin(angle)], [sin(angle), cos(angle)]])
    print("Rotation matrix:\n", ROT)
    return matrixtransformer(ROT @ newx)

def matrixtransformer(A):
    return A.T.copy()


def showimage(image):
    data1 = alt.Data(values=[
        {"x": float(x), "y": float(y), "i": i}
        for i, (x, y) in enumerate(image)
    ])

    scale = alt.Scale(domain=[-1000, 1000], nice=False)

    chart = alt.Chart(data1).mark_line(
        interpolate="linear-closed"
    ).encode(
        x=alt.X("x:Q", scale=scale),
        y=alt.Y("y:Q", scale=scale),
        order="i:Q"
    ).properties(
        width=300,
        height=300
    )
    return chart

#=================================================================

lynx = np.array([
[209.70, 368.42], [157.63, 332.16], [118.82, 284.21], [80.95, 224.56], [43.08, 244.44], [20.36, 266.67], [-4.26, 293.57], [2.37, 263.16], [-20.36, 292.40], [-39.29, 299.42], [-21.30, 259.65],
[-50.65, 267.84], [-39.29, 242.11], [-55.38, 240.94], [-100.83, 300.58], [-149.11, 345.03], [-172.78, 361.40], [-189.82, 300.58], [-192.66, 225.73], [-181.30, 145.03], [-168.05, 104.09], [-184.14, 66.67],
[-186.98, 31.58], [-183.20, 3.51], [-208.76, -4.68], [-197.40, -29.24], [-182.25, -44.44], [-203.08, -43.27], [-172.78, -92.40], [-131.12, -126.32], [-101.78, -147.37], [-74.32, -163.74], [-110.30, -224.56],
[-143.43, -287.72], [-161.42, -240.94], [-282.60, -221.05], [-388.64, -205.85], [-370.65, -301.75], [-339.41, -397.66], [18.46, -397.66], [345.09, -400.00], [359.29, -378.95], [367.81, -342.69], [346.98, -
362.57], [363.08, -302.92], [357.40, -243.27], [348.88, -266.67], [336.57, -201.17], [290.18, -135.67], [240.00, -118.13], [258.93, -164.91], [257.99, -228.07], [252.31, -271.35], [256.09, -333.33],
[247.57, -359.06], [230.53, -307.60], [194.56, -238.60], [160.47, -181.29], [120.71, -149.71], [165.21, -132.16], [201.18, -100.58], [183.20, -99.42], [221.07, -73.68], [253.25, -24.56], [222.01, -23.39],
[251.36, -1.17], [262.72, 24.56], [234.32, 25.73], [214.44, 42.11], [202.13, 60.82], [220.12, 101.75], [234.32, 160.23], [240.00, 230.41], [232.43, 316.96]
])

batman = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])

#==================TASK2=========================================

original_lynx = lynx.copy()

img0 = showimage(lynx).properties(title="Original")

print()
print("FIRST ORDER")
print()

L1 = stretch(lynx, 1.5, 0.7)
L2 = shear(L1, 0.5, 0)
L3 = rotation(L2, np.pi / 4)

img1 = showimage(L1).properties(title="1: Stretch")
img2 = showimage(L2).properties(title="1: Stretch → Shear")
img3 = showimage(L3).properties(title="1: Stretch → Shear → Rotate")

print()
print("SECOND ORDER")
print()

L1 = shear(lynx, 0.5, 0)
L2 = stretch(L1, 1.5, 0.7)
L3 = rotation(L2, np.pi / 4)

img4 = showimage(L1).properties(title="2: Shear")
img5 = showimage(L2).properties(title="2: Shear → Stretch")
img6 = showimage(L3).properties(title="2: Shear → Stretch → Rotate")

print()
print("THIRD ORDER")
print()

L1 = rotation(lynx, np.pi / 4)
L2 = shear(L1, 0.5, 0)
L3 = stretch(L2, 1.5, 0.7)

img7 = showimage(L1).properties(title="3: Rotate")
img8 = showimage(L2).properties(title="3: Rotate → Shear")
img9 = showimage(L3).properties(title="3: Rotate → Shear → Stretch")

print()
print("FOURTH ORDER")
print()

L1 = stretch(lynx, 1.5, 0.7)
L2 = rotation(L1, np.pi / 4)
L3 = shear(L2, 0.5, 0)

img10 = showimage(L1).properties(title="4: Stretch")
img11 = showimage(L2).properties(title="4: Stretch → Rotate")
img12 = showimage(L3).properties(title="4: Stretch → Rotate → Shear")

combined = alt.hconcat(img0, img1, img2, img3, img0, img4, img5, img6, img0, img7, img8, img9, img10, img11, img12)
combined.show()



