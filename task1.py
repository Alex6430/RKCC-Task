import sys
import argparse
import re


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', "-f", type=argparse.FileType(), required=True)

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    text = namespace.name.read()
    if not text:
        print("file is empty")
        sys.exit()
    else:
        pattern = r"[eE][rR][rR][oO][rR].[0-9]{1,}"
        # print((re.findall(pattern, text)))
        error_list = (re.findall(pattern, text))
        if not error_list:
            print("the keyword ERROR was not found in the file")
            sys.exit()
        else:
            error_map = dict((x, error_list.count(x)) for x in set(error_list) if error_list.count(x) >= 1)
            list_error_map = list(error_map.items())
            list_error_map.sort(key=lambda i: i[1], reverse=True)
            list_error_map = list_error_map[:10]
            for err in list_error_map:
                print("{0} : {1}".format(err[0].upper().replace(":"," "), err[1]))