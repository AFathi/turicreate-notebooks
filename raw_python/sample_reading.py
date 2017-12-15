# Import Turi Create package
import turicreate as turi
# Reads the data file, in this case we will read data from a CSV file
dataBuffer = turi.SFrame.read_csv('src/notebooks/data/SampleCSVFile_119kb.csv')
# Parses out the first 5 rows (counting begins from 0 to 4)
dataBuffer.head(4)
