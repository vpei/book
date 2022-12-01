import hashlib
# import ipfsapi
import os
import io
import sys
 
def printUsage():
	print ('''Usage: [python] pymd5sum.py ''')

def geneMd5(filename):
    m = hashlib.md5()
    file = io.FileIO(filename, 'r')
    bytes = file.read(1024)
    while(bytes != b''):
        m.update(bytes)
        bytes = file.read(1024) 
    file.close()
    return m.hexdigest()

# def geneCID(filename):
#     api = ipfsapi.connect('127.0.0.1', 5001)
#     res = api.add(filename)
#     # print (res)
#     return res

def main():
    if(len(sys.argv) != 1 and len(sys.argv) != 2):
        printUsage()
    # mat = '{:48}\t{:32}'
    if(len(sys.argv)==1):
        # path='D://xfmovie//pilimi-zlib-0-119999//'
        path='D://zlib-torrent//pilimi-zlib-all//'
    if(len(sys.argv)==2):
        path=sys.argv[1]
    for fpathe,dirs,fs in os.walk(path):
        for f in fs:
            full_file = os.path.join(fpathe,f)
            # print (mat.format(full_file.replace(path, ''),geneMd5(full_file)))
            print (full_file.replace(path, '') + ' ' + geneMd5(full_file).upper()) # + ' ' + geneCID(full_file))
main()


# pip3 install ipfsapi
# python md5.py > md5.txt