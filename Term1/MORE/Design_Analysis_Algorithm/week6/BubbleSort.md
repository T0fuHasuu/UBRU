int arr[] = { 5, 2, 4, 6, 1, 3}
int n = 6
for (int i = 0; i < n - 1; i++){
   for (int j = 0; j < n - 1; j++){		// loop 5x5
       if (arr[j] > arr[j + 1]){			//compare index n and n+1
           swap(arr[j], arr[j + 1])		//swap array
       }
    }
}

//
Array Initialization:

int arr[] = { 5, 2, 4, 6, 1, 3}: An integer array arr is declared and initialized with the given values.
int n = 6: The size of the array arr is stored in the variable n.
Outer Loop:

for (int i = 0; i < n - 1; i++): This loop iterates n - 1 times. In each iteration, it processes the entire array once.
Inner Loop:

for (int j = 0; j < n - 1; j++): This loop iterates n - 1 times for each outer loop iteration, comparing adjacent elements.
Comparison and Swap:

if (arr[j] > arr[j + 1]): Compares the current element arr[j] with its next element arr[j + 1].
swap(arr[j], arr[j + 1]): If the current element is greater than the next, the elements are swapped.