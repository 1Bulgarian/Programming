#include <stdio.h>
#include <stdlib.h>

int main()
{
    char message[100];
    int change;

    printf("Message: ");
    fgets(message,100, stdin);

    printf("Change: ");
    scanf("%d", &change);

    printf("Original message: %s", message);

    encrypt(message,change);
    printf("Encrypted message: %s", message);


    return 0;
}

void encrypt(char* message, int shift) {
    int i = 0;

    while(message[i] != '\0') {
        char ltr = message[i];
        char base = (message[i] < 'a') ? 'A' : 'a';

        if(!((base == 'a' && (base + shift <=122)) || (base == 'A' && (base + shift <=90))))
        {

        }
        else if(!((base == 'a' && (base - shift >=97)) || (base == 'A' && (base - shift >=65))))
        {
            char a = 122-shift;
            if(base == 'A') message[i]=122-shift;
            else message[i]
        }
        else {
            message[i] = (((message[i] - base) + shift)%26)+base;
        }

        //A-Z
        if((message[i]>=65) && (message[i]<=90))
        {
            message[i] = (((message[i] - 65) + shift)%26)+65;
        }
        // a-z
        else if((message[i]>=97) && (message[i]<=122))
        {
            message[i] = (((message[i] - 97) + shift)%26)+97;
        }
        i++;
    }
}

int isAlphabetic(char c) {
    return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z');
}
