from graphics import Canvas
import time
import random
    
"Global constants"
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
BLOCK_SIZE = 20
DELAY = 0.01
'This is the key for the player and the score items and their color options'
color_key = {} 
color_key[1] = 'red'
color_key[2] = 'blue'
color_key[3] = 'green'
color_cycle = 1


def main(): 
    
    '''This code introduces the game in a simple 
    layout that dissapears after a click, the game starts after'''
    borders = 0
    SCORE = int(0)
    
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    TrailEcho = canvas.create_text(CANVAS_WIDTH*0.6, CANVAS_HEIGHT*.52, anchor = 'center', font='Times', font_size = 50, text='BLAZER', color='red')
    canvas.set_hidden(TrailEcho, True)
    TrailTitle = canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, anchor = 'center', font='Times', font_size = 50, text='TRAILBLAZER', color='black')
    
    time.sleep(DELAY*100)
    canvas.set_hidden(TrailEcho, False)
    
    time.sleep(DELAY*100)
    Creator_Title = canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT*0.6, anchor = 'center', font='Times', font_size = 25, text='by AMARI', color='black')
    Title_Instruction = canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT*0.77, anchor = 'center', font='Arial', font_size = 15, text='ARROWS TO MOVE, SPACE TO CHANGE COLOR, CLICK TO START', color='black')
    
    time.sleep(DELAY*100)
    canvas.wait_for_click()
      # no longer visible
    canvas.set_hidden(TrailEcho, True)  # no longer visible
    canvas.set_hidden(Creator_Title, True)  # no longer visible
    canvas.set_hidden(Title_Instruction, True)
    
    time.sleep(DELAY*20)
    canvas.set_hidden(TrailEcho, False)
    time.sleep(DELAY*20)
    canvas.set_hidden(TrailEcho, True)
    time.sleep(DELAY*20)
    canvas.set_hidden(TrailEcho, False)
    time.sleep(DELAY*20)
    canvas.set_hidden(TrailEcho, True)
    time.sleep(DELAY*20)
    canvas.set_hidden(TrailEcho, False)
    time.sleep(DELAY*20)
    canvas.set_hidden(TrailEcho, True)
    time.sleep(DELAY*20)
    canvas.set_hidden(TrailEcho, False)
    time.sleep(DELAY*20)
    canvas.set_hidden(TrailEcho, True)
    canvas.set_hidden(TrailTitle, True)
    start_game(canvas, borders, random, SCORE)
    
    
   
def start_game(canvas, borders, random, SCORE):
    
    'The next few variables determine the cell limits of the arena based on the global constants above'
    xline_count = int(CANVAS_WIDTH / BLOCK_SIZE)
    yline_count = int(CANVAS_HEIGHT / BLOCK_SIZE)
    req_pieces = 0
    
    'These next 10 lines create the arena, the lines and the borders'
    leftborder = canvas.create_rectangle(0, 0, BLOCK_SIZE, CANVAS_HEIGHT, 'gray')
    rightborder = canvas.create_rectangle((CANVAS_WIDTH - BLOCK_SIZE), 0, CANVAS_WIDTH, CANVAS_HEIGHT, 'gray')
    topborder = canvas.create_rectangle(0, 0, CANVAS_WIDTH, BLOCK_SIZE, 'gray')
    bottomborder = canvas.create_rectangle(0, (CANVAS_HEIGHT - BLOCK_SIZE), CANVAS_WIDTH, CANVAS_HEIGHT, 'gray')
    borders = [leftborder, rightborder, topborder, bottomborder]
    
    for i in range (yline_count):
        canvas.create_line(0, i*BLOCK_SIZE, CANVAS_WIDTH, i*BLOCK_SIZE, 'gray')
    for i in range (xline_count):
        canvas.create_line(i*BLOCK_SIZE, 0, i*BLOCK_SIZE, CANVAS_HEIGHT, 'gray')
   
    'After the player clicks, the game initiates here'
    play_game(canvas, borders, req_pieces, random, SCORE)
    
    
    
def play_game(canvas, borders, req_pieces, random, SCORE):
    
    'Variables that deternine the starting movement of the player/spawns and change throughout'
    spawn_boolean = 0
    
    '''This determines the size of the arena, 
    determining how many cells there are 
    vertically and horizontally based on the size'''
    xline_count = int(CANVAS_WIDTH / BLOCK_SIZE) - 2 
    yline_count = int(CANVAS_HEIGHT / BLOCK_SIZE) - 2
    random_x = BLOCK_SIZE * (random.randint(1, xline_count))
    random_y = BLOCK_SIZE * (random.randint(1, yline_count))
    player_x = random_x + (BLOCK_SIZE / 2)
    player_y = random_y + (BLOCK_SIZE / 2)
    vertical = 0
    horizontal = BLOCK_SIZE
    color_cycle = 1
    move_interval = 3
    move_counter = 0
    SCORE = 0
    trail_length = 0
    trail_loss = 1
    trail = []
    
    player = canvas.create_rectangle(random_x, random_y, (random_x + BLOCK_SIZE), (random_y + BLOCK_SIZE), color_key[1])
    canvas.set_outline_color(player, 'black')
    req_pieces = [player, borders, canvas]
    
    'These following variables are associated with spawns and their spawn rate'
    left_spawns = []
    top_spawns = []
    right_spawns = []
    bottom_spawns = []
    spawn_delay_counter = 0
    spawn_delay = 300
    initial_delay = spawn_delay
    enemy_accelerant = 14
    enemy_speed = int(BLOCK_SIZE / enemy_accelerant)
    score_change = 0
    scoretext = []
    
    spawns_dict = {}
    trail_leftx_dict = {}
    trail_topy_dict = {}
    
    while(True):
        
        '''The following ~25 lines of code check where the player is 
        and takes keyboard inputs, arrow keys to initiate movement and 
        space to initiate color changes that cycle through 4 colors'''
        key = canvas.get_last_key_press() 
        player_x = canvas.get_left_x(player) 
        player_y = canvas.get_top_y(player)
    
        if trail_length >= 10:
            move_interval = 1
        if 5 <= trail_length < 10:
            move_interval = 2
        if trail_length < 5:
            move_interval = 3
        
        'This is how the player changes colors, using the dictionary of colors above'
        if key == ' ':
            if trail_length >= trail_loss:
                trail_length -= trail_loss
            if trail_length < trail_loss:
                trail_length = 0
            if color_cycle == 3:
                color_cycle = 1
            else:
                color_cycle += 1
            canvas.set_color(player, color_key[color_cycle])
            for trail_piece in trail:
                canvas.delete(trail_piece)
                
        if key == 'ArrowLeft':
            vertical = 0
            horizontal = -BLOCK_SIZE
        if key == 'ArrowRight':
            vertical = 0
            horizontal = BLOCK_SIZE
        if key == 'ArrowUp':
            vertical = -BLOCK_SIZE
            horizontal = 0
        if key == 'ArrowDown':
            vertical = BLOCK_SIZE
            horizontal = 0
        
        '''The next 10 lines performs basic movement and 
        allows the player to appear on the other side of the map 
        if they reach the borders, making the map feel like an infinite or a globe'''
        if player_x < 0: 
            canvas.move(player, CANVAS_WIDTH, 0)
        elif player_x > (CANVAS_WIDTH - BLOCK_SIZE):
            canvas.move(player, -CANVAS_WIDTH, 0)
        elif player_y < 0:
            canvas.move(player, 0, CANVAS_HEIGHT)
        elif player_y > (CANVAS_HEIGHT - BLOCK_SIZE):
            canvas.move(player, 0, -CANVAS_HEIGHT)
        elif move_counter >= move_interval:
            canvas.move(player, horizontal, vertical)
            move_counter = 0
            if trail_length > 0:
                new_trail = trail.append(canvas.create_rectangle(player_x, player_y, (player_x + BLOCK_SIZE), (player_y + BLOCK_SIZE), color = 'white', outline = color_key[color_cycle]))
                trail_leftx_dict[trail[-1]] = player_x
                trail_topy_dict[trail[-1]] = player_y
                if len(trail) >= trail_length and len(trail) > 0:
                    canvas.delete(trail[-(trail_length)])
                
        else:
            move_counter += 1
        
        if spawn_boolean == 0:
            
            random_axis = (BLOCK_SIZE * random.randint(1, (yline_count-2)))
            random_placement = random.randint(BLOCK_SIZE, BLOCK_SIZE * 10)
            color_selector = random.randint(1, 3)
            left_spawns.append(canvas.create_oval(-random_placement, random_axis, (-random_placement + BLOCK_SIZE), (random_axis + BLOCK_SIZE), color_key[color_selector]))
            spawns_dict[left_spawns[-1]] = color_selector
            if len(left_spawns) >= 8:
                canvas.delete(left_spawns[-8])
            random_axis = (BLOCK_SIZE * random.randint(1, (xline_count-2)))
            random_placement = random.randint(BLOCK_SIZE, BLOCK_SIZE * 10)
            color_selector = random.randint(1, 3)
            top_spawns.append(canvas.create_oval(random_axis, -random_placement, (random_axis + BLOCK_SIZE), (-random_placement + BLOCK_SIZE), color_key[color_selector]))
            spawns_dict[top_spawns[-1]] = color_selector
            if len(top_spawns) >= 8:
                canvas.delete(top_spawns[-8])
            random_axis = (BLOCK_SIZE * random.randint(1, (yline_count-2)))
            random_placement = random.randint(BLOCK_SIZE, BLOCK_SIZE * 10)
            color_selector = random.randint(1, 3)
            right_spawns.append(canvas.create_oval((CANVAS_WIDTH + random_placement), random_axis, (CANVAS_WIDTH + random_placement + BLOCK_SIZE), (random_axis + BLOCK_SIZE), color_key[color_selector]))
            spawns_dict[right_spawns[-1]] = color_selector
            if len(right_spawns) >= 8:
                canvas.delete(right_spawns[-8])
            random_axis = (BLOCK_SIZE * random.randint(1, (xline_count-2)))
            random_placement = random.randint(BLOCK_SIZE, BLOCK_SIZE * 10)
            color_selector = random.randint(1, 3)
            bottom_spawns.append(canvas.create_oval(random_axis, (CANVAS_HEIGHT + random_placement), (random_axis + BLOCK_SIZE), (CANVAS_HEIGHT + random_placement + BLOCK_SIZE), color_key[color_selector]))
            spawns_dict[bottom_spawns[-1]] = color_selector
            if len(bottom_spawns) >= 8:
                canvas.delete(bottom_spawns[-8])
            spawn_boolean = 1
        
        for spawn in left_spawns:
            canvas.move(spawn, enemy_speed, 0)
        for spawn in top_spawns:
            canvas.move(spawn, 0, enemy_speed)
        for spawn in right_spawns:
            canvas.move(spawn, -enemy_speed, 0)
        for spawn in bottom_spawns:
            canvas.move(spawn, 0, -enemy_speed)
            
  
        'The area controlled by the player is the capture zone'
        capturex = player_x
        capturey = player_y
        score_multiplier = trail_length
        score_change = 0
    
        '''The code below determines what objects are 
        underneath the player and whether they are 
        score objects or just part of the arena'''
        captured = canvas.find_overlapping(capturex, capturey, capturex + BLOCK_SIZE, capturey + BLOCK_SIZE)
        for captured_object in captured:
            if captured_object not in req_pieces and captured_object not in borders and captured_object not in trail:
                if color_cycle != spawns_dict[captured_object]:
                    canvas.delete(captured_object)
                    score_change = int(-10)
                    SCORE += score_change
                    trail_length = 0
                    print(SCORE)
                    scoretext.append(canvas.create_text(capturex + (BLOCK_SIZE/2), capturey + (BLOCK_SIZE/2), font='Times', font_size = 15, text=str(score_change), color = 'black'))
                    if len(scoretext) >= 2:
                        canvas.delete(scoretext[-2])
                    for trail_piece in trail:
                        canvas.delete(trail_piece)
                        trail_leftx_dict.remove[trail_piece]
                        trail_topy_dict.remove[trail_piece]
                if color_cycle == spawns_dict[captured_object]:
                    canvas.delete(captured_object)
                    score_change = int(10 + 10 * score_multiplier)
                    SCORE += score_change
                    trail_length += 1
                    print(SCORE)
                    scoretext.append(canvas.create_text(capturex + (BLOCK_SIZE/2), capturey + (BLOCK_SIZE/2), font='Times', font_size = 15, text=str(score_change), color = 'black'))
                    if len(scoretext) >= 2:
                        canvas.delete(scoretext[-2])
        
        if len(trail) > 0:
            for trail_part in trail:
                trailx = trail_leftx_dict[trail_part]
                traily = trail_topy_dict[trail_part]
                trailcaptured = canvas.find_overlapping(trailx, traily, trailx + BLOCK_SIZE, traily + BLOCK_SIZE)
                if len(trailcaptured) > 1:
                    for captured_object in trailcaptured:
                        if captured_object not in req_pieces and captured_object not in borders and captured_object not in trail:
                            if color_cycle != spawns_dict[captured_object]:
                                canvas.delete(captured_object)
                                score_change = int(-10)
                                SCORE += score_change
                                trail_length = 0
                                print(SCORE)
                                scoretext.append(canvas.create_text(trailx + (BLOCK_SIZE/2), traily + (BLOCK_SIZE/2), font='Times', font_size = 15, text=str(score_change), color = 'black'))
                                if len(scoretext) >= 2:
                                    canvas.delete(scoretext[-2])
                                for trail_piece in trail:
                                    canvas.delete(trail_piece)
                                    trail_leftx_dict.remove[trail_piece]
                                    trail_topy_dict.remove[trail_piece]
                            if color_cycle == spawns_dict[captured_object]:
                                canvas.delete(captured_object)
                                score_change = int(10 + 10 * score_multiplier)
                                SCORE += score_change
                                trail_length += 1
                                print(SCORE)
                                scoretext.append(canvas.create_text(trailx + (BLOCK_SIZE/2), traily + (BLOCK_SIZE/2), font='Times', font_size = 15, text=str(score_change), color = 'black'))
                                if len(scoretext) >= 2:
                                    canvas.delete(scoretext[-2])
   
        'Runs the code that detects if the player has caught a score object underneath'
        
        '''Basis for the player animation delay, 
        for every 2 movements of the player, 
        the other pieces move once'''
        time.sleep(DELAY) 
        
        if spawn_delay_counter < spawn_delay:
            spawn_delay_counter += 1
        if spawn_delay_counter >= spawn_delay:
            spawn_delay_counter = 0
            spawn_boolean = 0
            if spawn_delay > int(initial_delay/20):
                spawn_delay -= int(initial_delay/30)
                print('speed increased')
                enemy_accelerant -= 3
            
    

if __name__ == '__main__':
    main()