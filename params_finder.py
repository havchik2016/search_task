def find_params(toponym):
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    toponym_left_down = toponym["boundedBy"]["Envelope"]["lowerCorner"]
    x1, y1 = toponym_left_down.split(" ")
    toponym_up_right = toponym["boundedBy"]["Envelope"]["upperCorner"]
    x2, y2 = toponym_up_right.split(" ")

    delta_x = str((float(x2) - float(x1)) / 2)
    delta_y = str((float(y2) - float(y1)) / 2)
    size_x = int(float(delta_x) * 200000)
    size_y = int(float(delta_y) * 200000)
    if size_x > 650:
        size_x1 = 650
    else:
        size_x1 = size_x
    if size_y > 450:
        size_y1 = 450
    else:
        size_y1 = size_y

    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([delta_x, delta_y]),
        "l": "map",
        "pt": ",".join([toponym_longitude, toponym_lattitude, "pmwtm"]),
        "size": ",".join([str(size_x1), str(size_y1)])
    }
    return map_params, size_x1, size_y1
