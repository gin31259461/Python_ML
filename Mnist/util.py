from matplotlib import pyplot

def plot_mnist_image(image: Type[np.ndarray], labels: Type[np.ndarray]):
    for i in range(9):
        image_pixels = image[i].reshape(28, 28)
        axis = pyplot.subplot(3, 3, i + 1)
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)
        axis.set_title(labels[i])
        pyplot.gray()
        pyplot.imshow(image_pixels)
    pyplot.show()