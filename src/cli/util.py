import argparse
import os

def is_int(value):
    try:
        return int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"\"{value}\" is not a valid integer")


def is_file_path(value):
    path = os.path.dirname(os.path.realpath(__file__)) + "/" + value
    if (not os.path.isfile(path) and (not os.path.exists(path))):
        raise argparse.ArgumentTypeError(f"\"{value}\" is not a valid file path")
    return value