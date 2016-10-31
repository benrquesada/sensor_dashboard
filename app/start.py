

def save_to_DB(_id, tag, value):
    sense = Sensor(_id = _id, tag = tag, value = value)
    sense.save()
