#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for idx in names:
        if idx[0:2] != "__":
            print(idx)
