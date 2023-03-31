from PIL import Image

'''mac =Image.open("C:\\Users\\prinfnu\\Documents\\Python Scripts\\Images\\prince.png")
print(type(mac))
print(mac)
print("size of image: ",mac.size)
print("filename of image: ",mac.filename)
print("format discription of image: ",mac.format_description)'''

# there are two images we will be working with:
# word_matrix.png and  mask.png
# The word_matrix is a png image,it contains a spreadsheet of words with a hidden message in it
# Your task is to use the mask.png image to reveal the hidden message inside the word_matrix.png. 
# Keep in mind, you may need to resize the mask.png in order for this to work.

words=Image.open("C:\\Users\\prinfnu\\Documents\\Python Scripts\\Images\\word_matrix.png")
mask=Image.open("C:\\Users\\prinfnu\\Documents\\Python Scripts\\Images\\mask.png")

print("size of image words matrix: ",words.size)
print("size of image mask: ",mask.size)

mask=mask.resize((1015,559))

print("size of image mask after resizing: ",mask.size)

mask.putalpha(200)

words.paste(mask,(0,0),mask)

words.save("C:\\Users\\prinfnu\\Documents\\Python Scripts\\Images\\word_unmasked.png")