# Name: ...
# CSE 140
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of nucleotides seen so far.
gc_count = 0
at_count = 0

g_count = 0
c_count = 0
a_count = 0
t_count = 0

other_count = 0       # Used for error checking in Problem #6


# for each base pair in the string,
for bp in seq:

    # next, if the bp is a G or a C,
    if bp == 'C':
        c_count = c_count + 1
        gc_count = gc_count + 1

    elif bp == 'G':
        g_count = g_count + 1
        gc_count = gc_count + 1

    elif bp == 'A':
        a_count = a_count + 1
        at_count = at_count + 1

    elif bp == 'T':
        t_count = t_count + 1
        at_count = at_count + 1

    else:
        # print(bp)     Used in error checking for problem #6
        other_count = other_count + 1

    # Set the total count to just the bps that are g, c, a or t
    total_count = g_count + c_count + a_count + t_count

# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count
at_content = float(at_count) / total_count
at_gc_ratio = float(at_count) / gc_count

# Print the answer
print()
print('***' + filename + '***')
print('GC-content:', gc_content)
print('AT-content:', at_content)
print('AT/GC ratio:', at_gc_ratio)
print()
print('G-count:', g_count)
print('C-count:', c_count)
print('A-count:', a_count)
print('T-count:', t_count)
# print('Other:', other_count)      Used to error check for problem #6
print()
print('---Data Checking---')
print('G + C + A + T\t', g_count + c_count + a_count + t_count)
print('Total Count\t', total_count)
print ('Sequence Length\t', len(seq))
