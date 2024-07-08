import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as img 
import imageio

def load_image(FILENAME = 'Input_pic.PNG'):
    
      # loading the png image as a 3d numpy array
      image = imageio.imread(FILENAME)

      # #print this image shape
      # print(image.shape)

      # # display the image
      # plt.imshow(image)
      # plt.show()

      #Scale the pixel values to be between 0 and 1
      image = image/255.0

      # return the image array
      return image


def initialize_centroids(image, clusters):
      #Flatten the image to a 2D array
      pixels = np.reshape(image, (image.shape[0]*image.shape[1], image.shape[2]))
      num_pixels = pixels.shape[0]
      num_channels = pixels.shape[1]

      #Initialize the centroids array randomly from the pixels array
      centroids = np.zeros((clusters, num_channels))


      for i in range(clusters):
            random_idx = np.random.choice(num_pixels)
            centroids[i] = pixels[random_idx]
            
      return pixels, centroids
    

def euclidean_distance(p1, p2):
      return np.sqrt(np.sum((p1 - p2)**2))



def k_means_clustering(pixels, centroids, clusters, num_iterations = 10):
      num_pixels = pixels.shape[0]
      num_channels = pixels.shape[1]

      #Initialize the cluster assignments and the loss
      cluster_assignments = np.zeros(num_pixels)
      # loss = 0

      for _ in range(num_iterations):
            #Assign each pixel to the closest centroid
            for i in range(num_pixels):
                  min_distance = float('inf')
                  closest_cluster = 0

                  for j in range(clusters):
                        distance = euclidean_distance(pixels[i], centroids[j])

                        if distance < min_distance:
                              min_distance = distance
                              closest_cluster = j

                  cluster_assignments[i] = closest_cluster
                  # loss += min_distance

            #Update the centroids
            for j in range(clusters):
                  cluster_pixels = pixels[cluster_assignments == j]
                  centroids[j] = np.mean(cluster_pixels, axis = 0)

      return centroids, cluster_assignments #, loss

def save_compressed_image(centroids, assignments, original_image, clusters):
      # Map each pixel to its corresponding centroid
      compressed_pixels = centroids[assignments.astype(int)]
      compressed_image = np.reshape(compressed_pixels, original_image.shape)

      # Display the compressed image
      plt.imshow(compressed_image)
      plt.show()

      # Save the compressed image
      imageio.imwrite('compressed_image_' + str(clusters) + '.png', compressed_image)



if __name__ == '__main__':
      image = load_image()

      clusters = 16 # k - value
      clusters = int(input('Enter the number of colors in the compressed image. Default is 16.\n'))


      pixels, centroids = initialize_centroids(image, clusters)
      centroids, assignments = k_means_clustering(pixels, centroids, clusters)
      save_compressed_image(centroids, assignments, image, clusters)
    
    
