H = 6
W = 25
IMAGE_SIZE = H * W
inp = open("inputs/day08.txt").read()
layers = []
while inp:
    layers.append(inp[:IMAGE_SIZE])
    inp = inp[IMAGE_SIZE:]
        

def part1():
    row_with_lowest_0s = []
    lowest_num_of_zeros = IMAGE_SIZE
    for layer in layers:
        if layer.count('0') < lowest_num_of_zeros:
            lowest_num_of_zeros = layer.count('0')
            row_with_lowest_0s = layer
        
    return row_with_lowest_0s.count('1') * row_with_lowest_0s.count('2')


def part2():
    decoded = list(layers[0])
    for layer in layers:
        for i in range(len(layer)):
            if decoded[i] == '2':
                decoded[i] = layer[i]

    image = ''
    while decoded:
        for i in range(W):
            image += decoded[i]
        image += '\n'
        decoded = decoded[W:]

    return image.replace('0', ' ')


print (part1())
print (part2())