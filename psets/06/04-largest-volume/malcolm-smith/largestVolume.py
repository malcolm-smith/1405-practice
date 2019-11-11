def maxvolume(arr):
    largestBox = [arr[0]]
    largestVolume = arr[0][1] * arr[0][1] * arr[0][2]
    for box in arr:
        volume = box[0] * box[1] * box[2]
        if volume > largestVolume:
            largestBox = box
            largestVolume = volume
    return largestBox