while 1:
    #create a empty list
    enemies = []
    
    # The number of current enemy ships within range
    # enemy: The name of this enemy
    # dist: The distance to your cannon of this enemy
    enemy, dist = input().split()
    dist = int(dist)
    enemies.append([dist,enemy])
    enemies = sorted(enemies)
    print(enemies[0][1]) # The name of the most threatening enemy (HotDroid is just one example)
