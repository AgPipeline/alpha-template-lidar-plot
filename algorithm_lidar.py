"""Plot-level Lidar algorithm
"""

# Importing modules. Please add any additional import statements below
import numpy as np

# Definitions
# Please replace these definition's values with the correct ones
VERSION = '1.0'

# Information on the creator of this algorithm
ALGORITHM_AUTHOR = ''
ALGORITHM_AUTHOR_EMAIL = ''

ALGORITHM_NAME = ''
ALGORITHM_DESCRIPTION = 'This algorithm calculates something useful from lidar data'

# Citation information for publication (more information in HOW_TO.md)
CITATION_AUTHOR = ''
CITATION_TITLE = ''
CITATION_YEAR = ''

# The name of one or more variables returned by the algorithm, separated by commas (more information in HOW_TO.md)
# If only one name is specified, no comma's are used.
# Note that variable names cannot have comma's in them: use a different separator instead. Also,
# all white space is kept intact; don't add any extra whitespace since it may cause name comparisons
# to fail.
VARIABLE_NAMES = ''

# Optional override for the generation of a BETYdb compatible csv file
# Set to False to suppress the creation of a compatible file
WRITE_BETYDB_CSV = True

# Optional override for the generation of a TERRA REF Geostreams compatible csv file
# Set to False to suppress the creation of a compatible file
WRITE_GEOSTREAMS_CSV = True


# Entry point for plot-level lidar algorithm
def calculate(pxarray: np.ndarray):
    """Calculates one or more values from plot-level Lidar data
    Arguments:
        pxarray: Array of Lidar data for a single plot
    Return:
        Returns one or more calculated values
    """
    # ALGORITHM: fill in the following lines with your algorithm
    

    # RETURN: replace the following return with your calculated values. Be sure to order them as defined in VARIABLE_NAMES above
    return 
