# Import Turi Create package
import turicreate as turi
# Reads the data file, in this case we will read data from a CSV file
dataBuffer = turi.SFrame.read_csv('/Users/ahmedbekhit/Documents/Data/Development/TuriCreate/SampleCSVFile_119kb.csv', header=False)
dataBuffer.head(5)
print dataBuffer
