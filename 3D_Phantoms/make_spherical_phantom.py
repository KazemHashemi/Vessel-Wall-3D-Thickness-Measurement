
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
import os

out_path = '/v/ai/nobackup/shashemi/VWI_DL/Thickness_3D/phantom/'

r = 1.5
d = 1.5

phantoms = ['sphere_10', 'sphere_05', 'sphere_02']
spatial_res = [1/10,1/5,1/2]

fov_x = 1.05*(r+d)
fov = 1.05*2*(r+d)

for phtm, res in zip(phantoms, spatial_res):

    if not os.path.exists(out_path + phtm + '/'):
        os.makedirs(out_path + phtm + '/')

    out_file = out_path + phtm + '/' + phtm + '_seg.npy'

    
    

    nx = int(np.round(fov_x/res))
    ny = int(np.round(fov/res))
    nz = ny
    out = 0.5* np.ones((nx,ny,nz))

    cx = nx
    cy = ny/2
    cz = nz/2

    X,Y,Z = np.mgrid[0:nx,0:ny,0:nz]

    lumen = (X + 0.5 - cx)**2 + (Y + 0.5 - cy)**2 + (Z + 0.5 - cz)**2 - (r/res)**2
    wall = (X + 0.5 - cx)**2 + (Y + 0.5 - cy)**2 + (Z + 0.5 - cz)**2 - ((r+d)/res)**2
    msk = ((lumen>=0) & (wall <0))
    
    out[lumen < 0] = 0
    out[wall >= 0] = 1


    np.save(out_file, out)
    
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
    #print(dir(ax1.patch))
    #print(dir(ax1.patches))
    plt.show()

