#include "serverWriter.h"

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

    serverWriter test(7777);
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
            Mat frame;
            while(cap.isOpened()){cap >> frame; test.write(frame); frame.release();}
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