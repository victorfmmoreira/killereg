import pygame
from pygame.locals import *
import sys

fps = 60
catch_fps = 300
screen_width = 800
screen_height = 500
screen_size = [ screen_width, screen_height]
background_color = [ 0, 30, 30 ]
font_color = [ 220, 90, 90 ]
screen = pygame.display.set_mode( screen_size )
numero_de_tiros = 5 

#define o tipo dos objetos naves
nave1 = pygame.image.load( "chicken_left.png" )
nave2 = pygame.image.load( "chicken_right.png" )

tiro_nave1 = []
tiro_nave2 = []

for indice_do_tiro in range( numero_de_tiros ):
    tiro_nave1.append( pygame.image.load( "small_egg.png" ) )
    tiro_nave2.append( pygame.image.load( "small_egg.png" ) )

#cria variaveis para as posicoes dos objetos
nave1_rect = nave1.get_rect()
nave2_rect = nave2.get_rect()

tiro_nave1_rect = []
tiro_nave2_rect = []
for indice_do_tiro in range( numero_de_tiros ):
    tiro_nave1_rect.append( tiro_nave1[ indice_do_tiro ].get_rect() )
    tiro_nave2_rect.append( tiro_nave2[ indice_do_tiro ].get_rect() )

#define o tipo dos textos
pygame.font.init()
font = pygame.font.Font(None, 36)
title = font.render("NAVINHAS", 1, font_color )
title_rect = title.get_rect()
title_rect.centerx = screen.get_rect().centerx
title_rect.top = 30


estado = "definicoes iniciais"
#estado de definicoes iniciais
#define coordenada x e y da posicao inicial das naves
clock = pygame.time.Clock()

#define teclas com lock
lock_key = [K_CAPSLOCK, K_NUMLOCK, K_SCROLLOCK]

#loop principal do programa
while True:
    
    pressed_key = pygame.key.get_pressed()
    event_list = pygame.event.get()

    for event in event_list:
	if event.type == pygame.QUIT:
	    sys.exit()

    if pressed_key[ K_w ] and pressed_key[ K_LCTRL ]:
        sys.exit()
    
    if estado == "definicoes iniciais":
	distancia_das_laterais = 10
	nave1_rect.left = distancia_das_laterais
	nave2_rect.right = screen.get_rect().right - distancia_das_laterais

	nave1_rect.centery = screen.get_rect().centery
	nave2_rect.centery = nave1_rect.centery

	#define coordenada x e y da posicao inicial dos tiros 
	for indice_do_tiro in range( numero_de_tiros ):
	    tiro_nave1_rect[indice_do_tiro].left = screen_width + 1
	    tiro_nave2_rect[indice_do_tiro].right = -1

	#define velocidade das naves e dos tiros
	initial_nave1_speed = 18
	initial_nave2_speed = initial_nave1_speed

	velocidade_tiro_nave1 = []
	velocidade_tiro_nave2 = []
	for indice_do_tiro in range( numero_de_tiros ):
	    velocidade_tiro_nave1.append( (  1 * 2 ** indice_do_tiro ) )
	    velocidade_tiro_nave2.append( -velocidade_tiro_nave1[indice_do_tiro] )

        #define aceleracao das naves
        aceleracao_das_naves = -4

	#define distancia minima das naves ate as laterais da telas no eixo y
	min_top_distance = 100
	min_bottom_distance = 50

        #definicao de delays

	key_delay = 30
        game_over_delay = 300


	#definicao dos contadores de ciclo

	key_nave1_ciclo = key_delay
	key_nave2_ciclo = key_delay
        game_over_ciclo = 0

	estado = "loop"

    #Descreve os eventos do jogo
    elif estado == "loop":
	    nave1_top_distance = nave1_rect.centery
	    nave1_bottom_distance = screen.get_rect().bottom - nave1_rect.centery
 
            #controla velocidade das naves
            nave1_speed = initial_nave1_speed
            nave2_speed = initial_nave2_speed
            for indice_do_tiro in range( numero_de_tiros ):
                if tiro_nave1_rect[indice_do_tiro].left < screen_width:
                    if indice_do_tiro == numero_de_tiros - 1:
                        nave1_speed = 0
                    else:
                        nave1_speed += aceleracao_das_naves
            
                if tiro_nave2_rect[indice_do_tiro].left > 0:
                    if indice_do_tiro == numero_de_tiros - 1:
                        nave2_speed = 0
                    else:
                        nave2_speed += aceleracao_das_naves


            #move_nave
            if pressed_key[ K_w ] and nave1_top_distance > min_top_distance:
		nave1_rect.centery -= nave1_speed
	    elif pressed_key[ K_s ] and nave1_bottom_distance > min_bottom_distance:
		nave1_rect.centery += nave1_speed


	    nave2_top_distance = nave2_rect.centery
	    nave2_bottom_distance = screen.get_rect().bottom - nave2_rect.centery
	    if pressed_key[ K_UP ] and nave2_top_distance > min_top_distance:
		nave2_rect.centery -= nave2_speed
	    elif pressed_key[ K_DOWN ] and nave2_bottom_distance > min_bottom_distance:
		nave2_rect.centery += nave2_speed

	#move os tiros ja disparados
    	    tiro_ciclo = 0
	    for indice_do_tiro in range( numero_de_tiros ):
	        tiro_nave1_rect[indice_do_tiro].move_ip( [ velocidade_tiro_nave1[indice_do_tiro], 0]) 
		tiro_nave2_rect[indice_do_tiro].move_ip( [ velocidade_tiro_nave2[indice_do_tiro], 0]) 


	#dispara os tiros da nave1
	    for indice_do_tiro in range( numero_de_tiros ):
		if pressed_key[ K_g ] and tiro_nave1_rect[indice_do_tiro].left > screen_width:
		   if key_nave1_ciclo >= key_delay:
		        key_nave1_ciclo = 0
		        if indice_do_tiro == 0:
		            tiro_nave1_rect[indice_do_tiro].center = nave1_rect.center
		        
		        elif tiro_nave1_rect[indice_do_tiro - 1].left < screen_width:
		            tiro_nave1_rect[indice_do_tiro].center = nave1_rect.center

	    if key_nave1_ciclo < key_delay:
		 key_nave1_ciclo += 1

	#dispara os tiros da nave2
	    for indice_do_tiro in range( numero_de_tiros ):
		if pressed_key[ K_KP5 ] and tiro_nave2_rect[indice_do_tiro].right < 0:
		   if key_nave2_ciclo >= key_delay:
		        key_nave2_ciclo = 0
		        if indice_do_tiro == 0:
		            tiro_nave2_rect[indice_do_tiro].center = nave2_rect.center
		        
		        elif tiro_nave2_rect[indice_do_tiro - 1].right > 0:
		            tiro_nave2_rect[indice_do_tiro].center = nave2_rect.center

	    if key_nave2_ciclo < key_delay:
		 key_nave2_ciclo += 1

	    screen.fill( background_color )
	    screen.blit( title, title_rect )
	    screen.blit( nave1, nave1_rect ) 
	    screen.blit( nave2, nave2_rect )
	    for indice_do_tiro in range( numero_de_tiros ):
		screen.blit( tiro_nave1[indice_do_tiro], tiro_nave1_rect[indice_do_tiro])
		screen.blit( tiro_nave2[indice_do_tiro], tiro_nave2_rect[indice_do_tiro])
	    pygame.display.flip()

            clock.tick( fps )

	#testa colisao
	    if nave1_rect.collidelist( tiro_nave2_rect ) != -1:
                message = "Palyer 2 win"
                estado = "game over"
                a = 0
	    if nave2_rect.collidelist( tiro_nave1_rect ) != -1:
                message = "Player 1 win"
                estado = "game over"


#game over loop
    elif estado == "game over":
        game_over_message = font.render( message, 1, [255, 30, 30] )
        game_over_message_rect = title.get_rect()
        game_over_message_rect.center = screen.get_rect().center

        screen.fill( [0,0,0] )
        screen.blit( game_over_message, game_over_message_rect )
        pygame.display.flip()
       
        '''
        if game_over_ciclo < game_over_delay:
            game_over_ciclo += 1
        else:
        '''
        for return_game in event_list:
            if return_game.type == KEYDOWN:
                estado = "definicoes iniciais"
                game_over_ciclo = 0
            elif return_game.type == KEYUP:
                if return_game.key in  lock_key:
                    estado = "definicoes iniciais"
                    game_over_ciclo = 0
                
        clock.tick( catch_fps )

    else:
        sys.exit( "estado nao encontrado" )
