# Import Turi Create package
import turicreate as turi
# Reads the data file, in this case we will read data from a CSV file
'''
    Each column in the `SFrame` is an `SArray` object.
    
    In the following line of code, the parameter `header` is set to `False` because the **CSV** data file we're using doesn't have a header.
    
    Note:- The `header` parameter is `True` by default and if we didn't set it to `False` it would show us the first **n+1** rows since it counts the first as a header automatically.
'''
dataBuffer = turi.SFrame.read_csv('/Users/ahmedbekhit/Documents/Data/Development/TuriCreate/SampleCSVFile_119kb.csv', header=False)

# Load the first 5 rows.
dataBuffer.head(5)

print dataBuffer
