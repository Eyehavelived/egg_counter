import numpy as np
import cv2
import os
from math import sqrt

def get_circle(gray, param1, param2, minRadius, maxRadius, minDist):
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((14,14),np.float32)/196
    dst = cv2.filter2D(gray,-1,kernel)
    blur = cv2.medianBlur(gray, 9, dst)

    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 5, minDist, param1, param2, minRadius, maxRadius)

    return np.uint16(np.around(circles))

def get_blobs(img, file_name, x, y, r, output_dir,
              marker_size, min_circularity, min_convex, min_inertia, min_area,
              is_preview, resize_dim=None):
    # Set our filtering parameters
    # Initialize parameter settiing using cv2.SimpleBlobDetector
    params = cv2.SimpleBlobDetector_Params()

    # Set Area filtering parameters
    params.filterByArea = True
    params.minArea = min_area

    # Set Circularity filtering parameters
    params.filterByCircularity = True
    params.minCircularity = min_circularity

    # Set Convexity filtering parameters
    params.filterByConvexity = True
    params.minConvexity = min_convex

    # Set inertia filtering parameters
    params.filterByInertia = True
    params.minInertiaRatio = min_inertia

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs
    keypoints = detector.detect(img)

    # remove blobs outside of the boundary
    counter = 0
    for kp in keypoints:
        kx, ky = kp.pt
        if not round(sqrt((kx-x)**2 + (ky-y)**2)) >= r:
            # draw red circles on blobs
            cv2.circle(img, (int(kx), int(ky)), marker_size, (0, 0, 255), 5)
            counter += 1

    # for some reason removing the unwanted keypoints doesn't work so counting it will have to do instead.
    text = f"Number of Eggs: {counter}"
    cv2.putText(img, text, (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 200), 6)

    if is_preview:
        assert resize_dim is not None
        cv2.namedWindow("preview")
        imgS = cv2.resize(img, resize_dim)
        cv2.imshow("preview", imgS)
    else:
        cv2.imwrite(f"{output_dir}/blobs_{file_name}", img)
    return counter


def blob_method(input_dir, output_dir, h_crop, w_crop, contrast, brightness, circ_param1, circ_param2, circ_min,
                circ_max, circ_dist, marker_size, min_circularity, min_convex, min_inertia, min_area,
                is_preview):

    if is_preview:
        file_list = [os.listdir(input_dir)[0]]
    else:
        file_list = os.listdir(input_dir)

    out = []

    for i in range(len(file_list)):
        file_name = file_list[i]
        img = cv2.imread(f'{input_dir}/{file_name}')

        # crop the image
        x = w_crop
        y = h_crop
        h = img.shape[0] - h_crop
        w = img.shape[1] - w_crop

        img = img[y:y + h, x:x + w]

        resize = (int(w/3), int(h/3))

        # Set to greyscale and the pump up contrast
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        output = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)

        # find the well or plate
        detected_well = get_circle(output, circ_param1, circ_param2, circ_min, circ_max, circ_dist)
        x, y, r = detected_well[0][0]

        # convert image back to BGR
        output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)
        cv2.circle(output, (x, y), r, (0, 0, 255), 5)

        # find the eggs using the blob method, save the modified image, and get the count of eggs
        eggCount = get_blobs(output, file_name, x, y, r, output_dir,
                             marker_size, min_circularity, min_convex, min_inertia, min_area,
                             is_preview, resize)
        if not is_preview:
            out.append(f"{file_name.split('.')[0]},{eggCount}")

    if not is_preview:
        with open(f"{output_dir}/count_results.csv", "w") as file:
            file.write("\n".join(out))

if __name__ == '__main__':
    # IO directories
    input_dir = 'input'
    output_dir = 'output'

    # crop amount
    h_crop = 0
    w_crop = 100

    # contrast adjustment
    contrast = 3
    brightness = -350

    # plate circle params
    circ_param1 = 50
    circ_param2 = 30
    circ_min = 450
    circ_max = 550
    circ_dist = 1000

    # blob params
    marker_size = 25
    min_circularity = 0.3
    min_convex = 0.4
    min_inertia = 0.05
    min_area = 500

    blob_method(input_dir, output_dir,h_crop, w_crop, contrast, brightness, circ_param1, circ_param2, circ_min, circ_max,
         circ_dist, marker_size, min_circularity, min_convex, min_inertia, min_area, True)
