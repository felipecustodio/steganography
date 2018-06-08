import numpy as np
import imageio
from matplotlib import pyplot as plt
from matplotlib import animation

original = np.asarray(imageio.imread("rogerinho.png", as_gray=False, pilmode="RGB"))
secret = np.asarray(imageio.imread("renan.png", as_gray=False, pilmode="RGB"))

merged = np.copy(original)

# merge images

# animation
# counter = 0
# frames = 0
# plt.axis('off')
# plt.imshow(merged, interpolation='none')
# plt.savefig("frames/merge/" + str(frames) + ".png")

print("Merging images...")
for i in range(original.shape[0]):
    for j in range(original.shape[1]):
        # get binary representation of pixel (original)
        # we're only interested in RGB
        r, g, b = original[i][j]
        rgb1 = ('{0:08b}'.format(r), '{0:08b}'.format(g), '{0:08b}'.format(b))
        # get binary representation of pixel (secret)
        r, g, b = secret[i][j]
        rgb2 = ('{0:08b}'.format(r), '{0:08b}'.format(g), '{0:08b}'.format(b))
        # now, we merge them
        # rg1 and rgb2 are string tuples, let's break them
        r1, g1, b1 = rgb1
        r2, g2, b2 = rgb2
        # now we can add the most significant bits of each one
        rgb = (r1[:4] + r2[:4], g1[:4] + g2[:4], b1[:4] + b2[:4])
        # we now have the new pixel for the output image (binary)
        # let's convert it back to int tuple (R,G,B)
        r, g, b = rgb
        merged[i][j] = [int(r, 2), int(g, 2), int(b, 2)]

    # animation
    # counter += 1
    # if (counter >= 10):
    #     frames += 1
    #     plt.axis('off')
    #     plt.imshow(merged, interpolation='none')
    #     plt.savefig("frames/merge/" + str(frames) + ".png")
    #     counter = 0

# unmerge images
unmerged = np.copy(merged)

# animation
# counter = 0
# frames = 0
# plt.axis('off')
# plt.imshow(unmerged, interpolation='none')
# plt.savefig("frames/unmerge/" + str(frames) + ".png")

print("Unmerging images...")
for i in range(merged.shape[0]):
    for j in range(merged.shape[1]):
        # get RGB
        r, g, b = merged[i][j]
        r, g, b = ('{0:08b}'.format(r), '{0:08b}'.format(g), '{0:08b}'.format(b))
        # extract last 4 bits (assuming we know it's 4 bits)
        # concatenate remaining bits as 0
        rgb = (r[4:] + "0000", g[4:] + "0000", b[4:] + "0000")
        # convert it back to int
        r, g, b = rgb
        unmerged[i][j] = [int(r, 2), int(g, 2), int(b, 2)]

    # animation
    # counter += 1
    # if (counter >= 10):
    #     frames += 1
    #     plt.axis('off')
    #     plt.imshow(unmerged, interpolation='none')
    #     plt.savefig("frames/unmerge/" + str(frames) + ".png")
    #     counter = 0


# plot images
# print("Plotting final results...")
# dpi = 80.0
# margin = 0.05
# xpixels, ypixels = original.shape[0], original.shape[1]
#
# figsize = (1 + margin) * ypixels / dpi, (1 + margin) * xpixels / dpi
# fig = plt.figure(figsize=figsize, dpi=dpi)
# ax = fig.add_axes([margin, margin, 1 - 2*margin, 1 - 2*margin])
#
# plt.axis('off')
# ax.imshow(merged, interpolation='none')
# plt.savefig("plots/demo_merged.png", dpi=100)
#
# plt.axis('off')
# ax.imshow(unmerged, interpolation='none')
# plt.savefig("plots/demo_unmerged.png", dpi=100)

print("Calculating RMSE...")

error = ((merged - original) ** 2)
error = np.sum(error)
error *= 1 / (merged.shape[0] * merged.shape[1])
error = np.sqrt(error)
print("Merged vs Original: {0:.4f}".format(error))

error = ((unmerged - secret) ** 2)
error = np.sum(error)
error *= 1 / (unmerged.shape[0] * unmerged.shape[1])
error = np.sqrt(error)
print("Extracted vs Secret: {0:.4f}".format(error))

print("Finished")
