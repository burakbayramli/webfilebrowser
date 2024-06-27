# webfilebrowser

- Allows browsing of files, folders through simple Web interface,
  works on Flask.

- Double click to view files, or see contents of a directory.

- For multiselect copy, move or delete, first check items from the
  left handside, and click on radio buttons of copy, or move. This
  puts you into target selection mode, browse to the directory you
  want to go to, and click 'done'. In case of delete, simply click
  done.

- App allows viewing of text files, png, jpg image files, pdf, and mp4
  video.

<img width="340" src="webfilebrowser.png"/>

### Architecture

The app is quite small, 300 LOC in all. Most of the work is done on the
client side via Javascript, only file manipulation tasks are done on
the server. Communication between client and server is via Ajax.

### TODO

- Dot files are filtered out, toggling that permission to view can be useful

- After multiselect, building of zip and download support

- "Favorites" folders to quickly jump between directories, the fav list
  can be read from a config file by flask, or stored on `localStorage`,
  specific to each user.

- Support for peacemeal reading of video, currently video viewing does
  not allow to skipping to any location, that feature would require
  using the range request feature of web transfers.

