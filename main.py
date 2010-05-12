import fasa_helper
import dta_helper
import operator
import output
import math

def calculate_error_margin(mass):

    lower = mass - .05
    upper = mass + .05

    return {'l':lower,'u':upper}
    
def match(mass, proteins):
    matches = []

    for protein in proteins:
        b_ions = protein[1][0]
        y_ions = protein[1][1]
        
        for x in range(len(b_ions)):
            
            #margin = calculate_error_margin(b_ions[x])
            if math.fabs(b_ions[x] - mass) <= .05:
                matches.append([protein[0], 'b' + str(x+1)])
                break
            if mass < b_ions[x]:
                break
            
        for x in range(len(y_ions)):
            #margin = calculate_error_margin(y_ions[x])
            if math.fabs(y_ions[x] - mass) <= .05:
                matches.append([protein[0], 'y' + str(x+1)])
                break
            
            if mass < y_ions[x]:
                break

    return matches

def inspect_dta(results_filename):
    proteins = fasa_helper.read_fasa('Yersinia_enterocolitica_ribosome.fasta')
    results = dta_helper.read_dta('yr_inclusion/' + results_filename)

    peak_matches = []
    scores = []
    for result in results:

        mass = result[0]

        protein_matches = match(mass, proteins)
        peak_matches.append([mass, protein_matches])

        for prot_match in protein_matches:
            found = False
            for score in scores:
                if score[0] == prot_match[0]:
                    score[1] += result[2]
                    found = True
            if not found:
                scores.append([prot_match[0], result[2]])

    scores = sorted(scores, key=operator.itemgetter(1),reverse = True)

    output.output(results_filename,scores,peak_matches)
