import pygame 
import sys
from _chessboard import CREATE_CHESSBOARD

pygame.init()


res = (800,800)
# white color
color = (255,255,255)
screen = pygame.display.set_mode(res) 
pygame.display.set_caption('N-Queen')

# light shade of the button
color_light = (170,170,170)
  
# dark shade of the button
color_dark = (100,100,100)
  
# stores the width of the
# screen into a variable
width = screen.get_width()
  
# stores the height of the
# screen into a variable
height = screen.get_height()
  
# defining a font
smallfont = pygame.font.SysFont('Corbel',35)
  
# rendering a text written in
# this font
text = smallfont.render('ALG1' , True , color)

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    global done
                    global t
                    t = self.text
                    if int(t) >= 4:
                        done = True
                    
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)




clock = pygame.time.Clock()
input_box1 = InputBox(width/2-100, height/4+100, 140, 32)
input_boxes = [input_box1]

done = False    
Page_C = 0 
#page one
while not done:   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            Page_C = 1
        for box in input_boxes:
            box.handle_event(event)
            if event.type == pygame.K_RETURN and int(t) >= 4:      
                done = True
    for box in input_boxes:
        box.update()

    screen.fill((30, 30, 30))
    for box in input_boxes:
        box.draw(screen)
    screen.blit(smallfont.render('Please enter number of queens (n >= 4)!' , True , color) , (width/2-250,height/4))
    pygame.display.flip()
    clock.tick(30)







pygame.init()
  

screen = pygame.display.set_mode(res)
  

color = (255,255,255)
  

color_light = (170,170,170)
  

color_dark = (100,100,100)

width = screen.get_width()
  

height = screen.get_height()
  

smallfont = pygame.font.SysFont('Corbel',35)
  

text = smallfont.render('quit' , True , color)
done = False  
# page 2
while not done and Page_C == 0:
      
    for ev in pygame.event.get():
          
        if ev.type == pygame.QUIT:
            pygame.quit()
              

        if ev.type == pygame.MOUSEBUTTONDOWN:
              

            if width/4-50 <= mouse[0] <= width/4+90 and height/2-20 <= mouse[1] <= height/2+20:
                import alg1 as alg
                done = True  
            if(2*(width/4))-50 <= mouse[0] <= (2*(width/4))+90 and height/2-20 <= mouse[1] <= height/2+20:
                import alg2 as alg
                done = True  
            if(3*(width/4))-50 <= mouse[0] <= (3*(width/4))+90 and height/2-20 <= mouse[1] <= height/2+20: 
                import alg3 as alg
                done = True  
                  

      

    mouse = pygame.mouse.get_pos()
      
    if width/4-50 <= mouse[0] <= width/4+90 and height/2-20 <= mouse[1] <= height/2+20:
        pygame.draw.rect(screen,color_light,[width/4-50,height/2-20,140,40])
    else:
        pygame.draw.rect(screen,color_dark,[width/4-50,height/2-20,140,40])
    if (2*(width/4))-50 <= mouse[0] <= (2*(width/4))+90 and height/2-20 <= mouse[1] <= height/2+20:    
        pygame.draw.rect(screen,color_light,[(2*(width/4))-50,height/2-20,140,40])
    else:
        pygame.draw.rect(screen,color_dark,[(2*(width/4))-50,height/2-20,140,40])
    if (3*(width/4))-50 <= mouse[0] <= (3*(width/4))+90 and height/2-20 <= mouse[1] <= height/2+20:     
        pygame.draw.rect(screen,color_light,[(3*(width/4))-50,height/2-20,140,40])
    else:      
        pygame.draw.rect(screen,color_dark,[(3*(width/4))-50,height/2-20,140,40])
        
        
      
    # superimposing the text onto our button
    screen.blit(smallfont.render('ALG-fi' , True , color) , (width/4-30,height/2-16))
    screen.blit(smallfont.render('ALG-se' , True , color) , ((2*(width/4))-30,height/2-16))
    screen.blit(smallfont.render('ALG-th' , True , color) , ((3*(width/4))-30,height/2-16))
      
    # updates the frames of the game
    pygame.display.update()





print(t)
N = int(t)
result = alg.Run_Alg(N)
pygame.display.set_caption('Process time : ' + str(result[1]))
ARR = result[0]
queenImg = pygame.image.load('queen.png')

pygame.init()

WIDTH = HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def chess_build(ARR):

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        CREATE_CHESSBOARD(WIDTH, HEIGHT, WINDOW, ARR, queenImg)

        pygame.display.update()

chess_build(ARR)

pygame.quit()
