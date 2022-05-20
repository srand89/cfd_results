from operator import concat

with open('Scenario 1.sum') as f:
    data = f.readlines()
    
    for line in data:
        if 'Temp  +' in line:
            max_temp = line
        if 'MdotIn x Cp x (TOut - TIn) =' in line:
            mdotcp = line
        if '(Numerical) Energy Out  -  Energy In' in line:
            eo_ei = line
        if 'Heat Transfer from Wall To Fluid' in line:
            htfwtf = line
        if 'Heat Transfer Due to Sources In Fluid' in line:
            htdtsif = line
        if 'Radiation heat balance' in line:
            rhb = line 
    
max_temp = max_temp.split()
max_temp = max_temp[3]
max_temp = float(max_temp)

mdotcp = mdotcp.split()
mdotcp = float(mdotcp[8])

eo_ei = eo_ei.split()
eo_ei = float(eo_ei[7])

htfwtf = htfwtf.split()
htfwtf = float(htfwtf[7])

htdtsif = htdtsif.split()
htdtsif = float(htdtsif[8])

rhb = rhb.split()
net_radiative_heat=rhb[4]
net_radiative_heat= net_radiative_heat.strip('/')

net_radiative_heat = float(net_radiative_heat)

#left_side = eo_ei + htfwtf + htdtsif
#error = (rhb - left_side)/left_side
#print(error) 

print(f.name)
print("Max Temp:",max_temp)
print("net radiative heat:", net_radiative_heat)

