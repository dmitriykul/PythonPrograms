#Модуль Statistics
import statistics

nums = [1, 5, 33, 12, 46, 33, 2]

#Среднее
print(statistics.mean(nums))

#Медиана
print(statistics.median(nums))

#Мода
print(statistics.mode(nums))

print(statistics.median_low(nums))
