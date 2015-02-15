while 1:
    #create a empty list
    enemies = []
    
    # The number of current enemy ships within range
    # enemy: The name of this enemy
    # dist: The distance to your cannon of this enemy
    enemy, dist = input().split()
    dist = int(dist)
    enemies.append([enemy,dist])
    enemies = sorted(enemies, key = lambda x: x[1])
    print(enemies[0][0]) # The name of the most threatening enemy (HotDroid is just one example)
