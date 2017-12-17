# Import Turi Create package
import turicreate as turi

# Create an SFrame object.
'''
    Each column in the `SFrame` is an `SArray` object.
    
    In the following `SFrame` object, we have created a data buffer (dataset) that specifies the size of each pet's eyes, nose, and head.
    
    Each number in the dataset is a ratio from 15cm.
    
    Note:- The ratios in the dataset are NOT accurate or related to reality. Those are random ratios used for demonstration purposes.
'''
dataBuffer = turi.SFrame({
                         "pet_types": ["cat", "dog", "wolf", "cat", "wolf", "dog"],
                         "eyes":      [0.23,  0.64,  0.89,   0.26,  0.93,   0.66 ],
                         "nose":      [0.11,  0.68,  0.78,   0.08,  0.74,   0.57 ],
                         "head":      [0.34,  0.47,  0.66,   0.37,  0.68,   0.45 ]
                         })

# Create a nearest neighbor classifier using the SFrame object above.
classifier = turi.nearest_neighbor_classifier.create(dataBuffer, target="pet_types")

# Edit the input below. Make sure the numbers are between 0 and 1.
userinput = turi.SFrame({
                        "eyes":      [0.32],
                        "nose":      [0.20],
                        "head":      [0.42]
                        })

# Predict the input using the nearest neighbor classifier.
result = classifier.predict(userinput, max_neighbors=2)
print result
