class Solution:
	def sol(self, arr):
		return self.__helper(arr, len(arr))

	def __helper(self, arr, n):
		addition = 0
		for i in arr:
			addition += i

		return addition

def main():
	print('This is the main function of this program. Creating a function which will return sum of array.')
	print(f'The sum of array [2, 3, 5, 89, 19] is {Solution().sol([2, 3, 5, 89, 19])}')


if __name__ == '__main__':
	main()
