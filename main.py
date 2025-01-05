import pgzrun
from pygame import image, transform
from Class.hero import Hero
from Class.collectable import Collectable

WIDTH = 800
HEIGHT = 600

hero = Hero(100, 300)
collerctables = [
    Collectable(300, 525),
    Collectable(500, 525),
    Collectable(700, 525)
]

coins_collected = 0
font_size = 30

buttons = [
    {"text": "Start", "x": 300, "y": 200, "width": 200, "height": 70, "action": "start_game"},
    {"text": "Exit", "x": 300, "y": 300, "width": 200, "height": 70, "action": "exit_game"}
]

current_screen = "menu"  # Tela atual do jogo

background_image = image.load("images/background.png")
background_image = transform.scale(background_image, (WIDTH, HEIGHT))

platform_image = image.load("images/ground-1.png")  
platform_width = platform_image.get_width() 
platform_height = platform_image.get_height()
platform_rect = Rect(0, HEIGHT - platform_height, WIDTH, platform_height) 


sounds.background.play()
sounds.background.set_volume(0.5)


def draw():
    screen.clear()
    if current_screen == "game":
        screen.blit(background_image, (0, 0))
        for x in range(0, WIDTH, platform_width):
            screen.blit(platform_image, (x, HEIGHT - platform_height))  # Desenha a plataforma no fundo
        hero.update(platform_rect)  # Atualiza o herói com movimentação
        screen.blit(hero.get_sprite(), (hero.x, hero.y))
        
        for collectable in collerctables:
            if not collectable.collected:
                screen.blit(collectable.get_sprite(), (collectable.x, collectable.y))

        screen.draw.text(f"Coins:  {coins_collected}", (10, 10), fontsize=font_size, color="black")
    
    if current_screen == "menu":
        draw_menu()

def draw_menu():
    screen.blit(background_image, (0, 0))
    screen.draw.text("Adventure Kodland!", center=(WIDTH // 2, 100), fontsize=40, color="Black")
    for button in buttons:
        screen.draw.filled_rect(Rect((button["x"], button["y"]), (button["width"], button["height"])), "gray")
        screen.draw.text(button["text"], center=(button["x"] + button["width"] // 2, button["y"] + button["height"] // 2), fontsize=30, color="white")

def on_mouse_down(pos):
    global current_screen
    
    if current_screen == "menu":
        for button in buttons:
            button_rect = Rect((button["x"], button["y"]), (button["width"], button["height"]))
            if button_rect.collidepoint(pos):
                if button["action"] == "start_game":
                    current_screen = "game"
                elif button["action"] == "exit_game":
                    exit()

def on_key_down(key):
    if current_screen == "game":
        if key == keys.SPACE:
            if hero.on_ground:
                hero.velocity_y = -20
        if key == keys.RIGHT:
            hero.velocity_x = hero.speed
        if key == keys.LEFT:    
            hero.velocity_x = -hero.speed

def on_key_up(key):
    if current_screen == "game":
        if key in [keys.RIGHT, keys.LEFT]:
            hero.velocity_x = 0
def update():
    global coins_collected
    if current_screen == "game":
        hero.update(platform_rect)

        for collectable in collerctables:
            if not collectable.collected and hero.rect.colliderect(collectable.rect):
                collectable.collected = True
                coins_collected += 1
                sounds.coin.play()
                sounds.coin.set_volume(0.5)

pgzrun.go()
