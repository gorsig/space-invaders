import pygame

HEIGHT = 800
WIDTH = 600


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    running = True

    while running:
        # Process input/events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == '__main__':
    main()
