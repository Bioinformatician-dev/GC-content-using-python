#Finding G and C content
for a single fasta file

# reading the input  fasta file
fr = open('GC_input.fasta', 'r')

seq = ""  # this will store the entire fasta as a single string

# looping over each line in our fasta file
for line in fr:
    if ">" in line:  # check if it a header line
        continue
    else:
        line = line.rstrip("\n")
        seq = seq + line

# closing the input file
fr.close()

total_len = len(seq)  # this will store total number of bases in the sequence
print('Content of C: ', round((seq.count("C") / total_len) * 100, 2), '%')  # finding and printing % of C
print('Content of G: ', round((seq.count("G") / total_len) * 100, 2), '%')  # finding and printing % of G
