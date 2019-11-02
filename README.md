# Camera Server

Build an application that has a c++ server backend for
interfacing with various cameras, open socket and send out
images on that socket.

Build a separate web-based application that can connect to 
image streaming server and display in web browser window.

Source for server:

[https://github.com/JPery/MJPEGWriter]

## Requirements

### macOS

- brew (on mac)
- cmake
- OpenCV

OpenCV:
```bash
# on macOS
brew install opencv
```

### linux

- OpenCV

## Usage

Compile:
```bash
mkdir build
cd build
cmake ..
make -j 8
```

Run:
```bash
./source [option]
```

wherein `[option]` is either `--webcam` or `--noise`. Webcam option has issue in CLion on macOS, but can be called from terminal. Noise option will generate random noise video feed.

## Issues

When working with CLion on macOS 10.14.6+ there is a webcam permissions issue
wherein macOS will not prompt to get permissions to use webcam through 
CLion when running the program. 
https://youtrack.jetbrains.com/issue/IDEA-219288
https://youtrack.jetbrains.com/issue/IDEA-224190#focus=streamItem-27-3723449.0-0
