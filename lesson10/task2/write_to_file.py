zoo = ['lion', "elephant", 'monkey']

print("__name__: " + __name__)

if __name__ == "__main__":
    f = open("output.txt", 'a')

    for i in zoo:
        f.write(i)

    f.close()
