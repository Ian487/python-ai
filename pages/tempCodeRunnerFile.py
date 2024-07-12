import pygame
import random

# 初始化 Pygame
pygame.init()

# 設置屏幕大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 設置顏色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 設置遊戲時鐘
clock = pygame.time.Clock()

# 設置角色
player_size = 50
player_x = 50
player_y = screen_height - player_size
player_velocity_y = 0
gravity = 1
jump_strength = 15

# 設置障礙物
obstacle_width = 20
obstacle_height = 70
obstacle_color = red
obstacle_speed = 5
obstacle_list = []


# 創建障礙物
def create_obstacle():
    x_pos = screen_width
    y_pos = screen_height - obstacle_height
    obstacle_list.append([x_pos, y_pos])


# 遊戲主循環
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_y == screen_height - player_size:
                player_velocity_y = -jump_strength

    # 更新角色位置
    player_velocity_y += gravity
    player_y += player_velocity_y
    if player_y > screen_height - player_size:
        player_y = screen_height - player_size
        player_velocity_y = 0

    # 更新障礙物位置
    for obstacle in obstacle_list:
        obstacle[0] -= obstacle_speed
    if len(obstacle_list) > 0 and obstacle_list[0][0] < -obstacle_width:
        obstacle_list.pop(0)

    # 創建新的障礙物
    if len(obstacle_list) == 0 or obstacle_list[-1][0] < screen_width - 300:
        create_obstacle()

    # 檢查碰撞
    for obstacle in obstacle_list:
        if (
            player_x < obstacle[0] + obstacle_width
            and player_x + player_size > obstacle[0]
            and player_y + player_size > obstacle[1]
        ):
            running = False

    # 繪製屏幕
    screen.fill(white)
    pygame.draw.rect(screen, black, (player_x, player_y, player_size, player_size))
    for obstacle in obstacle_list:
        pygame.draw.rect(
            screen,
            obstacle_color,
            (obstacle[0], obstacle[1], obstacle_width, obstacle_height),
        )

    pygame.display.update()
    clock.tick(30)

pygame.quit()