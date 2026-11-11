def find_max_min(numbers):
    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:

      if num > maximum:
        maximum = num

      if num < minimum:
        minimum = num

    return maximum,minimum

numbers = [10,25,5,40,15]

maximum,minimum = find_max_min(numbers)

print("Maximum:",maximum)
print("Minimum:",minimum)
