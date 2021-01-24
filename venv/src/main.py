import cv2

FILE_PATH = input("Type file path: ")
RESIZE_LEN = list(map(int, input("Type resize length. ex) x y  \nIf you won't resize image type 0 0 \n").split(' ')))
pos_list = []


def load_image(file_path, resize=None):
    """
    :param file_path: image file path
    :param resize: Tuple
    :return: image or resized image
    """

    image = cv2.imread(file_path)
    if resize and resize != [0, 0]:
        resized = cv2.resize(image, (resize[0], resize[1]), interpolation=cv2.INTER_AREA)
        return resized
    else:
        return image


def get_rgb(img, position):
    b, g, r = img[position[1], position[0]]  # y, x tuple
    print(r, g, b)
    # return r, g, b


def on_mouse(event, x, y, flags, param):
    global pos_list, IMG
    if event == cv2.EVENT_LBUTTONDOWN:
        pos_list.clear()
        pos_list.append((x, y))
        print("position:", x, y)
        b, g, r = IMG[y, x]
        print('R, G, B:', r, g, b)


IMG = load_image(FILE_PATH, resize=RESIZE_LEN)


def main():
    global pos_list
    print("press any key to quit")
    cv2.imshow("get_color", IMG)
    cv2.setMouseCallback('get_color', on_mouse)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
