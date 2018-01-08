import argparse
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import imutils
import cv2
from imutils import paths

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True, help="Path to model")
ap.add_argument("-i", "--images", required=True, help="Path to images")
args = vars(ap.parse_args())

# load the trained convolutional neural network
print("[INFO] loading network...")
model = load_model(args["model"])

for imagePath in sorted(list(paths.list_images(args["images"]))):
	print(imagePath)
	image = cv2.imread(imagePath)
	orig = image.copy()

	image = cv2.resize(image, (28, 28))
	image = np.array(image, dtype="float") / 255.0
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)

	(brocolli, weed) = model.predict(image)[0]

	# build the label
	label = "Weed" if weed > brocolli else "Brocolli"
	proba = weed if weed > brocolli else brocolli
	label = "{}: {:.2f}%".format(label, proba * 100)

	# draw the label on the image
	output = imutils.resize(orig, width=400)
	cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
		0.7, (0, 255, 0), 2)

	# show the output image
	cv2.imshow("Output", output)
	cv2.waitKey(0)
