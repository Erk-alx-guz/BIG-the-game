import pygame
# Button Class
class Button:
    def __init__(self, x, y, width, height, text, font, text_color, bg_color, alpha_min, alpha_max):
        self.rect = pygame.Rect(x, y, width, height)  # Button rectangle
        self.text = text  # Button text
        self.font = font  # Font object
        self.text_color = text_color  # Text color
        self.bg_color = bg_color  # Background color
        self.alpha_min = alpha_min
        self.alpha_max = alpha_max  # Alpha for transparency (0 = fully transparent, 255 = fully opaque)
        
        # Create the background surface
        self.bg_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.bg_surface.fill(self.bg_color)
        self.bg_surface.set_alpha(self.alpha_max)  # Set the transparency
        
        self.text_surf = self.font.render(self.text, True, self.text_color)  # Rendered text surface
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)  # Center text in button

    def reset(self):
        self.bg_surface.set_alpha(self.alpha_max)
    
    def draw(self, screen):
        screen.blit(self.bg_surface, self.rect.topleft)  # Draw the translucent background
        screen.blit(self.text_surf, self.text_rect)  # Draw text on top of button
    
    def is_hovered(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) :
            self.bg_surface.set_alpha(self.alpha_min)
        else:
            self.bg_surface.set_alpha(self.alpha_max)
        return self.rect.collidepoint(pygame.mouse.get_pos())  # Check if mouse is over the button
    
    def is_clicked(self, event):
        return self.is_hovered() and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 # Check if button is clicked
