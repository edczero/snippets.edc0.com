#!/bin/bash

export PATH=/opt/homebrew/bin:$PATH

for f in "$@"
do
    album_name=${Choosen_Item}
    rclone copy -v --check-first --size-only \
      --ignore-existing --max-size 1G --max-age 30d -u \
      --no-update-modtime "$f" \
      GPhotos-Personal:/album/$album_name/

    osascript -e 'display notification "'"$f"'" with title "'"Upload Finished: $album_name"'"'
done 