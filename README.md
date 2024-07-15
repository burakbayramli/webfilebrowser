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

### Architecture and Usage

The app is quite small, 300 LOC in all. Most of the work is done on the
client side via Javascript, only file manipulation tasks are done on
the server. Communication between client and server is via Ajax.

To use locally, for testing, simply

```
python app.py
```

This starts a server accessible on `127.0.0.1` aka `localhost`. 

To expose the server to others in the network, change the `app.py`
file to say, e.g. for `192.168.1.1`,

```
app.run(host="192.168.1.1",port=8080)
```

Now running `app.py` will start a server accessible on port 8080 via
the IP adress shown. 

### TODO

- Dot files are filtered out, toggling that permission to view can be
  useful. Priority: low.

- Multiselect and zip, then download feature. Priority: medium.

- "Favorites" folders to quickly jump between directories, the fav list
  can be read from a config file by flask, or stored on `localStorage`,
  specific to each user. Priority: low.

- Support for peacemeal reading of video, currently video viewing does
  not allow to skipping to any location, that feature would require
  using the range request feature of web transfers. Priority: low.

- HTML view of local files does not show `img` references to local
  images in the same directory because those refs also need their
  `/get_file` calls. Priority: low.


