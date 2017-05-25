
import Adafruit_MCP3008

# SPI Configuration
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25

mcp = None
alcohol = 0.0


def init():
    global mcp
    mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)


def get():
    # return last alcohol value read from breathalyzer
    global alcohol
    return alcohol


def update():
    # read real value from breathalyzer
    global alcohol

    value = mcp.read_adc(0)
    value = value - 150
    if value < 0:
        value = 0
    value = 2.0 * value / 1024.0

    alcohol = value


def set(value):
    # set value for demonstration
    global alcohol
    alcohol = value
