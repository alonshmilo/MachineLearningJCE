from PIL import Image
import glob
import numpy as np

image_list = map (Image.open, glob.glob("c:/*ok*.png"))
ok_image = np.zero(len(image_list), image_list[0].size[0]*image_list[0].size[1])
for (idx, im) in enumerate(image_list):
    ok_image[idx,:] = np.array(im,np.uint8).reshape(1,im.size[0]*im.size[1])


image_list = map (Image.open, glob.glob("c:/*cyst*.png"))
cyst_image = np.zero(len(image_list), image_list[0].size[0]*image_list[0].size[1])
for (idx, im) in enumerate(image_list):
    cyst_image[idx,:] = np.array(im,np.uint8).reshape(1,im.size[0]*im.size[1])

#now 2 matrices:
all_image = np.concatenation((ok_image,cyst_image))

#now tagging what is ok and what is not
image_class = np.concatenation((np.zeros(ok_image.shape[0],1),np.ones(cyst_image.shape[0],1)))

#now taking the tests: 20%, 10% from each "list"
from sklearn.cross_validation import train_test_split

x_train, x_test, y_train, y_test = train_test_split(all_image, image_class, test_size=0.2)

#now we throw it to the "checker"


classifier = NearestNeighbor(); #new "object"
classifier.train(x_train,y_train) #we are training it with method "train"
y_pred=classifier.predict(x_test) # and we test the rest, using "predict"

num_of_correct = np.sum(y_pred==y_test)
accuracy = num_of_correct/len(y_test)

#accuracy depends on the input: how the input was divided.