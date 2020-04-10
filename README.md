# shmpcount

OpenCV desktop app with GTK+

## Binaries

Download from [Releases](https://github.com/kanokkorn/shmpcount/releases)

## Development

For development, You need to download and install requires dependencies. Follow the guides

Assume you have x64 processor

### Windows

Can be compile from source, but pre-build binaries are recommend

- [Python 3.6 or higher](https://www.python.org/downloads/)
- [Cairo](http://ftp.gnome.org/pub/GNOME/binaries/win64/dependencies/cairo_1.8.8-1_win64.zip)
- [PyGobject](http://ftp.gnome.org/pub/GNOME/binaries/win32/pygobject/)
- [GTK+ Runtime](http://ftp.gnome.org/pub/GNOME/binaries/win64/gtk+/)
- [Glade](https://glade.gnome.org/) For developing UI

### Ubuntu

- Python3

```bash
sudo apt install -y python3-dev python3-pip
```

- GTK+2

```bash
sudo apt install -y build-essential gtk+2.0 libcairo2-dev libjpeg-dev libgif-dev
```

- Python binding

```bash
sudo apt install -y python3-gi-cairo python3-gi
```

- Glade (Optional)

```bash
sudo apt-get install -y glade-gtk2
```

UI files are locate in  ```ui``` folder

## License

[BSD 3](https://github.com/kanokkorn/shmpcount/blob/master/LICENSE)
