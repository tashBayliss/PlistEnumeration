#Full scan script

#~/Documents/Project/Files/1(1)/uk.co.costa.club_578627826_v3.28.0_947.ipa
#~/Documents/Project/uk.co.costa.club_578627826_v3.28.0_947.ipa

import os
import plistTool

#38 files
directory = os.path.expanduser("~/Documents/Project/Files/1(1)")

for filename in os.listdir(directory):
    if filename.endswith(".ipa"):
        plistTool.checkPath(os.path.join(directory, filename), 10)

    else:
        continue
