from find_and_rename import *
from splign import *
from mask_1 import *
from mask_2 import *
from add_genome import *
from add_annotation import *
import sys

find_and_rename(sys.argv[2], sys.argv[4])

mask_1(sys.argv[1])

add_annotation(sys.argv[5], sys.argv[7])

splign(sys.argv[3])

mask_2(sys.argv[1])

add_genome(sys.argv[4], sys.argv[6])


print('Successfully updated all input sequences!')
