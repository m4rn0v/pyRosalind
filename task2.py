from cmd import *
from libs.utils import from_file
from libs.utils import to_file

to_file(complement(dna(from_file("datasets/2"))), "outputs/2")