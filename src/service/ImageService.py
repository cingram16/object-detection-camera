from PIL import Image
from matplotlib import pyplot as plt


class ImageService:

    @staticmethod
    def show_image(pil_img, prob, boxes, classes):
        COLORS = [[0.000, 0.447, 0.741], [0.850, 0.325, 0.098], [0.929, 0.694, 0.125],
                  [0.494, 0.184, 0.556], [0.466, 0.674, 0.188], [0.301, 0.745, 0.933]]

        plt.figure(figsize=(16, 10))
        plt.imshow(pil_img)
        ax = plt.gca()
        colors = COLORS * 100

        for p, (xmin, ymin, xmax, ymax), c in zip(prob, boxes.tolist(), colors):
            ax.add_patch(plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                                       fill=False, color=c, linewidth=3))
            cl = p.argmax()
            text = f'{classes[cl.item()]}: {p[cl]:0.2f}'
            ax.text(xmin, ymin, text, fontsize=15,
                    bbox=dict(facecolor='yellow', alpha=0.5))

        plt.axis('off')
        plt.savefig('./assets/result.jpg')
        image = Image.open(open(f'./assets/result.jpg', 'rb'))
        image.show()
