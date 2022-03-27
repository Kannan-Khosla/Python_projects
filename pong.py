# this game basicaaly represents the game PONNG in which all is moved and striked with the movable paddles.
#When ball strikes the opposite end player gets a pont. player scoring 11 points first wins the match

import pygame


# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((700, 500))
    # set the title of the display window
    pygame.display.set_caption('PONG')
    # get the display surface
    w_surface = pygame.display.get_surface()
    # create a game object
    game = Game(w_surface)
    # start the main game loop by calling the play method on the game object
    game.play()
    # quit pygame and clean up the pygame window
    pygame.quit()


# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object

        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color('black')
       
        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

        # === game specific objects
        Ball_color = pygame.Color('white')
        Ball_radius = 7
        self.Ball_center = [350,250]  # coordinates of ball
        Ball_velocity = [7,7]   #velocity of the ball
        self.Ball_direction = [1, 1] #direction coordinates of the ball
        self.ball = Ball(Ball_color, Ball_radius, self.Ball_center, Ball_velocity, self.Ball_direction, self.surface)
        
        
        
        
        
        
#paddle corresponding dimensions
        Paddle_width = 10
        Paddle_height = 90
        self.Paddle1_top =  250
        self.Paddle2_top = 250
        Paddle1_left = 100
        Paddle2_left = 700 - 100 - 10
        self.Paddle1_velocity = 14
        self.Paddle2_velocity = 14
        Paddle_color = pygame.Color('white')
        self.paddle1 = Paddle(self.surface, Paddle_width, Paddle_height, self.Paddle1_top, Paddle1_left, Paddle_color, self.Paddle1_velocity)
        self.paddle2 = Paddle(self.surface, Paddle_width, Paddle_height, self.Paddle2_top, Paddle2_left, Paddle_color, self.Paddle2_velocity)
        self.score=[0,0]
        
        # in beginning no key is being pressed
        self.q_down= False  
        self.a_down= False
        self.p_down= False
        self.l_down= False



    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.

        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()
            if self.continue_game:
                self.update()
                self.decide_continue()
            self.game_Clock.tick(self.FPS)  # run at most with FPS Frames Per Second

    def handle_events(self):
        
        

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:   #for closing the window
                self.close_clicked = True
                
            #########################    
            if event.type== pygame.KEYDOWN:  #using keyboard key events when key is pressed down key.down is true and keyUP is false
                
                if event.key == pygame.K_q:
                    self.q_down= True          
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_q:
                    self.q_down=False
            ##########################        
            if event.type== pygame.KEYDOWN:        
                if event.key == pygame.K_a:
                    self.a_down= True
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_a:
                    self.a_down=False
            ##########################        
            if event.type== pygame.KEYDOWN:
        
                if event.key == pygame.K_p:
                    self.p_down= True
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_p:
                    self.p_down=False
            ###########################
            if event.type== pygame.KEYDOWN:        
                if event.key == pygame.K_l:
                    self.l_down= True
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_l:
                    self.l_down=False                    
            ###########################        
            
            
            
# movement of paddles 

    def handle_keydown(self,event):
        if event.key == pygame.K_q: #left paddle up
            paddle1.set_paddle1_top(paddle1.get_paddle1_top()+self.Paddle1_velocity)
        if event.key == pygame.K_a:#left paddle down
            paddle1.set_paddle1_top(paddle1.get_paddle1_top()-self.Paddle1_velocity)   
         
        if event.key == pygame.K_p:#right paddle up
            paddle2.set_paddle2_top(paddle2.get_paddle_2top()+self.Paddle2_velocity)
        if event.key == pygame.K_l:#right paddle down
            paddle2.set_paddle2_top(paddle2.get_paddle_2top()-self.Paddle2_velocity)                    

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color)  # it clears the display surface first
        self.ball.draw()
        self.paddle1.draw()
        self.paddle2.draw()
        self.draw_score()


        pygame.display.update()  # make the updated surface appear on the display

    def update(self):
        #the game updates are done here for eg movemnet ball , paddle, collisions etc.
        
        
        self.ball.move()
        self.ball.strike_walls(self.score)
        if self.Ball_direction[0]==1:
            self.paddle2.ball_paddle_collision(self.Ball_center, self.Ball_direction)
        elif self.Ball_direction[0]==-1:
            self.paddle1.ball_paddle_collision(self.Ball_center,self.Ball_direction)
            
            
            
         #paddle stopping code to avoid paddles move out of the display window   
        if self.q_down:
            if self.paddle1.get_rect().top-self.Paddle1_velocity>0 :
                self.paddle1.set_paddle_top(self.paddle1.get_paddle_top()-self.Paddle1_velocity)                       
                
            
        if self.a_down:
            if  self.paddle1.get_rect().bottom+self.Paddle1_velocity<self.surface.get_height():
                self.paddle1.set_paddle_top(self.paddle1.get_paddle_top()+self.Paddle1_velocity)            
            
        if self.p_down:
            if self.paddle2.get_rect().top-self.Paddle2_velocity>0 :
                self.paddle2.set_paddle_top(self.paddle2.get_paddle_top()-self.Paddle2_velocity)
        if self.l_down:
            if  self.paddle2.get_rect().bottom+self.Paddle2_velocity<self.surface.get_height():
                self.paddle2.set_paddle_top(self.paddle2.get_paddle_top()+self.Paddle2_velocity)   
            
            
      # displays the score board      
    def draw_score(self):
        text_color = pygame.Color('white')
        text_font = pygame.font.SysFont('', 72)
        text_image1 = text_font.render(str(self.score[0]), True, text_color)   #renders font score for player 1
        text_image2 = text_font.render(str(self.score[1]), True, text_color)   #renders font for player 1
        self.surface.blit(text_image1, (5,5))
        self.surface.blit(text_image2, (670,5))


    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check

        for i in range(2):
            if self.score[i]==11:
                self.continue_game=False


class Ball:
    # represents a single Ball moving to and fro in the Pong Game
    def __init__(self, Ball_color, Ball_radius, Ball_center, Ball_velocity,Ball_direction, screen):
        self.color = Ball_color
        self.radius = Ball_radius
        self.center = Ball_center
        self.velocity = Ball_velocity
        self.direction=Ball_direction
        self.screen = screen


    def move(self):
        # Change the location of the Dot by adding the corresponding
      
        for i in range(0, 2):
            self.center[i] = self.center[i] + self.velocity[i]*self.direction[i]


    def draw(self):
        # Draw the dot onto the game's window
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)

# Wall  Bounce
    def strike_walls(self,score):
        if self.center[0]>700-self.radius:
            self.direction[0]= -1
            score[0]+=1
        if self.center[0] < self.radius:
            self.direction[0]= 1
            score[1]+=1
        if self.center[1] > 490:
            self.direction[1] = -1
        if self.center[1] < self.radius :
            self.direction[1] = 1




class Paddle:
    #represents the paddle moving up and down the screen
    def __init__(self, screen, Paddle_width, Paddle_height, Paddle_top, Paddle_left, Paddle_color, Padddle_velocity):
        self.screen= screen
        self.width=Paddle_width
        self.height=Paddle_height
        self.top=Paddle_top
        self.left=Paddle_left
        self.color=Paddle_color
        self.velocity=Padddle_velocity

    def draw(self):
        self.rect_position=pygame.Rect(self.left, self.top, self.width, self.height)
        pygame.draw.rect(self.screen,self.color, self.rect_position)
    
    
    
            
    def set_paddle_top(self,new_top):  
        self.top=new_top
        
        
        
    def get_paddle_top(self):
        return self.top  #returns paddle top
    
    def get_rect(self):
        return self.rect_position  #returns rect_positions
        
    
   #collision of ball with paddles

    def ball_paddle_collision(self, ball,direction):
        if self.rect_position.collidepoint(ball): #using collidepint technique
            direction[0]= -direction[0]
            
            
    
main()

