#!/usr/bin/env python
import os, sys, getopt
import PIL.Image

def writeFloorFile(filename, data):
    f = open(filename, 'w')
    f.write(data)
    f.close()

def generateEmptyMap(width, height, blocksize):
    data = []
    for h in range(0, height, blocksize):
        data.append([True] * (width / blocksize) )
    return data

def convertMapToPolygons(data, blocksize):
    rowFormat = '* %s, %s; %s, %s; %s, %s; %s, %s'
    result = []
    for rowIdx, row in enumerate(data):
        for cellIdx, cell in enumerate(row):
            if cell == True:
                x1 = cellIdx * blocksize
                y1 = rowIdx * blocksize
                x2 = x1
                y2 = y1 + blocksize
                x3 = x1 + blocksize
                y3 = y1 + blocksize
                x4 = x1 + blocksize
                y4 = y1
                result.append(rowFormat % (x1, y1, x2, y2, x3, y3, x4, y4) )
    result.reverse()
    return result

def applyWalkableImageToMap(imagefilename, blocksize):
    im = PIL.Image.open(imagefilename)
    rgb_im = im.convert('RGB')
    data = generateEmptyMap(im.size[0], im.size[1], blocksize)
    for rowIdx, row in enumerate(data):
        for cellIdx, cell in enumerate(row):
            x = cellIdx * blocksize + (blocksize / 2)
            y = rowIdx * blocksize + (blocksize / 2)
            r, g, b = rgb_im.getpixel((x, y))
            data[rowIdx][cellIdx] = (r + g + b > 0)
    return data

def parseCommandOptions(argv):
    helpline = 'Parameters: [-b <pixel blocksize>] -i <imagemap file>' + \
        '\nExample: python floor-gen.py -i data/plateau_zones.png -b 20'
    inputfile = None
    blocksize = 5
    try:
        opts, args = getopt.getopt(argv,"hi:b:",["imagemap=","blocksize="])
    except getopt.GetoptError:
        print helpline
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print helpline
            sys.exit()
        elif opt in ("-i", "--imagemap"):
            inputfile = arg
        elif opt in ("-b", "--blocksize"):
            blocksize = arg
    if (inputfile == None):
        print(helpline)
        return False
    else:
        return (inputfile, blocksize)

if __name__ == '__main__':
    options = parseCommandOptions(sys.argv[1:])
    if options:
        #print('image: ', options[0])
        #print('blocksize: ', options[1])
        mymap = applyWalkableImageToMap(options[0], options[1])
        myfile = convertMapToPolygons(mymap, options[1])
        fileparts = os.path.splitext(options[0])
        writeFloorFile(fileparts[0] + '.flo', '\n'.join(myfile) )
        #print('\n'.join(myfile))
