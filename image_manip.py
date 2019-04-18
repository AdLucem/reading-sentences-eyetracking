from PIL import Image, ImageOps
import numpy as np


def stack_graphs(names, merged):
	"""Put all the graphs together in a single picture
	for ease of study"""

	imgs = [Image.open(name) for name in names]
	img_merge = np.vstack((np.asarray(i) for i in imgs))
	img_merge = Image.fromarray(img_merge)
	img_merge.save(merged)

def overlay(name, slidenum):

	bg = "sent-graphs/" + str(slidenum) + ".png"
	bg = Image.open(bg)
	fg = Image.open(name)

	w, h = fg.size
	w_, h_ = bg.size
	print(w, h)
	print(w_, h_)


	#fg.putalpha(128)
	#bg.paste(fg, (0, 0), fg)
	#bg.show()

def put_image(p, n):

	slide = "sentences/" + str(n) + ".png"
	img = Image.open(slide)
	img = ImageOps.flip(img)
	p.imshow(img)	