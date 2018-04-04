#include <stdlib.h>
int* tlow1(int start, int end) { 
    int len = 0, max = 0, size = sizeof(start)*(end-start)+1; int *arr = malloc(size); 
    for (int i = start; i < end || i == start; i++){
        int counter = 0;
        for (int j = 1; j <= end; j++){if (i % j == 0){counter++;}} 
        if (counter > max) {max = counter; len = 0; arr = malloc(size);}
        if (counter == max) {arr[len] = i; len++;}
    } arr[len] = -1; return arr;
}
