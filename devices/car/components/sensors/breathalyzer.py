
alcohol = 0


def get():
    # return last alcohol value read from breathalyzer
    global alcohol
    return alcohol


def update():
    # read real value from breathalyzer
    global alcohol

    # TODO: @zio read value from breathalyzer


def set(value):
    # set value for demonstration
    global alcohol
    alcohol = value
