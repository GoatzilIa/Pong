import pygame
from settings import Settings
from pygame.time import Clock
from button import Button
import game_functions as gf

def Game_Intro(p_settings, screen, stats, sb, play_button, paddles, ball, paddle_right, paddle_tr, paddle_br, clock):
    intro = True

    while intro:

        screen.fill((20, 20, 20))
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        smallText =  pygame.font.Font('freesansbold.ttf', 40)
        Text1Surf, Text1Rect = text_objects("Pong", largeText)
        Text2Surf, Text2Rect = text_objects("AI - No Walls", smallText)

        Text1Rect.center = ((p_settings.screen_width / 2), (p_settings.screen_height / 5))
        screen.blit(Text1Surf, Text1Rect)
        Text2Rect.center = ((p_settings.screen_width / 2), ((p_settings.screen_height / 20 )* 7))
        screen.blit(Text2Surf, Text2Rect)

        play_button.draw_button()
        gf.check_events(p_settings, screen, stats, sb, play_button, paddles, ball, paddle_right, paddle_tr, paddle_br)
        if stats.game_active:
            intro = False

        pygame.display.update()
        clock.tick(60)

def text_objects(text, font):
    textSurface = font.render(text, True,(255, 255, 255) )
    return textSurface, textSurface.get_rect()