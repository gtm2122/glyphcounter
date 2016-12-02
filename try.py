def main():
 with open('new_file') as file:
  content = file.readlines()
 
 #print content
 #exit()
 #print len(content[1][1])
 #print len(conten
 #print content[2]
 #print len(content[1])

 world = [] 

 for i in content:
  #i = list(i)
  #print len(i)
  i = i.split()
  for j in i:
   line = []
   for k in j:
    if not(k=='\n'):
     line.append(k)
   world.append(line)
 #print world[1]
 #file = 'abc.txt'
 
 all_X = [] 

 for x in range (0,len(world)):
  #print world[x]
  #print len(world)
  #print len(world[0])
  
  for y in range(0,len(world[0])):
  
   if(world[x][y]=='X' ):
    all_X.append([x,y])
#print all_X
#def func(x][y,world)
 count = 0
 
 for x in range(0,len(world)-1):
  flag = 0
  for y in range(0,len(world[0])-1):
   if(world[x][y] =='X' and [x,y] in all_X):
    #print tuple([x,y])
    func(x,y,world,all_X)
    flag = 1
  #if(flag==1):
    count+=1
    #exit()
 print count
 
def func(x,y,world,all_X):
 #print [x,y]
 if([x,y]not in all_X):
  return
 for i in range(0,len(all_X)):
  if all_X[i] == [x,y] :
   
   del all_X[i]
   break
 
 if (world[x+1][y] =='X' and x+1 < len(world)-1):
  func(x+1,y,world,all_X)
  #print 0
 if  (world[x-1][y] =='X' and x > 0):
  func(x-1,y,world,all_X)
  #print 1
 if  (world[x][y+1] =='X' and y+1 < len(world[0])-1):
  func(x,y+1,world,all_X)
  #print 2
 if  (world[x][y-1] =='X' and y > 0):
  func(x,y-1,world,all_X)
  #print 3
 if  (world[x+1][y+1] =='X' and x+1 < len(world) and y+1 <len(world[0])-1):
  func(x+1,y+1,world,all_X)
  #print 4
 if  (world[x+1][y-1] =='X' and x+1 < len(world)and y>0):
  func(x+1,y-1,world,all_X)
  #print 5
 if  (world[x-1][y+1] =='X' and x >0 and y+1< len(world[0])-1):
  func(x+1,y,world,all_X)
  #print 6
 if  (world[x-1][y-1] =='X' and x>0 and y>0):
  func(x+1,y,world,all_X)
  #print 7  
 
main()
