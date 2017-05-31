
pulse = 80


def get():
    # return last pulse value read from fitbit
    global pulse
    return pulse


def update():
    # read pulse value from fitbit
    global pulse

    # TODO: @zio get value from fitbit


def danger():
    return False


def set(value):
    # set value for demonstration
    global pulse
    pulse = value
