from copy import deepcopy
grid_size = input()
rows = int(grid_size[0])
cols = int(grid_size[2])
#print (rows,cols)
state_values = []
for i in range(rows):
    temp = input()
    temp = list(temp.split(" "))
    #print(temp)
    temp = list(map(float, temp))
    #print (temp)
    state_values.append(temp)
end_walls = input()
numends = int(end_walls[0])
numwalls = int(end_walls[2])
#print (numends,numwalls)
end_coords = []
for i in range(numends):
    temp = input()
    temp = list(temp.split(" "))
    temp = list(map(int, temp))
    #print (temp)
    end_coords.append(temp)
wall_coords = []
for i in range(numwalls):
    temp = input()
    temp = list(temp.split(" "))
    temp = list(map(int, temp))
    #print (temp)
    wall_coords.append(temp)
start_state = input()
#print (start_state)
unit_step_reward = float(input())
#print (unit_step_reward)
Utility = []
Temp_Utility = []
for i in range (rows):
    Utility.append([0]*cols)
Temp_Utility = deepcopy(Utility)
discount_factor = .99
error_factor = .01
term_value = error_factor*(1-discount_factor)/discount_factor
print(term_value)
def check_possible(x,y):
    if(x < 0 or y < 0 or x > rows - 1 or y > cols -1):
        return False
    temp = [x,y]
    for cord in wall_coords:
        if temp == cord:
            #print("wall")
            #print(temp)
            return False
    return True
def best_action_select(x,y):
    global Utility
    best_val = -10000
    if(check_possible(x+1,y)):
        temp_val = .8*Utility[x+1][y]
        if(check_possible(x,y-1)):
            temp_val += .1*Utility[x][y-1]
        else:
            temp_val += .1*Utility[x][y]
        if(check_possible(x,y+1)):
            temp_val += .1*Utility[x][y+1]
        else:
            temp_val += .1*Utility[x][y]
        #temp_val += unit_step_reward
        best_val = max(best_val,temp_val)
    if(check_possible(x-1,y)):
        temp_val = .8*Utility[x-1][y]
        if(check_possible(x,y-1)):
            temp_val += .1*Utility[x][y-1]
        else:
            temp_val += .1*Utility[x][y]
        if(check_possible(x,y+1)):
            temp_val += .1*Utility[x][y+1]
        else:
            temp_val += .1*Utility[x][y]
        #temp_val += unit_step_reward
        best_val = max(best_val,temp_val)
    if(check_possible(x,y+1)):
        temp_val = .8*Utility[x][y+1]
        if(check_possible(x+1,y)):
            temp_val += .1*Utility[x+1][y]
        else:
            temp_val += .1*Utility[x][y]
        if(check_possible(x-1,y)):
            temp_val += .1*Utility[x-1][y]
        else:
            temp_val += .1*Utility[x][y]
        #temp_val += unit_step_reward
        best_val  = max(best_val,temp_val)
    if(check_possible(x,y-1)):
        temp_val = .8*Utility[x][y-1]
        if(check_possible(x+1,y)):
            temp_val += .1*Utility[x+1][y]
        else:
            temp_val += .1*Utility[x][y]
        if(check_possible(x-1,y)):
            temp_val += .1*Utility[x-1][y]
        else:
            temp_val += .1*Utility[x][y]
        #temp_val += unit_step_reward
        best_val  = max(best_val,temp_val)
    return best_val
def check_end(x,y):
    temp = [x,y]
    for var in end_coords:
        if(var == temp):
            return True
    return False
def init_utility():
    global Utility
    global Temp_Utility
    global state_values
    for i in range(rows):
        for j in range(cols):
            if(check_end(i,j)==True):
                Utility[i][j] = state_values[i][j]
    Temp_Utility = deepcopy(Utility)
    for i in range(rows):
        for j in range(cols):
            if(check_possible(i,j) == False or check_end(i,j) == True):
                continue
            else:
                state_values[i][j] = unit_step_reward

def value_iteration():
    iter = 0
    while(True):
        iter+=1
        print(iter)
        global Utility
        global Temp_Utility
        global state_values
        Utility = deepcopy(Temp_Utility)
        delta = -100
        for i in range (rows):
            for j in range(cols):
                if(check_possible(i,j) == False or check_end(i,j) == True):
                    continue
                res = best_action_select(i,j)
                #print("res",res)
                Temp_Utility[i][j] = state_values[i][j] + discount_factor*res
                #print(Utility)
                #print(Temp_Utility)
                delta = max(delta,abs(Temp_Utility[i][j]-Utility[i][j]))
        for i in range(rows):
            temp_list = [round(var,3) for var in Temp_Utility[i]]
            str1 = ' '.join(str(e) for e in temp_list)
            print(str1)
        print()
        print("delta",delta)
        #if(Temp_Utility == Utility):
        #    break
        if(delta <= term_value):
            break
init_utility()
value_iteration()
