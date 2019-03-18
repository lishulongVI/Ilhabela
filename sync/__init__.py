def add(a):
    a += 1
    return a


def desc(a):
    a -= 1
    return a


if __name__ == '__main__':
    import dis

    print(dis.dis(add))
    print(
        '*' * 20
    )
    print(dis.dis(desc))
