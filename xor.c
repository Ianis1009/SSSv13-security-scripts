#include <stdio.h>
#include <string.h>

#define MAX 257

int main () {

    FILE* fin = fopen("xorcrypt.in", "r");
    FILE* fout = fopen("xorcrypt.out", "w");


    char text[MAX], key[MAX];
    fgets(text, MAX, fin);
    fgets(key, MAX, fin);
    text[strcspn(text, "\n")] = '\0';
    key[strcspn(key, "\n")] = '\0';

    int n = strlen(text);

    for (int i = 0; i < n; i++ ) {
        unsigned char x = text[i] ^  key[i];
        for (int j = 7; j >= 0; j--) {
            if (x & (1 << j)) {
                fprintf(fout, "1");
            } else {
                fprintf(fout, "0");
            }
        }

        if (i < n - 1) {

            fprintf(fout, " ");
        }
    }

    //close
    fclose(fin);
    fclose(fout);
    return 0; 
}