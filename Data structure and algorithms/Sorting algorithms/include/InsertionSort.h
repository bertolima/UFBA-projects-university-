template<class T>
void InsertionSort(T arr[], int size) {
	int j;
    T key;
	for (int i = 1; i < size; i++) {
		key = arr[i];
		j = i - 1;

		while (j >= 0 && arr[j] > key) {
			arr[j + 1] = arr[j];
			j--;
		}
		arr[j + 1] = key;
	}
}