import pygame as pg
from pathlib import Path
from pygame_utilities import Button, ImageButton

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
FONT_NAME = "arial"

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CORNFLOWER_BLUE = (99, 149, 238)


def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Button Demo")
    clock = pg.time.Clock()

    assets_dir = Path(__file__).parent / "assets"
    normal_img = pg.image.load(assets_dir / "button_normal.png").convert_alpha()
    hovered_img = pg.image.load(assets_dir / "button_hovered.png").convert_alpha()
    pressed_img = pg.image.load(assets_dir / "button_pressed.png").convert_alpha()

    black_white_circle = pg.Rect((SCREEN_WIDTH *9 // 20, SCREEN_HEIGHT // 6, 50, 50))

    red_button = Button(screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3, RED, 75, 50, text="Red Button", text_size=12, border_radius=12)
    blue_button = Button(screen, SCREEN_WIDTH * 2 // 5, SCREEN_HEIGHT * 2 // 3, BLUE, 75, 50, text="Blue Button", text_size=12, border_radius=12)
    img_button = ImageButton(screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3, normal_img, hover_image=hovered_img, pressed_image=pressed_img, text="Image Button", text_size=12)
    img_button2 = ImageButton(screen, SCREEN_WIDTH * 2 // 5, SCREEN_HEIGHT // 3, normal_img, text="Tint", text_size=12)

    buttons: list[Button | ImageButton] = [red_button, blue_button, img_button, img_button2]

    light_on = False

    running = True
    while running:
        clock.tick(60)
        mouse_pos = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            for button in buttons:
                if button.handle_event(event):
                    light_on = not light_on

        screen.fill(CORNFLOWER_BLUE)

        if light_on:
            pg.draw.rect(screen, WHITE, black_white_circle, border_radius=25)
        else:
            pg.draw.rect(screen, BLACK, black_white_circle, border_radius=25)

        for button in buttons:
            button.update(mouse_pos)
            button.draw()

        pg.display.flip()
    pg.quit()

if __name__ == "__main__":
    main()