import pygame as pg

def draw_text(
        surf: pg.Surface,
        text: str,
        size: int,
        x: int,
        y: int,
        font_name: str = "arial",
        colour: tuple = (255, 255, 255),
        align_x: str = "center",
        align_y: str = "center"
        ) -> None:
    
    font_match = pg.font.match_font(font_name)
    font = pg.font.Font(font_match, size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect()

    # Horizontal alignment
    if align_x == "left":
        text_rect.left = x
    elif align_x == "center":
        text_rect.centerx = x
    elif align_x == "right":
        text_rect.right = x
    
    # Vertical alignment  
    if align_y == "top":
        text_rect.top = y
    elif align_y == "center":
        text_rect.centery = y
    elif align_y == "bottom":
        text_rect.bottom = y
    
    surf.blit(text_surface, text_rect)