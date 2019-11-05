#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <pthread.h>
#include <iostream>

class commServer{

    private:
        int clients[100];
        int n = 0;
        pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

    public:

        commServer(){};

        void run();

};