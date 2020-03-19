
from Bio import SeqIO
import numpy as np
from PIL import Image
import math

filename = 'sequence.fasta'
records = []
colors = {'A' : [41, 41, 106],
          'G' : [171, 85, 161],
          'T' : [94, 202, 233],
          'C' : [111, 87, 164],
          'U' : [94, 202, 233]
    
}   # a nice blue color scheme


for record in SeqIO.parse(file_name, "fasta"):
    records.append(record) # get records from fasta file
if records:
    sequence = records[0].seq
    length = len(sequence)
    dim = math.ceil(math.sqrt(length))  # dimensions of our image is the sqrt of seq length

    data = np.zeros((dim, dim, 3), dtype=np.uint8 ) # initialize array of  zeroes
    for i, base in enumerate(sequence):
         data[int(i/dim)][i%dim] = colors[base]
    image = Image.fromarray(data)   #create the image
    image.show()





