#bubble sort algorthim python  | in python--------------------------------------------------------------------------------------

def bubble_sort(nums):
	#ser swapped to true so the loop looks runs at last onece 
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(nums) - 1):
			if nums[i] > nums[i + 1]:
				#swapped the elements
				nums[i], nums[i + 1] = nums[i + 1], nums[i]
				#set the flag to true true so well loop again 
				swapped = True



random_lists = [5,10,11,16,22,3,1,9,0,7]
bubble_sort(random_lists)
print('The result of bubble_sort algorthim')
print(random_lists)