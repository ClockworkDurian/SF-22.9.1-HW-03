def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return low

def input_and_validate_numbers():
    sequence = input("Введите последовательность чисел через пробел: ").split()
    if not all(x.isdigit() for x in sequence):
        raise ValueError("Последовательность должна состоять из целых чисел")
    number = int(input("Введите любое число: "))
    return list(map(int, sequence)), number

def sort_sequence(arr):
    for i in range(len(arr)):
        idx_min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[idx_min]:
                idx_min = j
        if i != idx_min:
            arr[i], arr[idx_min] = arr[idx_min], arr[i]

def main():
    try:
        sequence, number = input_and_validate_numbers()
        sort_sequence(sequence)
        position = binary_search(sequence, number)
        if position < len(sequence) and sequence[position] == number:
            print(f"Число {number} находится на позиции {position}")
        elif position == len(sequence):
            print(f"Число {number} больше всех чисел в последовательности, а позиция ближайшего меньшего элемента равна {position-1}")
        else:
            print(f"Число {number} находится между числами {sequence[position-1]} и {sequence[position]}, а позиция числа {sequence[position-1]} равна {position-1}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()