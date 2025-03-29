import os 
# 

files = os.listdir('image')
i = 1

for file in files:
    if file.endswith('.png'):
        os.rename(f"image/{file}", f"image/{i}.png")
        i = i + 1


print('Files renamed successfully')