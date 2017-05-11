    
import os
import shutil

#def copy():
#    for root, dirs, files in os.walk('set1'):
#        for name in files:
#			if "z01_p0" in name:
#                print "hello"
                    #source = root+'/'+name
                #print sourceshutil.copy(source, "p0test/"+name)

def positions(num):
    arreglo=[]
    for i in range(num):
        if num>9 and i<10:
            position = "p0"+str(i)
            arreglo.append(position)
        else:
            position = "p"+str(i)
            arreglo.append(position)
    return arreglo

def times(num):
    arreglo=[]
    for i in range(num):
        if num>9 and i<10:
            time = "_t0"+str(i)
            arreglo.append(time)
        else:
            time = "_t"+str(i)
            arreglo.append(time)
    return arreglo    

def movePositions(folder, positionsList):
    for root, dirs, files in os.walk(folder):
        for name in files:
            for position in positionsList:
                if position in name:
                    source = root+'/'+name
                    newpath = 'clean/'+position
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                    shutil.move(source, newpath+'/'+name)

def moveTimes(folder, timesList):
    for root, dirs, files in os.walk(folder):
        for name in files:
            for time in timesList:
                if time in name:
                    pato=root.split('/')
                    source = root+'/'+name
                    newpath = 'timeSeries/'+pato[1]+'/'+time[1:]
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                    shutil.move(source, newpath+'/'+name)

#to use for both positions and times uncomment both functions and enter name of folder, times and positions and run it in command line
#movePositions("timeSeries", positions(6))
#moveTimes("clean", times(8))



