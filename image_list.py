import cv2
import memory_profiler as mem_profile
import os
from linked_list import linked_list

my_list = linked_list()

files = os.listdir('./images')

for image in files:
    data = (image, cv2.imread('./images/'+image))
    my_list.append(data)

image = 2

data = my_list.get_image(image)
print(data[0])

images = my_list.display_image()
print(images)

my_list.erase_image(image)
images = my_list.display_image()
print(images)


print('Linked list length: ',my_list.length())
print('Memory Usage: ',mem_profile.memory_usage()[0])
