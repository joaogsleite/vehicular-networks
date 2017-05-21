
attention = 0


def get():
    # return last alcohol value read from mindwave
    global attention
    return attention


def update():
    # read real value from mindwave
    global attention

    # TODO: @zio read value from mindwave


def update(value):
    # set value for demonstration
    global attention
    attention = value