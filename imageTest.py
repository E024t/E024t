import numpy as np
import imageio.v2 as iio
import json

def changeImageHistogram():
    # image = (iio.imread("./lion.jpeg")).astype('float')
    # print(image.shape)
    with open('json_files/UserImage.json') as f:
        imageData = json.load(f)

    # print(imageData['data'])
    imageData_data = imageData['data']
    image = np.zeros([imageData['height'],imageData['width'],3]).astype('float')

    for i in range(imageData['height']):
        for j in range(imageData['width']):    
            image[i,j,0]= imageData_data[4*(j+(imageData['width'])*i)+0]
            image[i,j,1]= imageData_data[4*(j+(imageData['width'])*i)+1]
            image[i,j,2]= imageData_data[4*(j+(imageData['width'])*i)+2]
            # print(4*((i+1)*(j+1)-1))
            # print((i+(imageData['width'])*(j)))
            


    # print(image.shape)   
    # print(imageData_data[0])   

    image = image.astype('float')

    image = (255/(1+(60/(image+1))**4)).astype('uint8')
    # image = image .astype('uint8')

    # print(image.shape) 
    # print(imageData_data.shape)
    # image_jason = {"0":image[:,:,0],
    #                 "1":image[:,:,1],
    #                 "2":image[:,:,2]}

    iio.imsave("./static/after.png",image)
    image_to_data =[]
    for i in range(imageData['height']):
        for j in range(imageData['width']):
            # image_to_data.append(np.ndarray.tolist(image[i,j,0]) )
            image_to_data.append(int(image[i,j,0]) )
            image_to_data.append(int(image[i,j,1]) )
            image_to_data.append(int(image[i,j,2]) )
            image_to_data.append(255) 

    imageData['data'] = image_to_data

    filename = f'json_files/UserImageAfter.json'

    with open(filename, 'w') as file:
        # file.write(jsonify(data))
        file.write(json.dumps(imageData, separators=(',', ':')))
        