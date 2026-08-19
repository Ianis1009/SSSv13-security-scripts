#define _GNU_SOURCE

#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <unistd.h>

static int read_file_secure(int dirfd, const char *name)
{
    int fd;
    char buffer[4096];

    fd = openat(dirfd, name, O_RDONLY | O_CLOEXEC | O_NOFOLLOW);

    if (fd == -1) {
        perror("openat");
        return -1;
    }

    struct stat st;

    if (fstat(fd, &st) == -1) {
        perror("fstat");
        close(fd);
        return -1;
    }

    if (!S_ISREG(st.st_mode)) {
        fprintf(stderr, "Refusing non-regular file\n");
        close(fd);
        return -1;
    }

    for (;;) {
        ssize_t n = read(fd, buffer, sizeof(buffer));

        if (n == 0)
            break;

        if (n == -1) {
            if (errno == EINTR)
                continue;

            perror("read");
            close(fd);
            return -1;
        }

        if (write(STDOUT_FILENO, buffer, (size_t)n) == -1) {
            perror("write");
            close(fd);
            return -1;
        }
    }

    close(fd);
    return 0;
}

int main(int argc, char **argv)
{
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <directory> <file>\n", argv[0]);
        return EXIT_FAILURE;
    }

    int dirfd = open(argv[1], O_RDONLY | O_DIRECTORY | O_CLOEXEC);

    if (dirfd == -1) {
        perror("open directory");
        return EXIT_FAILURE;
    }

    int result = read_file_secure(dirfd, argv[2]);

    close(dirfd);

    return result == 0 ? EXIT_SUCCESS : EXIT_FAILURE;
}

/***
 * TODO: add rules 
 */