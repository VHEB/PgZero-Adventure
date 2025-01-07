import pgzrun
from pygame import image, transform
from Class.hero import Hero
from Class.collectable import Collectable
from Class.enemy import Enemy

WIDTH = 800
HEIGHT = 600

life = 3
coins_collected = 0
font_size = 30
current_screen = "menu"
music_enabled = True  

background_image = image.load("images/background.png")
background_image = transform.scale(background_image, (WIDTH, HEIGHT))

platform_image = image.load("images/ground-1.png")
platform_width = platform_image.get_width()
platform_height = platform_image.get_height()

sounds.background.play()
sounds.background.set_volume(0.5)

platform_rect = Rect(0, HEIGHT - 50, WIDTH, 50)  
platforms = [
    Rect(150, 500, 10, 20),
    Rect(350, 500, 10, 20),
    Rect(600, 500, 10, 20),
    platform_rect,
]

def reset_game():
    global life, coins_collected, hero, enemies, collerctables

    life = 3
    coins_collected = 0

    hero = Hero(100, 300)  

    enemies = [
        Enemy(500, 300, 150, 750),
    ]

    collerctables = [
        Collectable(150, 480),
        Collectable(350, 480),
        Collectable(600, 480),
    ]

reset_game()

buttons = [
    {"text": "Start", "x": 300, "y": 200, "width": 200, "height": 70, "action": "start_game"},
    {"text": "Exit", "x": 300, "y": 400, "width": 200, "height": 70, "action": "exit_game"},
    {"text": "Music On/Off", "x": 300, "y": 300, "width": 200, "height": 70, "action": "toggle_music"},
]


def draw():
    screen.clear()
    if current_screen == "game":
        screen.blit(background_image, (0, 0))
        for x in range(0, WIDTH, platform_width):
            screen.blit(platform_image, (x, HEIGHT - 50))
        hero_update(platforms)
        screen.blit(hero.get_sprite(), (hero.x, hero.y))

        for collectable in collerctables:
            if not collectable.collected:
                screen.blit(collectable.get_sprite(), (collectable.x, collectable.y))

        for enemy in enemies:
            screen.blit(enemy.image, (enemy.x, enemy.y))

        for platform in platforms:
            screen.blit(platform_image, platform.topleft)

        screen.draw.text(f"Life: {life}", (20, 10), fontsize=font_size, color="black")
        screen.draw.text(f"Coins: {coins_collected}", (20, 50), fontsize=font_size, color="black")

    elif current_screen == "menu":
        draw_menu()

    elif current_screen == "lose":
        draw_lose()
    elif current_screen == "win":
        draw_win()

def draw_menu():
    screen.blit(background_image, (0, 0))
    screen.draw.text("Adventure Kodland!", center=(WIDTH // 2, 100), fontsize=40, color="Black")
    for button in buttons:
        screen.draw.filled_rect(Rect((button["x"], button["y"]), (button["width"], button["height"])), "gray")
        screen.draw.text(button["text"], center=(button["x"] + button["width"] // 2, button["y"] + button["height"] // 2), fontsize=30, color="white")

def draw_lose():
    screen.blit(background_image, (0, 0))
    screen.draw.text("You Lost!", center=(WIDTH // 2, HEIGHT // 2 - 100), fontsize=60, color="red")
    screen.draw.filled_rect(Rect((300, 400), (200, 70)), "gray")
    screen.draw.text("Menu", center=(400, 435), fontsize=30, color="white")

def draw_win():
    screen.blit(background_image, (0, 0))
    screen.draw.text("You Win!", center=(WIDTH // 2, HEIGHT // 2 - 100), fontsize=60, color="green")
    screen.draw.filled_rect(Rect((300, 400), (200, 70)), "gray")
    screen.draw.text("Menu", center=(400, 435), fontsize=30, color="white")

def on_mouse_down(pos):
    global current_screen

    if current_screen == "menu":
        for button in buttons:
            button_rect = Rect((button["x"], button["y"]), (button["width"], button["height"]))
            if button_rect.collidepoint(pos):
                if button["action"] == "start_game":
                    reset_game()
                    current_screen = "game"
                elif button["action"] == "exit_game":
                    exit()
                elif button["action"] == "toggle_music":
                    toggle_music() 

    elif current_screen == "lose":
        button_rect = Rect((300, 400), (200, 70))
        if button_rect.collidepoint(pos):
            reset_game()
            current_screen = "menu"
    elif current_screen == "win":
        button_rect = Rect((300, 400), (200, 70))
        if button_rect.collidepoint(pos):
            reset_game()
            current_screen = "menu"

def on_key_down(key):
    if current_screen == "game":
        if key == keys.SPACE and hero.on_ground:
            hero.velocity_y = -20  
        if key == keys.RIGHT:
            hero.velocity_x = hero.speed
        if key == keys.LEFT:
            hero.velocity_x = -hero.speed

def on_key_up(key):
    if current_screen == "game":
        if key in [keys.RIGHT, keys.LEFT]:
            hero.velocity_x = 0

def toggle_music():
    global music_enabled
    music_enabled = not music_enabled
    if music_enabled:
        sounds.background.play()
    else:
        sounds.background.stop()

def hero_update(platforms):
    hero.update(platforms) 

def update():
    global coins_collected, life, current_screen
    if current_screen == "game":
        hero_update(platforms)

        for collectable in collerctables:
            if not collectable.collected and hero.rect.colliderect(collectable.rect):
                collectable.collected = True
                coins_collected += 1
                sounds.coin.play()
                sounds.coin.set_volume(0.5)
                if coins_collected == len(collerctables):
                    current_screen = "win"

        for enemy in enemies:
            enemy.update(platform_rect)
            if hero.rect.colliderect(enemy.rect):
                hero.x, hero.y = 100, HEIGHT - 82
                sounds.hit.play()
                sounds.hit.set_volume(0.5)
                life -= 1
                if life <= 0:
                    current_screen = "lose"

pgzrun.go()
