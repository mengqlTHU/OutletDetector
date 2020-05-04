import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa
import cv2
import os


ia.seed(1)

seq = iaa.Sequential([
    iaa.Fliplr(0.5), # horizontal flips
    iaa.Crop(percent=(0, 0.2)), # random crops
    # Small gaussian blur with random sigma between 0 and 0.5.
    # But we only blur about 50% of all images.
    iaa.Sometimes(
        0.5,
        iaa.GaussianBlur(sigma=(0, 10))
    ),
    # Strengthen or weaken the contrast in each image.
    iaa.LinearContrast((0.8, 1.2)),
    # Add gaussian noise.
    # For 50% of all images, we sample the noise once per pixel.
    # For the other 50% of all images, we sample the noise per pixel AND
    # channel. This can change the color (not only brightness) of the
    # pixels.
    iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.4*255), per_channel=True),
    # Make some images brighter and some darker.
    # In 20% of all cases, we sample the multiplier once per channel,
    # which can end up changing the color of the images.
    iaa.Multiply((0.8, 1.2), per_channel=0.2),
    # Apply affine transformations to each image.
    # Scale/zoom them, translate/move them, rotate them and shear them.
    iaa.Affine(
        scale={"x": (0.98, 1.02), "y": (0.98, 1.02)},
        translate_percent={"x": (-0.02, 0.02), "y": (-0.02, 0.02)},
        rotate=(-5, 5),
        # shear=(-0.2, 0.2),
        mode="edge"
    )
], random_order=True) # apply augmenters in random order


aug_start = 100

im = cv2.imread(os.path.join("p", "1.jpg"))
for _ in range(400):
    images_aug = seq(image=im)            
    filename_jpg = f"{aug_start}.jpg"
    aug_start+=1
    cv2.imwrite(os.path.join("p", filename_jpg), images_aug)