import numpy as np
from math import *
import altair as alt

alt.renderers.enable("browser")

vertices, faces = read_off("your_model.off")

#==================TASK3=========================================

def rotate_xy(X, angle):
    newx = matrixtransformer(X)
    ROTXY = np.array([[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]])
    return matrixtransformer(ROTXY @ newx)

def rotate_yz(X, angle):
    newx = matrixtransformer(X)
    ROTYZ = np.array([[1,0,0],[0, cos(angle), -sin(angle)], [0, sin(angle), cos(angle)],])
    return matrixtransformer(ROTYZ @ newx)

def rotate_xz(X, angle):
    newx = matrixtransformer(X)
    ROTXZ = np.array([[cos(angle), 0,  -sin(angle)], [0, 1, 0], [sin(angle),0, cos(angle)],])
    return matrixtransformer(ROTXZ @ newx)


def matrixtransformer(A):
    return A.T.copy()

#==================TASK4=========================================

