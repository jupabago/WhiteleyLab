import shutil
import os

#this function is to remove the position and time from the iles to do it on Daime
def rename():
    for root, dirs, files in os.walk('timeSeries'):
        for name in files:
            	   
            	#nombre = root.split('/')
            	#specific for 3 directories in front, to make it general for any directory length use a loop
            	new= root+'/'+name+".tif"
            	old= root+'/'+name
            	print new+".tif"
            	print 'correct:', os.path.join(root, name)
                os.rename(old, new)

rename()                
