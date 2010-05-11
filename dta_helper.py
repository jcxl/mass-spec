def read_dta(filename):
    input = open(filename)

    input_list = []
    
    for line in input:
        element = line.split()
        element[0] = float(element[0])
        element[1] = float(element[1])
        
        input_list.append(element)

    input_list.pop(0) #Pop precursor mass.

    sum_of_intensity = 0

    for element in input_list:
        sum_of_intensity += element[1]

    for x in range(len(input_list)):
        relative_intensity = input_list[x][1] / sum_of_intensity
        input_list[x].append(relative_intensity)
        
    return input_list
