# loses a units of charge every unit of time the phone is on
# turning off the phone loses b units of charge

# turning off the phonen is instantaneous

t = int(input())
testcases = []
timestosend = []

for i in range(t):
    testcases.append(list(map(int, input().split())))
    timestosend.append(list(map(int, input().split())))

# so i think you should turn the phone off when the battery wasted during off time is more than the cost of turning it on and off. 

for i in range(t):
    num_messages = testcases[i][0]
    init_charge = testcases[i][1]
    charge_per_time = testcases[i][2]
    turn_off_consumption = testcases[i][3]

    used = 0
    current_time = 0
    flag = 0

    for k in range(num_messages):
        
        time = timestosend[i][k]
        used += min((time - current_time) * charge_per_time, turn_off_consumption)
        
        current_time = time
        if used >= init_charge: 
            print("NO")
            break
        flag +=1
        
    if flag != num_messages: 
        continue
    print("YES")
        



