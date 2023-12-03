import pygame 

# Game size 
COLUMNS = 10
ROWS = 20
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE

# side bar size 
SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

# window
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

# game behaviour 
UPDATE_START_SPEED = 300
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET = pygame.Vector2(COLUMNS // 2, -1)

# Colors 
YELLOW = '#f1e60d'
YELLOW_F = '#938c07'
RED = '#e51b20'		
RED_F = '#8b0f12'
BLUE = '#204b9b'	
BLUE_F = '#1a3e80'
GREEN = '#65b32e'	
GREEN_F = '#457b1f'
PURPLE = '#7b217f'	
PURPLE_F = '#2b0b2d'
CYAN = '#6cc6d9'	
CYAN_F = '#1f6b7b'
ORANGE = '#f07e13'	
ORANGE_F = '#914b09'
PURPLE_D = '#282130'
GRAY = '#1C1C1C'
LINE_COLOR = '#4c3f5b'

# shapes
TETROMINOS = {
	'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': PURPLE, 'color_f': PURPLE_F},
	'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'color': YELLOW, 'color_f': YELLOW_F},
	'J': {'shape': [(0,0), (0,-1), (0,1), (-1,1)], 'color': BLUE, 'color_f': BLUE_F},
	'L': {'shape': [(0,0), (0,-1), (0,1), (1,1)], 'color': ORANGE, 'color_f': ORANGE_F},
	'I': {'shape': [(0,0), (0,-1), (0,-2), (0,1)], 'color': CYAN, 'color_f': CYAN_F},
	'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'color': GREEN, 'color_f': GREEN_F},
	'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': RED, 'color_f': RED_F}
}

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200}