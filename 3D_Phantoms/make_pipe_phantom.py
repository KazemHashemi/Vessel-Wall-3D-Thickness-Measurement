
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource

R = 3
r = 1.5
d = 1.5

phantoms = ['pipe_10', 'pipe_05', 'pipe_02']
spatial_res = [1/10,1/5,1/2]

fov_xy = R + 1.05*2*(r+d)
fov_z = 1.05*2*(r+d)

for phtm, res in zip(phantoms, spatial_res):


    nx = int(np.round(fov_xy/res))
    ny = nx
    nz = int(np.round(fov_z/res))

    cx = nx
    cy = ny
    cz = nz/2

    X,Y,Z = np.mgrid[0:nx,0:ny,0:nz]

    lumen_xy = np.sqrt((X + 0.5 - cx)**2 + (Y + 0.5 - cy)**2) - (R+r+d)/res
    lumen = lumen_xy**2 + (Z + 0.5 - cz)**2 - (r/res)**2
    wall = lumen_xy**2 + (Z + 0.5 - cz)**2 - ((r+d)/res)**2
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
