import fasa_helper
import dta_helper
import operator
import output

def calculate_error_margin(mass):
    MOE = .05

    margin =  MOE

    lower = mass - margin
    upper = mass + margin

    return {'l':lower,'u':upper}

def match(mass, proteins):
    matches = []

    for protein in proteins:
        b_ions = protein[1][0]
        y_ions = protein[1][1]
        
        for x in range(len(b_ions)):
            margin = calculate_error_margin(b_ions[x])
            if margin['l'] <= mass <= margin['u']:
                matches.append([protein[0], 'b' + str(x+1)])
        for x in range(len(y_ions)):
            margin = calculate_error_margin(y_ions[x])
            if margin['l'] <= mass <= margin['u']:
                matches.append([protein[0], 'y' + str(x+1)])

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

inspect_dta('yr_inclusion.3076.3547.1.dta')
