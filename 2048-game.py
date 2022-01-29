
import random 
import copy
import concurrent.futures

class game_2048:

    def __init__(self):
        self.game = []
        for i in range(4):
            g = [-1]*4
            self.game.append(g)

    def print_game(self):
        for i in range(4):
            for j in self.game[i]:
                if j == -1:
                    print("*"+'\t',end='')
                else:
                    print(str(j)+'\t',end='')
            print()

    def add(self):
        while True:
            g = random.randrange(0,16)
            if self.game[g//4][g%4] == -1:
                break

        l = random.random()
        if ( l > 0.1):
            self.game[g//4][g%4] = 2

        else:
            self.game[g//4][g%4] = 4            
        
    def up(self):
        flag = False
        for i in range(1,4):
            for j in range(4):
                stack = []
                if self.game[i][j] != -1:
                    pos = 0
                    
                    for k in range(i-1,-1,-1):
                        if self.game[k][j] != -1:
                            pos = k+1
                            
                            if self.game[k][j] == self.game[i][j]:
                                stack.append(k)
                                self.game[k][j] *= 2
                                self.game[k][j] += 1
                                self.game[i][j] = -1
                                flag = True
                                pos = -1
                            break
                    if pos != -1:
                        self.game[pos][j],self.game[i][j] = self.game[i][j],self.game[pos][j]
                        if pos != i :
                            flag = True

                for e in stack:
                        self.game[e][j] -=1
        return flag
                    
    def down(self):
        flag = False
        for i in range(3,-1,-1):
            for j in range(4):
                stack = []
                if self.game[i][j] != -1:
                    pos = 3
                    
                    for k in range(i+1,4,1):
                        if self.game[k][j] != -1:
                            pos = k-1
                            if self.game[k][j] == self.game[i][j]:
                                stack.append(k)
                                self.game[k][j] *= 2
                                self.game[k][j] += 1
                                self.game[i][j] = -1
                                flag = True
                                pos = -1
                            break
                    
                    if pos != -1:        
                        self.game[pos][j],self.game[i][j] = self.game[i][j],self.game[pos][j]
                        if pos != i:
                            flag = True
                for e in stack:
                        self.game[e][j] -=1
        return flag

    def right(self):
        flag = False
        stack = []
        for i in range(3,-1,-1):
            for j in range(4):
                
                if self.game[j][i] != -1:
                    pos = 3
                    
                    for k in range(i+1,4,1):
                        if self.game[j][k] != -1:
                            pos = k-1
                            if self.game[j][k] == self.game[j][i]:
                                stack.append([k,j])
                                flag = True
                                self.game[j][k] *= 2
                                self.game[j][k] += 1
                                self.game[j][i] = -1
                                pos = -1
                            break
                
                    if pos != -1:
                        self.game[j][pos],self.game[j][i] = self.game[j][i],self.game[j][pos]
                        if pos != i:
                            flag = True
        for e in stack:
            self.game[e[1]][e[0]] -=1
        return flag
    
    def left(self):
        flag = False
        stack = []
        for i in range(1,4):
            for j in range(4):
                
                if self.game[j][i] != -1:
                    pos = 0
                    
                    for k in range(i-1,-1,-1):
                        if self.game[j][k] != -1:
                            pos = k+1
                            if self.game[j][k] == self.game[j][i]:
                                stack.append([k,j])
                                flag = True
                                self.game[j][k] *= 2
                                self.game[j][k] +=1
                                self.game[j][i] = -1
                                pos = -1
                            break
                
                    if pos != -1:
                        self.game[j][pos],self.game[j][i] = self.game[j][i],self.game[j][pos]
                        if pos != i:
                            flag = True
        for e in stack:
            self.game[e[1]][e[0]] -=1
        return flag

def get(game2,r,c):
    if r < 0 or c < 0:
        return 11
    elif r == 4 or c == 4:
        return 0
    else:
        return game2.game[r][c]

def sameNo(game):
    score = 0
    for i in range(4):
        for j in range(4):
            for k in range(i-1,i+1,1):
                   for l in range(j-1,j+1,1):
                      if k!=-1 and l!=-1:
                        if game[i][j] == game[k][l]:
                            score *=50
    return score  

global w
w = [
            [4**15,4**14,4**13,4**12],
            [4**8,4**9,4**10,4**11],
            [4**7,4**6,4**5,4**4],
            [4**0,4**1,4**2,4**3]
        ]

def mul(game):
    global w
    score = 0
    for i in range(4):
        for j in range(4):
            
            if game[i//4][i%4] != -1:
                score += game[i][j]

    return score
   

def zigzag(game,l):
    score = 0
    for i in range(0,16):
        
          if game[i//4][i%4]==-1:
              score = score +  (11**(4-l))
          else:
              score=score + ((16-i)**2)*game[i//4][i%4]
    return score


def cal_score(game2):
    score1 = 0
    score = 0
    c= count(game2.game)
    if c>=1:
        #score+=zigzag(game2.game,l)
        for i in range(0,16):
        
            if game2.game[i//4][i%4]==-1:
                score = score +  (11**(4))
            else:
                score=score + ((16-i)**2)*10*game2.game[i//4][i%4]
    else:
        for i in range(0,4):
          for j in range(0,4):

               if game2.game[i][j]==-1:
                  score=score+0

               else:
                 for k in range(i-1,i+1,1):
                   for l in range(j-1,j+1,1):
                      if k!=-1 and l!=-1:
                         score=score+game2.game[i][j]*game2.game[k][l]
                
    return score

def cal_score2(game2,l):
    score = 0
    score2 = 0
    for i in range(0,16):
        
        if game2.game[i//4][i%4]==-1:
            score = score +  (11**(4-l))
        else:
            if (i//4) % 2 == 1:
                score = score + ((16-i-3+2*(i%4))**2)*10*game2.game[i//4][i%4]
            else:
                score = score + ((16-i)**2)*10*game2.game[i//4][i%4]
            
            
            #print((16-i)*10*game2.game[i//4][i%4],i,game2.game[i//4][i%4])
    
    for i in range(4):
        for j in range(4):
            d = (get(game2,i,j)*get(game2,i-1,j)*get(game2,i-1,j-1)*get(game2,i+1,j)*get(game2,i+1,j+1)*get(game2,i,j+1)*get(game2,i-1,j+1)*get(game2,i+1,j-1)*get(game2,i,j-1))
            score2 += d
    
    return 1*score+0*score2

def check(game,level):
    if level == 3:
        return cal_score(game)
    
    
    culscore = 0
    #currpath.append("w")
    game2 = copy.deepcopy(game)
    
    if game2.up():
        game2.add()
    #score = cal_score(game2,level)
    

    
    #if score > maxscore[0] :
    #    maxscore[0] = score
    #    maxpath = currpath[:]
    #print('\n\n')
    #print("w",maxscore,score,maxpath,currpath,level)
    #game2.print_game()
    culscore += check(game2,level+1)
    #currpath.pop(-1)

    #currpath.append("a")
    #print(maxpath,"wtf")
    game2 = copy.deepcopy(game)
    if game2.left():
        game2.add()
    #score = cal_score(game2,level)
    
    
    #if score > maxscore[0] :
    #    maxscore[0] = score
    #    maxpath = currpath[:]
    #print('\n\n')
    #print("a",maxscore,score,maxpath,currpath,level)
    #game2.print_game()
    culscore += check(game2,level+1)
    #currpath.pop(-1)
    
    #currpath.append("s")
    game2 = copy.deepcopy(game)

    if game2.down():
        game2.add()
    #score = cal_score(game2,level)
   
    #if score > maxscore[0] :
    #    maxscore[0] = score
    #    maxpath = currpath[:]
    #print('\n\n')
    #print("s",maxscore,score,maxpath,currpath,level)
    #game2.print_game()
    culscore += check(game2,level+1)
    #currpath.pop(-1)
    
    #currpath.append("d")
    game2 = copy.deepcopy(game)
    if game2.right():
        game2.add()
    #score = cal_score(game2,level)
    
    #if score > maxscore[0] :
    #    maxscore[0] = score
    #    maxpath = currpath[:]
    #print('\n\n')
    #print("d",maxscore,score,maxpath,currpath,level)
    #game2.print_game()
    culscore += check(game2,level+1)
    #currpath.pop(-1)

    return culscore

def count(l):
    c = 0
    for i in range(4):
        for j in range(4):
            if l[i][j] == -1:
                c+=1
    return c


def playgame(g):
    while True :
    
        d = { 0 : 'w',1:'a',2:'s',3:'d'}

        j = random.randrange(0,3)
        j = d[j]
        #print(maxpath)
        if j == 'w':
            o = g.up()
        elif j == 's':
            o = g.down()
        elif j == 'a':
            o = g.left()
        elif j == 'd':
            o = g.right()
        if o == True:
            g.add()
        else:
            #print("invalid")
            o = g.up() or g.left() or g.right() or g.down()
            if not o:
                break
            else:

                g.add()

        #g.print_game()
        #print("\n\n")
    #print("Game over")

    return mul(g.game)

def play(game):

    gup = 0
    gleft = 0
    gright = 0
    gdown = 0
    states = 1
    n = 100

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(n):

            game2 = copy.deepcopy(game)

            if game2.up():
                game2.add()
            #upfuture = executor.submit(,game2,0)
            upfuture = executor.submit(playgame,game2)

            #upscore = check(game2,0)/states
            #gup += upscore 
            #print("upscore "+str(upscore))

            game2 = copy.deepcopy(game)

            if game2.left():
                game2.add()
            
            #leftfuture = executor.submit(check,game2,0)
            leftfuture = executor.submit(playgame,game2)

            #leftscore = check(game2,0)/states
            #gleft += leftscore
            #print("leftscore "+str(leftscore))

            game2 = copy.deepcopy(game)

            if game2.right():
                game2.add()
            
            #rightfuture = executor.submit(check,game2,0)
            rightfuture = executor.submit(playgame,game2)

            #rightscore = check(game2,0)/states
            #gright += rightscore
            #print("rightscore "+str(rightscore))

            game2 = copy.deepcopy(game)

            if game2.down():
                game2.add()
            
            #downfuture = executor.submit(check,game2,0)
            downfuture = executor.submit(playgame,game2)

            #downscore = check(game2,0)/states
            #gdown += downscore
            #print("downscore "+str(downscore))
            #print(i)
            gup += upfuture.result()
            #print("up"+str(upfuture.result()))
            gleft += leftfuture.result()
            #print("left"+str(leftfuture.result()))

            gright += rightfuture.result()
            #print("right"+str(rightfuture.result()))

            gdown += downfuture.result()
            #print("down"+str(downfuture.result()))


    gup/=n
    gleft/=n
    gright/=n
    gdown/=n
    #print("gup "+str(gup))
    #print("gleft "+str(gleft))
    #print("gright "+str(gright))
    #print("gdown "+str(gdown))
    maxe = max(gup,gleft,gright,gdown)

    if gup == maxe:
        print("w")
        return 'w'
    elif gleft == maxe:
        print("a")
        return 'a'
    elif gright == maxe:
        print("d")
        return 'd'
    else:
        print("s")
        return 's'



g = game_2048()
g.add()
g.print_game()
#play(g)

"""
while True:
    j = input()
    
    if j == 'w':
        o = g.up()
    elif j == 's':
        o = g.down()
    elif j == 'a':
        o = g.left()
    elif j == 'd':
        o = g.right()
    if o == True:
        g.add()
    else:
        print("invalid")
    g.print_game()
"""

#maxpath =[]
c = 1

while True :
    
    
    j = play(g)
    #print(maxpath)
    if j == 'w':
        o = g.up()
    elif j == 's':
        o = g.down()
    elif j == 'a':
        o = g.left()
    elif j == 'd':
        o = g.right()
    if o == True:
        g.add()
    else:
        print("invalid")
        o = g.up() or g.left() or g.right() or g.down()
        print("wtfff")
        if not o:
            break
        else:

            g.add()

    g.print_game()
    print("\n\n")
print("Game over")



