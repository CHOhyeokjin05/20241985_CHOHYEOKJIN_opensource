import cv2
import os
import numpy as np

data = [[[[441.0, 174.0], [1166.0, 176.0], [1165.0, 222.0], [441.0, 221.0]], ('ACKNOWLEDGEMENTS', 0.9974855780601501)], 
        [[[403.0, 346.0], [1204.0, 348.0], [1204.0, 384.0], [402.0, 383.0]], ('We would like to thank all the designers and', 0.9683309197425842)], 
        [[[403.0, 396.0], [1204.0, 398.0], [1204.0, 434.0], [402.0, 433.0]], ('contributors who have been involved in the', 0.9776103496551514)], 
        [[[399.0, 446.0], [1207.0, 443.0], [1208.0, 484.0], [399.0, 488.0]], ('production of this book; their contributions', 0.9866490960121155)], 
        [[[401.0, 500.0], [1208.0, 500.0], [1208.0, 534.0], [401.0, 534.0]], ('have been indispensable to its creation.We', 0.9628525972366333)], 
        [[[399.0, 550.0], [1209.0, 548.0], [1209.0, 583.0], [399.0, 584.0]], ('would also like to express our gratitude to all', 0.9740485548973083)], 
        [[[399.0, 600.0], [1207.0, 598.0], [1208.0, 634.0], [399.0, 636.0]], ('the producers for their invaluable opinions', 0.9963331818580627)], 
        [[[399.0, 648.0], [1207.0, 646.0], [1208.0, 686.0], [399.0, 688.0]], ('and assistance throughout this project. And to', 0.9943731427192688)], 
        [[[399.0, 702.0], [1209.0, 698.0], [1209.0, 734.0], [399.0, 738.0]], ('the many others whose names are not credited', 0.9772290587425232)], 
        [[[399.0, 750.0], [1211.0, 750.0], [1211.0, 789.0], [399.0, 789.0]], ('but have made specific input in this book, we', 0.997929036617279)], 
        [[[397.0, 802.0], [1090.0, 800.0], [1090.0, 839.0], [397.0, 841.0]], ('thank you for your continuous support.', 0.9981997609138489)]]


# Load the image
image_path = os.path.join(os.path.dirname(__file__), "../PaddleOCR/ppocr_img/imgs_en/img_12.jpg")
img = cv2.imread(image_path)

# Check if the image was loaded correctly
if img is None:
    print("Error: Could not load the image.")
    exit()

# Define color (green) and font
text_color = (0, 255, 0)  # Green in BGR format
font = cv2.FONT_HERSHEY_SIMPLEX
font_thickness = 2

# Loop through each data item and draw the polygons and text
for item in data:
    box_points = np.array(item[0], np.int32)  # Bounding box points
    text = item[1][0]  # Extract the text from the tuple

    # Draw the polygon for the bounding box
    cv2.polylines(img, [box_points], isClosed=True, color=text_color, thickness=2)

    # Calculate the height of the bounding box to adjust the font size
    box_height = abs(box_points[0][1] - box_points[3][1])
    font_scale = box_height / 25  # Adjust scale factor as needed for better fit

    # Set text starting position at the left edge of the box
    x, y = box_points[0][0], box_points[0][1] + box_height - 5  # Offset y to align with the box bottom

    # Put the text starting from the left edge of the bounding box with dynamic font size
    cv2.putText(img, text, (x, y), font, font_scale, text_color, font_thickness)

# Display the resulting image
cv2.imshow('Overlayed Text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

