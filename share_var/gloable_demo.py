from share_var.gloable import lis
import time


def change():
    global lis

    for i in range(100):
        lis.append(i)
