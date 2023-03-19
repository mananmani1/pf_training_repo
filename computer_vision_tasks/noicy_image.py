import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_noise():
    # Enter the path to the image file
    image_path = input("Enter the path to the image file: ")

    # Load the image
    image = cv2.imread(image_path)

    # Adding Gaussian type of  noise
    gauss_noise = np.random.normal(0, 50, image.shape)
    gauss_img = cv2.add(image, gauss_noise.astype(np.uint8))

    # # Adding Poisson type of noise
    # poisson_noise = np.random.poisson(50, image.shape)
    # poisson_img = cv2.add(image, poisson_noise.astype(np.uint8))

    # # Adding Uniform type of noise
    # uniform_noise = np.random.uniform(-50, 50, image.shape)
    # uniform_img = cv2.add(image, uniform_noise.astype(np.uint8))

    # Displaying the original and noisy images via plt
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

    axs[0, 0].imshow(image)
    axs[0, 0].set_title("Original Image")
    axs[0, 0].axis("off")

    axs[0, 1].imshow(gauss_img)
    axs[0, 1].set_title("Gaussian Noise")
    axs[0, 1].axis("off")

    # axs[1, 0].imshow(poisson_img)
    # axs[1, 0].set_title("Poisson Noise")
    # axs[1, 0].axis("off")

    # axs[1, 1].imshow(uniform_img)
    # axs[1, 1].set_title("Uniform Noise")
    # axs[1, 1].axis("off")

    plt.show()

add_noise()
