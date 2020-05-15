# put your python code here
length = int(input())
width = int(input())
height = int(input())


def sum_of_edges(l, w, h):
    s = 4 * (l + w + h)
    return s


def surface_area(l, w, h):
    S = 2 * (l * w + w * h + l * h)
    return S


def volume(l, w, h):
    V = l * w * h
    return V


print(sum_of_edges(length, width, height))
print(surface_area(length, width, height))
print(volume(length, width, height))
