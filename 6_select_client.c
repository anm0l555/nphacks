#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>
#define PORT 8080
   
int main(int argc, char const *argv[])
{
    int socketR = 0, returnValue;

    struct sockaddr_in serv_addr;
    
    char buffer[1024] = {0};
    
    socketR = socket(AF_INET, SOCK_STREAM, 0);
    if(socketR < 0)
    {
        printf("\n Socket creation error \n");
        return -1;
    }
    

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);
       
    if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)<=0) 
    {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }
   

    if (connect(socketR, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
    {
        printf("\nConnection Failed \n");
        return -1;
    }
    
    char buff[1024];
    int num=0;

    bzero(buff, sizeof(buff));
    returnValue = read( socketR , buffer, 1024);
    printf("Message Recieved from Server - \n");
    printf("%s\n",buffer );


    while(1)
    {
        bzero(buff, sizeof(buff));
        printf("Enter the String : ");
        while ((buff[num++] = getchar()) != '\n');
        send(socketR , buff , strlen(buff) , 0);
        printf("Message sent to Server Succesfully - \n");
        if(strncmp("end", buff, 3) == 0)
            break;

        bzero(buffer, sizeof(buffer));
        returnValue = read( socketR , buffer, 1024);
        printf("Message Recieved from Server - \n");
        printf("%s\n",buffer );
        //puts("While Running\n");
    }
    

    close(socketR);

    return 0;
}
