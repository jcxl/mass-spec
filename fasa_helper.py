def read_proteins(file):
    """
    Read all protiens and return a list in the format [name,sequence]
    
    Arguments:
    - `file`: The file name.
    """

    input = open(file)

    output = []

    #Dummy data. Allows the structure of the loop
    #to be somewhat simpler.
    sequence = []
    name = 'dummy'
    
    for line in input:
        
        if line[0] == '>':
            output.append([name, sequence])
            sequence = []
            name = line[1:].split()[0]  #Only the first 'word' is the name.
            
        else:
            fragment = line.replace('\n','')
            sequence.extend(fragment)
            
    output.append([name,sequence])
    output.pop(0) #Get rid of the dummy data.

    return output

def mass(acid):
    AMINO_ACID_MASSES = [['A',71.037] ,['C',103.009],['D',115.027],
                         ['E',129.043],['F',147.068],['G',57.021],
                         ['H',137.059],['I',113.084],['K',128.095],
                         ['L',113.084],['M',131.040],['N',114.043],
                         ['P',97.053] ,['Q',128.059],['R',156.101],
                         ['S',87.032] ,['T',101.048],['V',99.068],
                         ['W',186.079],['Y',163.063]]

    for entry in AMINO_ACID_MASSES:
        if acid == entry[0]:
            acid_mass = entry[1]
            return acid_mass

    return 0 #This should never happen.

def compute_b_ions(protein):
    k = len(protein) - 1

    ion_list = []

    sum = 1.0078 #This number is added to the total mass for some reason.
    
    for index in range(k):
        sum +=  mass(protein[index])
        ion_list.append(sum)

    return ion_list

def compute_y_ions(protein):
    k = len(protein) - 1

    ion_list = []

    sum = 19.01838504 #This number is added to the total mass for some reason.
                      #It is also much bigger than the number added to the b
                      #ion mass. Weird.

    for index_mod in range(k):
        sum += mass(protein[k - index_mod])
        ion_list.append(sum)   #She's Hungarian.

    return ion_list

def compute_ions(protein):
    """Compute all possible b and y ion masses for a protein.
    
    Arguments:
    - `protein`: The list of amino acids in a protein.
    """

    b_ions = compute_b_ions(protein)
    y_ions = compute_y_ions(protein)

    return [b_ions, y_ions]


def read_fasa(filename):
    """Read the specified .fasa document, and output the masses of all possible ions of proteins.
    
    Arguments:
    - `filename`: the filename of the fasa document.
    """

    
    proteins = read_proteins(filename)

    prot_list = []
    
    for protein in proteins:
        name = protein[0]
        sequence = protein[1]

        ions = compute_ions(sequence)

        prot_list.append([name, ions])

    return prot_list
