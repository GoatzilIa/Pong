import pygame
from settings import Settings
from pygame.time import Clock
from button import Button
import game_functions as gf

def Game_Over(p_settings, screen, stats, sb, play_button, paddles, ball, paddle_right, paddle_tr, paddle_br, clock):
    """creates a start screen"""
    over = True

    while over:
        """shows the start screen until the player clicks the play button"""
        screen.fill((20, 20, 20))
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        smallText =  pygame.font.Font('freesansbold.ttf', 40)
        smallerText = pygame.font.Font('freesansbold.ttf', 30)
        Text1Surf, Text1Rect = text_objects("Game Over", largeText)
        Text2Surf, Text2Rect = text_objects("Play Again?", smallText)

        if stats.ai_score == 5:
            Text3Surf, Text3Rect = text_objects("AI Won!", smallerText)
        elif stats.p_score == 5:
            Text3Surf, Text3Rect = text_objects("You Won!", smallerText)

        Text1Rect.center = ((p_settings.screen_width / 2), (p_settings.screen_height / 20) * 4)
        screen.blit(Text1Surf, Text1Rect)
        Text2Rect.center = ((p_settings.screen_width / 2), (p_settings.screen_height / 20) * 14)
        screen.blit(Text2Surf, Text2Rect)
        Text3Rect.center = ((p_settings.screen_width / 2), (p_settings.screen_height / 20) * 7)
        screen.blit(Text3Surf, Text3Rect)

        # checks if the play button has been pressed
        play_button.draw_button()
        gf.check_events(p_settings, screen, stats, sb, play_button, paddles, ball, paddle_right, paddle_tr, paddle_br)
        if stats.game_active:
            over = False

        pygame.display.update()
        clock.tick(60)

def text_objects(text, font):
    textSurface = font.render(text, True,(255, 0, 0) )
    return textSurface, textSurface.get_rect()