import pygame
pygame.init()

BLUE = (113, 169, 171)

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image")

fps = pygame.time.Clock()

class Cat:
    def __init__(self, x, y, width, heigt, images):
        self.images = [pygame.transform.scale(pygame.image.load(img), (width, heigt)) for img in images]
        self.speed = 0.05
        self.index = 0
        self.block = self.images[0].get_rect(topleft=(x,y))
        self.current_image = self.images[0]
        

    def show(self):
        window.blit(self.current_image, (self.block.x, self.block.y))

    def animate(self):
        self.index += self.speed
        if self.index >= len(self.images):
            self.index = 0
        self.current_image = self.images[int(self.index)]

images = [f"dance-cat-{i}.png" for i in range (1, 3)]
cat = Cat(318, 160, 165, 135, images)

button_rect = pygame.Rect(318, 340, 165, 35)
font = pygame.font.SysFont("Arial", 16)
text = font.render("Play", True, (255,255,255))

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        


    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    print("B")
    
    window.fill(BLUE)
    cat.show()
    cat.animate()

    pygame.draw.rect(window, (0, 0, 250), button_rect)

    window.blit(text, (button_rect.x + 25, button_rect.y + 5))

    pygame.display.flip()
    fps.tick(60)

pygame.quit()


