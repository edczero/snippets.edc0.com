#!/usr/bin/env python3

import os
import sys
import json
import time
import base64
import mimetypes
import subprocess
from pathlib import Path



NOTIFY_SCRIPT = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''

def notify(title, text):
  subprocess.call(['osascript', '-e', NOTIFY_SCRIPT, title, text])


mime_to_folder = {"application": "files", "image": "images", "video": "videos", "other": "archives"}

album_names = {"Screenshots": "Desktop-Screenshots",
			"Desktop": "Desktop-Screenshots",
			"Downloads": "Longspur",
			"Documents": "Longspur",
}

# Process files passed
input_files = sys.argv[1:]

print (input_files)


for f in input_files:
	if not os.path.exists(f):		
		sys.exit("File path doesn't exist")
	
	mt, k= mimetypes.guess_type(f)
	
	if mt:
		if "image" not in mt:
			sys.exit("Not an image file")
			
	parent_dir = os.path.basename(Path(f).parent)
	album_name = album_names.get(parent_dir, "Longspur")
	
	cmd = "/opt/homebrew/bin/rclone copy -v --check-first --size-only --ignore-existing --max-size 1G --max-age 30d -u --no-update-modtime " + f + " GPhotos-Personal:/album/" + album_name + "/"
	

	out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True, text=True)
	notify("Upload finished", out)
		
		  
