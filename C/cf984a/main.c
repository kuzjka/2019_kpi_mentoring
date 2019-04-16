#include <stdio.h>

#define MAX_SIZE 1000
#define INSERTION_THRESHOLD 40

int solution(int* data, int size);
void merge_sort(int* data, int size);
void insertion_sort(int* data, int size);

int data[MAX_SIZE];
int tmp[MAX_SIZE];

int main() {
//    freopen("input.txt", "r", stdin);
    int size;
    scanf("%d\n", &size);
    register int* it = data;
    register int* end = data + size;
    while (it != end) {
        scanf("%d", it++);
    }
    printf("%d\n", solution(data, size));
    return 0;
}

int solution(int* data, int size) {
    merge_sort(data, size);
    return *(data + (size - 1) / 2);
}

void merge_sort(int* data, int size) {
    insertion_sort(data, size);
}

void insertion_sort(int* data, int size) {
    register int* it = data + 1;
    register int* end = data + size;
    register int* left;
    register int* right;
    register int key;
    while (it < end) {
        key = *it;
        right = it;
        left = it - 1;
        while (*(left) > key) *(right--) = *(left--);
        *right = key;
        ++it;
    }
}