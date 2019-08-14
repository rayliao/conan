import json


def file():
    with open('./result.txt', 'a') as f:
        f.write('new line')


def demo():
    with open('./result.txt') as f:
        for line in f.readlines():
            l = json.loads(line)
            print(l['title'])


if __name__ == "__main__":
    demo()
