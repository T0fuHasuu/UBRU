#include <stdio.h>
#define MAX 50

void merge(int arr[], int n, int low, int mid, int high);
void partition(int arr[], int n, int low, int high);

void mergesort(int arr[], int n, int low, int high) {
    int mid;
    if (low < high) {
        mid = (low + high) / 2;
        mergesort(arr, n, low, mid);
        mergesort(arr, n, mid + 1, high);
        merge(arr, n, low, mid, high);
    }
}

void merge(int arr[], int n, int low, int mid, int high) {
    int i, m, k, l, temp[MAX];
    l = low;
    i = low;
    m = mid + 1;

    while ((l <= mid) && (m <= high)) {
        if (arr[l] <= arr[m]) {
            temp[i] = arr[l];
            l++;
        } else {
            temp[i] = arr[m];
            m++;
        }
        i++;
    }

    if (l > mid) {
        for (k = m; k <= high; k++) {
            temp[i] = arr[k];
            i++;
        }
    } else {
        for (k = l; k <= mid; k++) {
            temp[i] = arr[k];
            i++;
        }
    }

    for (k = low; k <= high; k++) {
        arr[k] = temp[k];
    }

    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int merge[MAX], i, n;
    printf("Enter the total number of elements: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        printf("\nElement %d: ", i + 1);
        scanf("%d", &merge[i]);
    }
    printf("\n");
    mergesort(merge, n, 0, n - 1);
    return 0;
}
