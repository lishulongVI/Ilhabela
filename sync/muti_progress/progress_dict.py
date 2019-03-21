from multiprocessing import Manager, Process


def to_add(d, k, v):
    d[k] = v


if __name__ == "__main__":
    process_dict = Manager().dict()
    p1 = Process(target=to_add, args=(process_dict, 'name', 'li'))
    p2 = Process(target=to_add, args=(process_dict, 'age', 13))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(process_dict)
