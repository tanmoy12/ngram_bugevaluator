
def bubbleSort(arr):
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

numbers_input = map(int, input("Enter numbers separated by spaces").strip().split(' '))

bubbleSort(arr)

for i in range(len(arr)):
