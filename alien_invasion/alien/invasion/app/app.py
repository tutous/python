import pygame
from pygame.sprite import Group

from alien.invasion.app import settings
from alien.invasion.util import game_stats as gs
from alien.invasion.util import game_functions as gf
from alien.invasion.object.ship import Ship


def run_game():
    # Initialize pygame, settings, and screen object.
    # #pygame.init()
    ai_settings = settings.Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Create an instance to store game statistics.
    stats = gs.GameStats(ai_settings)
    
    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
