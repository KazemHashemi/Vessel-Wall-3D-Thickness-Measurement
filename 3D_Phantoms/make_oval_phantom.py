
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
import os

r1 = 2
r2 = 1.5
r3 = 1.0
d = 1.5

phantoms = ['oval_10', 'oval_05', 'oval_02']
spatial_res = [1/10,1/5,1/2]

fov = 1.05*2*(max([r1,r2,r3])+d)
fov_x = 1.05*(max([r1,r2,r3])+d)

for phtm, res in zip(phantoms, spatial_res):

    nx = int(np.round(fov_x/res))
    ny = int(np.round(fov/res))
    nz = ny

    cx = nx
    cy = ny/2
    cz = nz/2

    X,Y,Z = np.mgrid[0:nx,0:ny,0:nz]

    lumen = (res*(X + 0.5 - cx)/r1)**2 + (res*(Y + 0.5 - cy)/r2)**2 + (res*(Z + 0.5 - cz)/r3)**2 - 1
    wall = (res*(X + 0.5 - cx)/(r1+d))**2 + (res*(Y + 0.5 - cy)/(r2+d))**2 + (res*(Z + 0.5 - cz)/(r3+d))**2 - 1

    msk = ((lumen>=0) & (wall <0))
    
    ax1 = plt.figure().add_subplot(projection='3d')
    ls = LightSource(90, 30)
    im1 = ax1.voxels(msk, facecolors='white', edgecolors='gray', shade=True, lightsource=ls)
    ax1.set_box_aspect((nx, ny, nz)) 
    ax1.grid(False)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_zticks([])
    ax1.set_axis_off()
    ax1.view_init(elev=30,azim=45)
    plt.show()
