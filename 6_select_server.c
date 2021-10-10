#include <stdio.h>
#include <string.h> 
#include <stdlib.h>
#include <errno.h>
#include <unistd.h> 
#include <arpa/inet.h> 
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/time.h> 

#define PORT 8080

int main()
{
    int opt = 1;
    int masterSocket, addrlen, newSocket, clientSockets[30], maxClients = 30;
    int maxSd;

    fd_set readFD;
    struct sockaddr_in address;

    char buffer[1024];
    char *message = "This Server can Echo your Message Back\n";

    for(int i=0;i<maxClients;i++)
    {
        clientSockets[i] = 0;
    }

    masterSocket = socket(AF_INET, SOCK_STREAM, 0);
    if(masterSocket==0)
    {
        perror("Socket Failed");
        exit(EXIT_FAILURE);
    }

    int temp;
    temp = setsockopt(masterSocket, SOL_SOCKET, SO_REUSEADDR, (char *)&opt, sizeof(opt));
    if(temp<0)
    {
        perror("SetSockopt");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
	address.sin_addr.s_addr = INADDR_ANY;
	address.sin_port = htons( PORT );

    temp = bind(masterSocket, (struct sockaddr *)&address, sizeof(address));
    if(temp<0)
    {
        perror("Bind Failure");
        exit(EXIT_FAILURE);
    }

    temp = listen(masterSocket, 3);
    if(temp <0)
    {
        perror("Listen Error");
        exit(EXIT_FAILURE);
    }

    addrlen = sizeof(address);

    puts("Waiting for Connections.........");
    int sd, activity, valread, i;
    while(1)
    {
        FD_ZERO(&readFD);
        FD_SET(masterSocket, &readFD);
        maxSd = masterSocket;

        for(i=0;i<maxClients;i++)
        {
            sd = clientSockets[i];
            
            if(sd>0)
                FD_SET(sd, &readFD);
            
            if(sd>maxSd)
                maxSd = sd;
        }

        activity = select(maxSd+1, &readFD, NULL, NULL, NULL);
        if((activity<0)&&(errno!=EINTR))
        {
            printf("Select Error");
        }
        
        if(FD_ISSET(masterSocket, &readFD))
        {
            if((newSocket = accept(masterSocket, (struct sockaddr *)&address, (socklen_t*)&addrlen))<0)
            {   
                //printf("%d", newSocket);
                perror("Accept Error");
                exit(EXIT_FAILURE);
            }

            printf("New Connection of Client is Eastablished\n");
            
            // Sending the Greeting Message to Client - 
            send(newSocket, message, strlen(message), 0);
            puts("Welcome Message Sent Successfully\n");

            // Adding the New Socket into array of ClientSockets
            for(int j=0;j<maxClients;j++)
            {
                if(clientSockets[j]==0)//Checking Empty Position
                {
                    clientSockets[j] = newSocket;
                    printf("Added the Client FD %d into List as %d\n", newSocket, j);

                    break;
                }
            }
        }

        // Now If Some IO operation is performed on other running sockets
        for(i=0;i<maxClients; i++)
        {   
            bzero(buffer, sizeof(buffer));
            sd = clientSockets[i];
            if(FD_ISSET(sd, &readFD))
            {   
                valread = read(sd, buffer, 1024);
                if(strncmp("end", buffer, 3) == 0)
                {
                    getpeername(sd, (struct sockaddr *)&address, (socklen_t*)&addrlen);
                    printf("Connection Disconnected-\n");
                    printf("Ip is: %s, port: %d\n", inet_ntoa(address.sin_addr), ntohs(address.sin_port));

                    close(sd);
                    clientSockets[i] = 0;
                }
                else //Echoing the Client Message Back
                {
                    buffer[valread] = '\0';
					printf("Message Recieved from Client - ");
					printf("%s", buffer);
					send(sd , buffer , strlen(buffer) , 0 );
                }
            }
        }
    }

    return 0;
}
