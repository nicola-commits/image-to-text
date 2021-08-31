from PIL import Image, ImageChops, UnidentifiedImageError
import sys
gradient = "10"
inputPath = input('THE INPUT PATH PLEASE>>>>')
outputPath = input('THE OUTPUT PATH(CREATE A .txt FILE PLS)>>>')
aaaa = input('Invert?>>>')
ratio = int(input('Ratio>>>'))
invert = False
if aaaa == 'Yes':
    invert = True
image = Image.open(inputPath)
outputFile = open(outputPath, "w")
if invert:
    gradient = gradient[::-1]
image = image.convert("L")
output = ""
width, height = image.size
for y in range(0, height, ratio):
    for x in range(0, width, ratio):
        colour = image.getpixel((x, y))
        output += gradient[round((colour / 255) * (len(gradient) - 1))] + " "
    output += "\n"
outputFile.write(output)
image.close()
outputFile.close()
print(output)
print('Process completed!')