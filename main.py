#rakshasa
import pygame, os 
import random
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
width=1200
height=650
poke="bulbasaur.png"
hp=100
st=0
randimg=random.randint(1,15)
screen = pygame.display.set_mode((width, height ))
pygame.display.set_caption('POKEMON GUESSING GAME')
background_image = pygame.image.load("database/bg.png").convert()
x = 200 # x coordnate of image
y = 150 # y coordinate of image
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()
input_box = pygame.Rect(250, 550, 140, 32)
color_inactive = pygame.Color('#005cf2')
color_active = pygame.Color('#d71b15')
color = color_inactive
active = False
text = ''
done = False
intro=False
basicfont = pygame.font.SysFont(None, 30)
textt = basicfont.render('Guess the pokemon', True,  (215, 27, 21))
texttrect = textt.get_rect()
texttrect.centerx = 400
texttrect.centery = 600
wr = basicfont.render('Your Guess is wrong!', True,  (215, 27, 21))
wrrect = wr.get_rect()
wrrect.centerx = 400
wrrect.centery = 620
rght = basicfont.render('Correct!', True,  (215, 27, 21))
rghtrect = rght.get_rect()
rghtrect.centerx = 400
rghtrect.centery = 620
evposx=460
evposy=520
game_over = basicfont.render('Game Over!Exiting Now.', True,  (215, 27, 21))
gorect = game_over.get_rect()
gorect.centerx = 400
gorect.centery = 620
intro_image = pygame.image.load("database/intro.png").convert()
screen.blit(intro_image, ( 0,0))
start_image=pygame.image.load("database/start.png").convert_alpha()
screen.blit(start_image, ( evposx,evposy))
pygame.display.flip()
while not intro:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = True
                done=True
            if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
                evposx, evposy = event.pos
                if start_image.get_rect().collidepoint(evposx-460, evposy-520):
                    intro=True
while not done:
    if randimg==1:
        poke="bulbasaur.png"
        ans="1bulbasaur.png"
    elif randimg==2:
        poke="ivysaur.png"
        ans="1ivysaur.png"
    elif randimg==3:
        poke="beedrill.png"
        ans="1beedrill.png"
    elif randimg==4:
        poke="blastoise.png"
        ans="1blastoise.png"
    elif randimg==5:
        poke="charizard.png"
        ans="1charizard.png"
    elif randimg==6:
        poke="caterpie.png"
        ans="1caterpie.png"
    elif randimg==7:
        poke="charmeleon.png"
        ans="1charmeleon.png"
    elif randimg==8:
        poke="charmander.png"
        ans="1charmander.png"
    elif randimg==9:
        poke="charizard.png"
        ans="1charizard.png"
    elif randimg==10:
        poke="jigglypuff.png"
        ans="1jigglypuff.png"
    elif randimg==11:
        poke="meowth.png"
        ans="1meowth.png"
    elif randimg==12:
        poke="venusaur.png"
        ans="1venusaur.png"
    elif randimg==13:
        poke="squirtle.png"
        ans="1squirtle.png"
    elif randimg==14:
        poke="raichu.png"
        ans="1raichu.png"
    elif randimg==15:
        poke="pikachu.png"
        ans="1pikachu.png"
        
        
    screen.blit(background_image, ( 0,0))
    pokemonImage = pygame.image.load("database/"+poke).convert_alpha()
    health = basicfont.render('Health: '+ str(hp), True,  (215, 27, 21))
    healthrect = health.get_rect()
    healthrect.centerx = 60
    healthrect.centery = 20
    streak = basicfont.render('Streak: '+ str(st), True,  (215, 27, 21))
    strect = streak.get_rect()
    strect.centerx = 48
    strect.centery = 45
    screen.blit(background_image, ( 0,0))
    screen.blit(pokemonImage, ( x,y))
    screen.blit(textt, texttrect)
    screen.blit(health, healthrect)
    screen.blit(streak, strect)
    pygame.display.flip()
    txt_surface = font.render(text, True, color)
    width = max(300, txt_surface.get_width())
    input_box.w = width
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(screen, color, input_box, 2)
    pygame.display.flip()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if poke==text+".png":
                            pokemonImage = pygame.image.load("database/"+ans).convert_alpha()
                            screen.blit(pokemonImage, ( x,y))
                            screen.blit(rght, rghtrect)
                            pygame.display.flip()
                            st=st+1
                            text = ''
                            randimg=random.randint(1,15)
                            pygame.time.wait(3000)
                        else:
                            hp=hp-20
                            health = basicfont.render('Health: '+ str(hp), True,  (255, 255, 5))
                            screen.blit(health, healthrect)
                            if hp==0:        
                                screen.blit(game_over, gorect)
                                pygame.display.flip()
                                pygame.time.wait(2500)
                                hp==100
                                done=True
                            else:
                                screen.blit(wr, wrrect)
                                pygame.display.flip()
                            text = ''
                            st=0
                            pygame.time.wait(500)
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

    clock.tick(30)

#loop over, quite pygame
pygame.quit()
