from PIL import Image

image = Image.open("lenna.jpg")

lenna_rgb = image.convert("RGB")
lenna_red, lenna_green, lenna_blue = lenna_rgb.split()

image_shift_horizontal = 50
coordinates_red_left = (image_shift_horizontal, 0, lenna_red.width, lenna_red.height)
lenna_red_left = lenna_red.crop(coordinates_red_left)
coordinates_red_middle = (image_shift_horizontal // 2, 0, lenna_red.width - image_shift_horizontal // 2, lenna_red.height)
lenna_red_middle = lenna_red.crop(coordinates_red_middle)
lenna_red_blend = Image.blend(lenna_red_left, lenna_red_middle, 0.5)

coordinates_blue_right = (0, 0, lenna_blue.width - image_shift_horizontal, lenna_blue.height)
lenna_blue_right = lenna_blue.crop(coordinates_blue_right)
coordinates_blue_middle = (image_shift_horizontal // 2, 0, lenna_red.width - image_shift_horizontal // 2, lenna_red.height)
lenna_blue_middle = lenna_blue.crop(coordinates_blue_middle)
lenna_blue_blend = Image.blend(lenna_blue_right, lenna_blue_middle, 0.5)

lenna_green_crop = lenna_green.crop((image_shift_horizontal // 2, 0, lenna_green.width - image_shift_horizontal // 2, lenna_green.height))

lenna_shifted = Image.merge("RGB", (lenna_red_blend, lenna_green_crop, lenna_blue_blend)).save('lenna_shifted.jpg')

lenna_shifted_thumb = Image.open("lenna_shifted.jpg")
lenna_shifted_thumb.thumbnail((80, 80))
lenna_shifted_thumb.save('lenna_shifted_thumb.jpg')
