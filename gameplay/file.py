# ZGW
# RUN! FISH!
# Zebin Lin   Frank Gao  Yujie Wei

# player control the fish pass through the barrier and get to his mom's birthday praty on time.


from gamelib import*
game = Game(1000,650,"RUN! FISH!",66)
bk = Image("bk.png",game)
bk.resizeTo(game.width, game.height)
nemo = Image("nemo.gif",game)
nemo.resizeBy(-65)
game.setBackground(bk)
house= Image("house.png",game)
house= Image("house.png",game)
house.resizeBy(60)
house.moveTo(2800,400)
house.setSpeed(1,90)
defeat = Image("defeat.gif",game)
defeat.resizeTo(game.width,game.height)
explosion = Image("explosion.png",game)
explosion.visible = False
ink = Image("ink.png",game)
ink.resizeBy(-80)

ink.visible = False
blood = Image("blood.png",game)
blood.visible = False
blood.resizeBy(-60)
victory = Image("victory.gif",game)
victory.resizeTo(game.width,game.height)
shark = []
for index in range(10):
    shark.append(Image("shark.png",game))
    y = randint(50,450)
    x = randint(5000,24000)
    shark[index].moveTo(x,y)
    shark[index].resizeBy(12)
    shark[index].setSpeed(12,270)
    shark[index].move(True)
fish1 = []
for index in range(45):
    fish1.append(Image("fish1.png",game))
    y = randint(30,530)
    x = randint(4000,15000)
    fish1[index].moveTo(x,y)
    fish1[index].resizeBy(-88)
    fish1[index].setSpeed(6,270)
    fish1[index].move(True)
fish2 = []
for index in range(5):
    fish2.append(Image("fish2.gif",game))
    y = randint(10,490)
    x = randint(4000,14000)
    fish2[index].moveTo(x,y)
    fish2[index].resizeBy(-68)
    fish2[index].setSpeed(5,270)
    fish2[index].move(True)

rocks = []

for index in range(70):
    rocks.append(Image("rock.png",game))
    y = randint(10,580)
    x = randint(1100,13000)
    rocks[index].moveTo(x,y)
    rocks[index].resizeBy(-97)
    rocks[index].setSpeed(8,270)
    rocks[index].move(True)

healthpod = []

for index in range(12):
    healthpod.append(Image("healthpod.png",game))
    y = randint(10,490)
    x = randint(1100,10000)
    healthpod[index].moveTo(x,y)
    healthpod[index].resizeBy(-75)
    healthpod[index].setSpeed(6,270)
    healthpod[index].move(True)
intro=Image("intro.gif",game)
intro.resizeTo(game.width, game.height)


    
bkk = Image("bkk.gif",game)
bkk.resizeTo(game.width, game.height)
bkk.draw()
game.update()
game.wait(K_SPACE)





while not game.over:
    game.processInput()
    intro.draw()
    if mouse.LeftButton:
        game.over= True

    game.update(30)



game.over= False
# LEVEL ONE GAME LOOP
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    bk.draw()
    house.move()
    nemo.move()
    for index in range(70):
        rocks[index].move()
        if rocks[index].collidedWith(nemo):
            nemo.health -=10
            rocks[index].visible = False
            explosion.moveTo(rocks[index].x,rocks[index].y)
            explosion.visible = True
    for index in range(12):
        healthpod[index].move()
        if healthpod[index].collidedWith(nemo):
           nemo.health += 5
           healthpod[index].visible = False
    for index in range(10):
        shark[index].move()
        if shark[index].collidedWith(nemo):
            nemo.health -=15
            shark[index].moveTo(shark[index].x-180, shark[index].y)
            shark[index].visible = True
            blood.moveTo(shark[index].x,shark[index].y)
            blood.visible = True
    for index in range(45):        
        fish1[index].move()
        if fish1[index].collidedWith(nemo):
            nemo.health -=5
            fish1[index].y += 150
            fish1[index].visible = True
    for index in range(5):        
        fish2[index].move()
        if fish2[index].collidedWith(nemo):
            nemo.speed-=1
            fish2[index].visible = False
            ink.moveTo(fish2[index].x,fish2[index].y)
            ink.visible = True
    if keys.Pressed[K_UP]:
        nemo.y -= 6
    if keys.Pressed[K_DOWN]:
        nemo.y += 6
    if keys.Pressed[K_RIGHT]:
        nemo.x += 6
    if keys.Pressed[K_LEFT]:
        nemo.x -= 6

    if game.time < 1:
      
        game.over= True
        
        defeat.draw()
        
    if nemo.health < 1:
      
        game.over= True
        defeat.draw()
    

    if nemo.collidedWith(house):

     
       game.over= True
       victory.draw()

   
    
    game.drawText("health"+str(nemo.health),nemo.x-20,nemo.y+70)
    game.displayTime(25,5)

    game.update(30)

game.wait(K_SPACE)

       
    

game.quit()
