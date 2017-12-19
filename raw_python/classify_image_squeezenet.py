# Import Turi Create package
import turicreate as turi

# Refrence the dataset path
url = "/Users/ahmedbekhit/Documents/Data/Development/TuriCreate/repo/turicreate-notebook/notebooks/data/food_images"

# Label the dataset
## Load the dataset folder image content using the image_analysis property
data = turi.image_analysis.load_images(url)
## Create a "foodType" key for each image in the dataset to specify whether it's an Egg or Soup, based on which folder it's located in.
data["foodType"] = data["path"].apply(lambda path: "Eggs" if "eggs" in path else "Soup")
## Export the labeled images as an SFrame object in order to use it while creating our image classifier.
data.save("egg_or_soup.sframe")
## Visualize the new labeled images list.
data.explore()

# Load the SFrame object that contains the labeled images.
dataBuffer = turi.SFrame("egg_or_soup.sframe")

# Randmly split the SFrame object
'''
    90% of the data from the original SFrame object will be used to train the image classifier.
    10% of the data from the original SFrame object will be used to test the image classifier.
'''
trainingBuffers, testingBuffers = dataBuffer.random_split(0.9)

# Train the image classifier using the SqueezeNet architecture and pre-trained model.
model = turi.image_classifier.create(trainingBuffers, target="foodType", model="squeezenet_v1.1")

# Evaluate the test data to determine the model accuracy
evaluations = model.evaluate(testingBuffers)

# Save the Turi Create model to retrieve it later
model.save("egg_or_soup.model")

# Export our new trained image classification model for Core ML.
model.export_coreml("FoodClassifier.mlmodel")
