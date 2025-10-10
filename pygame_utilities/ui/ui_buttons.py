import pygame as pg
from .text_drawing import draw_text
from typing import Optional

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Button:
    def __init__(
            self, surface: pg.Surface,
            x: int,
            y: int,
            colour: tuple[int, int, int] = BLACK,
            width: int = 50,
            height: int = 50,
            text: str = "",
            text_size: int = 20,
            text_colour: tuple[int, int, int] = WHITE,
            anchor_x: str = "left",     # "left", "center", "right"
            anchor_y: str = "top",      # "top", "center", "bottom"
            border_radius: int = 0
            ) -> None:
        
        if anchor_x == "center":
            x -= width // 2
        elif anchor_x == "right":
            x -= width
        
        if anchor_y == "center":
            y -= height // 2
        elif anchor_y == "bottom":
            y -= height

        self.surface = surface
        self.border_radius = border_radius
        self.text = text
        self.text_size = text_size
        self.text_colour = text_colour
        self.normal_colour = colour
        self.hovered_colour = tuple(min(c + 75, 255) for c in self.normal_colour)
        self.pressed_colour = tuple(max(c - 75, 0) for c in self.normal_colour)
        self.rect = pg.Rect((x, y, width, height))
        self.is_hovered = False
        self.is_pressed = False
        
    def update(self, mouse_pos: tuple[int, int]) -> None:
        self.check_hover(mouse_pos)
        
    def check_hover(self, mouse_pos) -> None:
        if self.rect.collidepoint(mouse_pos):
            self.is_hovered = True
        else:
            self.is_hovered = False
            
    def handle_event(self, event: pg.Event) -> bool:
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_pressed = True
                return False
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            if self.is_pressed and self.rect.collidepoint(event.pos):
                self.is_pressed = False
                return True
            self.is_pressed = False
        return False
    
    def draw(self) -> None:
        if self.is_pressed:
            pg.draw.rect(self.surface, self.pressed_colour, self.rect, border_radius = self.border_radius)
        elif self.is_hovered:
            pg.draw.rect(self.surface, self.hovered_colour, self.rect, border_radius = self.border_radius)
        else:
            pg.draw.rect(self.surface, self.normal_colour, self.rect, border_radius = self.border_radius)
            
        draw_text(self.surface, self.text, self.text_size, self.rect.centerx, self.rect.centery, align_x = "center", align_y = "center")


class ImageButton:
    def __init__(self,
                 surface: pg.Surface,
                 x: int,
                 y: int,
                 normal_image: pg.Surface,
                 hover_image: Optional[pg.Surface] = None,
                 pressed_image: Optional[pg.Surface] = None,
                 text: str = "",
                 text_size: int = 20,
                 text_colour: tuple[int, int, int] = WHITE,
                 border_radius: int = 0,
                 anchor_x: str = "left",
                 anchor_y: str = "top"
                 ) -> None:

        self.button = Button(
            surface,
            x,
            y,
            width = normal_image.get_width(),
            height = normal_image.get_height(),
            text = text,
            text_size = text_size,
            anchor_x=anchor_x,
            anchor_y=anchor_y,
            text_colour = text_colour
            )
        self.normal_image = normal_image
        self.hover_image = hover_image
        self.pressed_image = pressed_image

    def update(self, mouse_pos) -> None:
        return self.button.update(mouse_pos)
    
    def handle_event(self, event) -> bool:
        return self.button.handle_event(event)

    def draw(self) -> None:
        if self.button.is_pressed:
            image = self.pressed_image or self._tint_image(self.normal_image, (25, 25, 25))
        elif self.button.is_hovered:
            image = self.hover_image or self._highlight_image(self.normal_image, (25, 25, 25))
        else:
            image = self.normal_image

        self.button.surface.blit(image, self.button.rect)
            
        draw_text(self.button.surface, self.button.text, self.button.text_size, self.button.rect.centerx, self.button.rect.centery, align_x = "center", align_y = "center")

    def _highlight_image(self, image: pg.Surface, tint_colour: tuple[int, ...]) -> pg.Surface:
        tinted = image.copy()
        tinted.fill(tint_colour, special_flags = pg.BLEND_RGB_ADD)
        return tinted
        
    def _tint_image(self, image: pg.Surface, tint_colour: tuple[int, ...]) -> pg.Surface:
        tinted = image.copy()
        tinted.fill(tint_colour, special_flags = pg.BLEND_RGB_SUB)
        return tinted