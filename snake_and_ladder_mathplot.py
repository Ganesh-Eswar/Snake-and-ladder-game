import time
import numpy as np
import matplotlib
matplotlib.use('TkAgg') # do this before importing pylab

import matplotlib.pyplot as plt
from PIL import Image
import glob

# importing movie py libraries
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

            # redraw the canvas


if __name__ == "__main__":
    
    floc=glob.glob('snake_ladder.png')
    snl=Image.open(floc[0])
    increment=90
    positions=[[1,1],[23, 4],[28, 10],[32, 16],[36, 18],[39, 23],[45, 29],
               [46, 32],[47, 36],[48, 41],[54, 44],[59, 5],[64, 11],[67, 17],
               [70, 18],[15, 19],[19, 24],[21, 25],[25, 31],[27, 36],[28, 40],
               [29, 17],[33, 23],[37, 28],[38, 34],[41, 35],[46, 37],[47, 17],
               [53, 18],[54, 24],[58, 28],[59, 31],[63, 32],[68, 33],[92, 34],
               [93, 39],[96, 44],[99, 5],[100, 5]]    
    
    fig = plt.figure(figsize=[10,10])
    duration=60
    ax = fig.add_subplot(111)
    
    def make_frame(t):
        print(t)
        ax.clear()
        ax.imshow(snl)
        iind = int(np.floor((t-duration)*len(positions)/duration))
        print(iind)
            
        jloc=int(np.floor((positions[iind][0]-0.1)/10))
        if(jloc%2==0):
            iloc=int(positions[iind][0]-jloc*10)
        else:
            iloc=int(10-positions[iind][0]+jloc*10)
        ax.plot(30+(iloc*increment),850-(jloc*increment),'og',markersize=10)
            
        jloc=int(np.floor((positions[iind][1]-0.1)/10))
        if(jloc%2==0):
            iloc=int(positions[iind][1]-jloc*10-1)
        else:
            iloc=int(11-positions[iind][1]+jloc*10)
        ax.plot(30+(iloc*increment),850-(jloc*increment),'ob',markersize=10)
            
        return mplfig_to_npimage(fig)

        
    animation = VideoClip(make_frame, duration = duration)
    animation.write_videofile('MyGame.mp4',fps=5)
    