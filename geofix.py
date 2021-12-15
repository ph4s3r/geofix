"""

Author: Peter Karacsonyi

Usage: python geofix.py <path>
where <path> is a folder where target files with .geojson extension are stored

"""

import sys, os
import json
from pathlib import Path

filelist = []

newdirname = 'fixed'

os.makedirs(newdirname)

mypath = Path(sys.argv[1])
if not mypath.exists():
    print(f"path {mypath.resolve()} could not be resolved, exiting")
    sys.exit(-1)

print(f"enumerating files in path {mypath.resolve()}: \n")
for idx, file in enumerate(mypath.glob("*")):
    if 'geojson' in str(file):
        filelist.append(file)

for file in filelist:
    newfilename = newdirname + "/" + file.name
    with open(file, 'rt') as f:
        jsondata = json.load(f)

    jsondata['features'][0].pop('type')
    out = [jsondata['features'][0]]

    with open(newfilename, 'wt') as f:
        json.dump(out,f)
        print(f"read and converted file written to {str(file)}")
