import base64
image = open(".jpeg")
mistery_img2 = mistery_img2()
image_64_encode = base64.encodestring(mistery_img2)
image_64_decode = base64.decodestring(image_64_encode) 
image_result = open('deer_decode.gif', 'wb') # create a writable image and write the decoding result
image_result.write(image_64_decode)
