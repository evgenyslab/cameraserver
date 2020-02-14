#include "imageServer.h"
#include "commServer.h"

int main(int argc, char *argv[])
{
    enum mode{webcam, noise};
    int opmode = noise;
    if (argc>1){
        if (strcmp(argv[1],"--webcam")==0)
            opmode = webcam;
        else if (strcmp(argv[1],"--noise")==0)
            opmode = noise;
    }

    imageServer test(7777);
    // TODO, create comm server
    test.start();
    switch (opmode){
        case webcam:{
            VideoCapture cap;
            bool ok = cap.open(0);
            if (!ok)
            {
                printf("no cam found ;(.\n");
                pthread_exit(NULL);
            }
            Mat frame, _rframe;
            while(cap.isOpened()){
                cap >> frame;
                if (frame.rows > 600 | frame.cols > 600)
                    cv::resize(frame, _rframe, cv::Size(640,int(frame.rows * (680.0 / frame.cols))));
                else
                    _rframe = frame;
                test.write(_rframe); frame.release(); _rframe.release();}
            break;
        }
        case noise:{
            while(1) {
                Mat img(480, 640, CV_8UC3);
                randu(img, Scalar(0, 0, 0), Scalar(255, 255, 255));
                test.write(img);
                img.release();
            }
            break;
        }
    }

    test.stop();

    exit(0);

}