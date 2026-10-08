import numpy as np
from math import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def read_off(filename: str):
    with open(filename, 'r') as f:

        if 'OFF' != f.readline().strip():
            raise ValueError('Not a valid OFF header')

        n_verts, n_faces, _ = map(int, f.readline(). strip() .split())

        verts = [list(map(float, f.readline().strip().split())) for _ in range(n_verts)]
        faces = [list(map(int, f.readline().strip().split()[1:])) for _ in range(n_faces)]

    return np.array(verts), faces

vertices, faces = read_off(
    "/Users/pt2/PycharmProjects/ALA Lab1 Domkin/airplane_0631.off"
)

def plot_off(vertices, faces):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    mesh = Poly3DCollection([vertices[face] for face in faces],
                            alpha=0.3, edgecolor='k')
    ax.add_collection3d(mesh)

    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], s=2, c='r')

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.auto_scale_xyz(vertices[:, 0], vertices[:, 1], vertices[:, 2])

    plt.show()

plot_off(vertices, faces)

#==================TASK3=========================================

def rotate_xy(X, angle):
    newx = matrixtransformer(X)
    ROTXY = np.array([[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]])
    return matrixtransformer(ROTXY @ newx), ROTXY

def rotate_yz(X, angle):
    newx = matrixtransformer(X)
    ROTYZ = np.array([[1,0,0],[0, cos(angle), -sin(angle)], [0, sin(angle), cos(angle)],])
    return matrixtransformer(ROTYZ @ newx), ROTYZ

def rotate_xz(X, angle):
    newx = matrixtransformer(X)
    ROTXZ = np.array([[cos(angle), 0,  -sin(angle)], [0, 1, 0], [sin(angle),0, cos(angle)],])
    return matrixtransformer(ROTXZ @ newx), ROTXZ


def matrixtransformer(A):
    return A.T.copy()

Vxy, Mxy = rotate_xy(vertices, pi / 6)
print("XY rotation matrix:\n", Mxy)
plot_off(Vxy, faces)

Vyz, Myz = rotate_yz(vertices, pi / 4)
print("YZ rotation matrix:\n", Myz)
plot_off(Vyz, faces)

Vxz, Mxz = rotate_xz(vertices, pi / 3)
print("XZ rotation matrix:\n", Mxz)
plot_off(Vxz, faces)


#==================TASK4========================================

L1, Mxy = rotate_xy(vertices, pi / 6)
L2, Myz = rotate_yz(L1, pi / 4)
L3, Mxz = rotate_xz(L2, pi / 3)

TOTAL = Mxz @ Myz @ Mxy

print("Combined transformation matrix:\n", TOTAL)
plot_off(L3, faces)