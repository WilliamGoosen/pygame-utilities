import pygame as pg
from pathlib import Path
from pygame_utilities import Button, ImageButton, draw_text

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
FONT_NAME = "arial"

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
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

    # Screen grid layout
    LEFT_COLUMN = 50
    MIDDLE_COLUMN = SCREEN_WIDTH // 2
    RIGHT_COLUMN = SCREEN_WIDTH - 50
    TOP_ROW = 80
    MIDDLE_ROW = SCREEN_HEIGHT // 2
    ROW_HEIGHT = 80

    # Create "Light" to turn on and off
    black_white_circle = pg.Rect((MIDDLE_COLUMN - 25, TOP_ROW, 50, 50))

    # Create Blue and red buttons with default and custom corner radius
    red_button = Button(
        screen, LEFT_COLUMN, MIDDLE_ROW, RED, 75, 50, text="Sharp Corners", text_size=12
    )
    blue_button = Button(
        screen,
        LEFT_COLUMN,
        MIDDLE_ROW + ROW_HEIGHT,
        BLUE,
        75,
        50,
        text="Rounded Corners",
        text_size=12,
        border_radius=12,
    )

    # Create image buttons with state images, or uisng fallback tinting of normal image
    img_button = ImageButton(
        screen,
        RIGHT_COLUMN,
        MIDDLE_ROW,
        normal_img,
        hover_image=hovered_img,
        pressed_image=pressed_img,
        text="State Images",
        text_size=12,
        anchor_x="right",
    )
    img_button2 = ImageButton(
        screen,
        RIGHT_COLUMN,
        MIDDLE_ROW + ROW_HEIGHT,
        normal_img,
        text="Tint Fallback",
        text_size=12,
        anchor_x="right",
    )

    # Create three buttons to demo anchor_x usage
    left_anchored = Button(
        screen,
        MIDDLE_COLUMN,
        MIDDLE_ROW,
        colour=GREEN,
        width=100,
        height=30,
        text="Left",
        anchor_x="left",
        text_size=12,
        text_colour=BLACK,
    )

    center_anchored = Button(
        screen,
        MIDDLE_COLUMN,
        MIDDLE_ROW + ROW_HEIGHT,
        colour=GREEN,
        width=100,
        height=30,
        text="Center",
        anchor_x="center",
        text_size=12,
        text_colour=BLACK,
    )

    right_anchored = Button(
        screen,
        MIDDLE_COLUMN,
        MIDDLE_ROW + ROW_HEIGHT * 2,
        colour=GREEN,
        width=100,
        height=30,
        text="Right",
        anchor_x="right",
        text_size=12,
        text_colour=BLACK,
    )

    # List of created buttons for easier update and draw handling
    buttons: list[Button | ImageButton] = [
        red_button,
        blue_button,
        img_button,
        img_button2,
        left_anchored,
        center_anchored,
        right_anchored,
    ]

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

        # Descriptions for demo buttons
        draw_text(
            screen, "Buttons toggle", 18, MIDDLE_COLUMN, TOP_ROW - 40, colour=BLACK
        )
        draw_text(screen, "On / Off", 18, MIDDLE_COLUMN, TOP_ROW - 20, colour=BLACK)

        draw_text(
            screen,
            "Colour Buttons",
            18,
            LEFT_COLUMN + 38,
            MIDDLE_ROW - 50,
            colour=BLACK,
        )

        draw_text(
            screen,
            'Buttons alligned using "anchor_x"',
            18,
            MIDDLE_COLUMN,
            MIDDLE_ROW - 50,
            colour=BLACK,
        )

        draw_text(
            screen,
            "Image Buttons",
            18,
            RIGHT_COLUMN - 38,
            MIDDLE_ROW - 50,
            colour=BLACK,
        )

        # Draw anchor demonstration line
        pg.draw.line(
            screen,
            WHITE,
            (MIDDLE_COLUMN, MIDDLE_ROW - 20),
            (MIDDLE_COLUMN, MIDDLE_ROW + ROW_HEIGHT * 2 + 50),
            2,
        )

        for button in buttons:
            button.update(mouse_pos)
            button.draw()

        pg.display.flip()
    pg.quit()


if __name__ == "__main__":
    main()
