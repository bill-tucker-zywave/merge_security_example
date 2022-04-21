import argparse
import sys
from PIL import Image
#
def get_pics():
    # homer
    x = requests.get('https://i.guim.co.uk/img/media/88f6b98714035656cb18fb282507b60e82edb0d7/0_57_2560_1536/master/2560.jpg?width=620&quality=45&auto=format&fit=max&dpr=2&s=ba524fc454d04b8306b1cd88e133d488')
    # pizza
    y = requests.get('https://media-cdn.tripadvisor.com/media/photo-p/1b/e1/01/d8/photo0jpg.jpg')
    return x,y


def main(alpha):
    """TODO: Docstring for main.
    :returns: TODO

    """
    print('howdy')
    img1 = Image.open('homer.jpg')
    img2 = Image.open('pizza.jpg').resize(img1.size)
    #
    Image.blend(img1, img2, alpha).save(
        "result/Image_blend_{}.jpg".format(alpha))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--alpha", default=.5, help="Alpha to use for merging images")
    args = parser.parse_args()
    main(float(args.alpha))
