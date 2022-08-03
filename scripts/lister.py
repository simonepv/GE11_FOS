import os
import sys

def main():
    inDirName = "Output/"
    outFileName = "ListDataFile.txt"
    os.system( 'ls -d -1 "$PWD/"'+inDirName+'*.* > '+outFileName )

if __name__ == '__main__':
   main()
