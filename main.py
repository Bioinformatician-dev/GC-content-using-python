#Finding G and C content for a single fasta file

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

# Finding G and C content for a multi fasta file

# reading the input multi fasta file
fr=open('multi_GC_input.fasta','r')

seq = "" # this will store the sequence of each fasta 

for line in fr: # looping over each line in our fasta file
    if ">" in line: # check if it is a header line
        if seq != "": # check if the seq variable is an empty string or not
            length = len(seq) # this will store the length of a fasta sequence
            print('Content of C: ', round((seq.count("C")/length)*100,2),'%') # finding and printing % of C
            print('Content of G: ', round((seq.count("G")/length)*100,2),'%') # finding and printing % of G
            print("")
            seq = "" # again making seq as empty string to store the sequence of the next fasta sequence
        print(line, end="") # this line prints the header
            
    else: # if it is not a header line
        line = line.rstrip("\n") # remove '\n' from the end of the line
        seq = seq+line # concatenate it to seq
        
# closing the input file
fr.close()
length = len(seq) # this will store the length of last fasta sequence
print('Content of C: ', round((seq.count("C")/length)*100,2),'%') # finding and printing % of C
print('Content of G: ', round((seq.count("G")/length)*100,2),'%') # finding and printing % of G
