#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>

#define SIZE 1024

int main(int argc, char *argv[])
{
    int file;
    ssize_t bytes_read;

    unsigned char buffer[SIZE];

    uint32_t checksum = 0;

    if (argc != 2)
    {
        printf("Utilizare: %s <fisier>\n", argv[0]);
        return EXIT_FAILURE;
    }

    file = open(argv[1], O_RDONLY);

    if (file == -1)
    {
        perror("[ERROR] -> deschiderea fisierului");
        return EXIT_FAILURE;
    }

    while ((bytes_read = read(
        file,
        buffer,
        sizeof(buffer)
    )) > 0)
    {
        for (ssize_t i = 0; i < bytes_read; i++)
        {
            checksum += buffer[i];
        }
    }

    if (bytes_read == -1)
    {
        perror("[ERROR] -> citirea fisierului");

        close(file);

        return EXIT_FAILURE;
    }

    if (close(file) == -1)
    {
        perror("[ERROR] -> inchiderea fisierului");

        return EXIT_FAILURE;
    }

    printf("FISIER: %s\n", argv[1]);
    printf("Checksum: %08X\n", checksum);

    return EXIT_SUCCESS;
}
