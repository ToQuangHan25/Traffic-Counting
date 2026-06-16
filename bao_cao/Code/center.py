def get_center(box):
    cx = int((box[0] + box[2]) / 2)
    chieu_cao_box = box[3] - box[1]
    cy = int(box[3] - (chieu_cao_box * 0.15))
    return (cx, cy, chieu_cao_box)