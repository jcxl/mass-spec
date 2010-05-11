def output(filename,scores, matches):
    ofile = open('output_' + filename + '.txt', "w")

    ofile.writelines('{0:10} {1:40} {2:6}'.format('Rank', 'Name', 'Score'))
    ofile.writelines('\n' + '='.rjust(60,"="))

    for x in range(len(scores)):
        rank = x + 1
        name = scores[x][0]
        score = scores[x][1]

        ofile.writelines('\n{0} {1:40} {2:6}'.format(str(rank).ljust(10), name, score))

    ofile.writelines('\n\n')
    
    for x in range(len(matches)):
        ofile.writelines(str(matches[x][0]) + '\n')
        for y in range(len(matches[x][1])):
            ofile.writelines(str(matches[x][1][y]).rjust(50)+ '\n')
    
    
    ofile.close()

