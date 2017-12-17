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
