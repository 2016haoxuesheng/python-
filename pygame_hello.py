#这是用Pygame实现hello
import pygame
import sys

pygame.init()
pygame.display.set_mode((1200, 700))
pygame.display.set_caption("hello")
#第7行，点睛之笔(真正实现了hello)
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
