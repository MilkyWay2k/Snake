import pygame
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
score = 0
fps = 5
lose = False

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
score_font = pygame.font.SysFont('Arial', 30, bold = True)
end_font = pygame.font.SysFont('Arial', 120, bold = True)

def reset():
	global x, y, apple, dirs, length, dx, dy, score, fps, lose, snake
	x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
	apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
	dirs = {'W': True, 'S': True, 'A': True, 'D': True}
	length = 1
	snake = [(x, y)]
	dx, dy = 0, 0
	score = 0
	fps = 5
	lose = False


while True:
	sc.fill(pygame.Color('black'))
	# Рисование змеи и яблока
	[(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE - 3, SIZE - 3))) for i, j in snake]
	pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))

	# Передвижение змеи
	if not lose:
		x += dx * SIZE
		y += dy * SIZE
		snake.append((x, y))
		snake = snake[-length:]

		#Змейка кушает яблоко
		if snake[-1] == apple:
			apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
			length += 1
			score += 1
			fps += 1

	#Показ очков
	render_score = score_font.render(f'SCORE: {score}', 1, pygame.Color('red'))
	sc.blit(render_score, (5, 5))

	#Проигрыш
	if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
		lose = True
		#while True:
			#render_end = end_font.render('ПРОИГРЫШ!', 1, pygame.Color('red'))
			#sc.blit(render_end, (RES // 2 - 385, RES // 3))
			#pygame.display.flip()
			#for event in pygame.event.get():
				#if event.type == pygame.QUIT:
					#exit()
	if lose:
		render_end = end_font.render('ПРОИГРЫШ!', 1, pygame.Color('red'))
		sc.blit(render_end, (RES // 2 - 385, RES // 3))


	pygame.display.flip()
	clock.tick(fps)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	#Управление
	key = pygame.key.get_pressed()
	if key[pygame.K_r] and lose:
		reset()
	if not lose:
		if key[pygame.K_w] and dirs['W']:
			dx, dy = 0, -1
			dirs = {'W': True, 'S': False, 'A': True, 'D': True}
		if key[pygame.K_s] and dirs['S']:
			dx, dy = 0, 1
			dirs = {'W': False, 'S': True, 'A': True, 'D': True}
		if key[pygame.K_a] and dirs['A']:
			dx, dy = -1, 0
			dirs = {'W': True, 'S': True, 'A': True, 'D': False}
		if key[pygame.K_d] and dirs['D']:
			dx, dy = 1, 0
			dirs = {'W': True, 'S': True, 'A': False, 'D': True}
