import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image_file", help="The file to put on the wall! (Max res 160x120)")
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()