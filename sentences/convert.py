from PIL import Image
import matplotlib.pyplot as plt
import sys

dname = "../sent-graphs/"
fname = sys.argv[1]

img = Image.open(fname)
plt.imshow(img)
plt.savefig(dname + fname)


