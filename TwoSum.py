#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
import time

def twoSum_simple(nums_list, target):
    """
    return the indices of the two numbers such that they add up to a specific target.

    Args:
        nums_list (List[int]): list of intergers
        target (int): taget value

    Returns:
        List[int]: list of indices

    """
    try:
        dico = {}
        for index, num in enumerate(nums_list):
            val = target - num

            if val not in dico:
                dico[num] = index
            else:
                return [dico[val], index]
    except:
        print('incorrect input')


def twoSum_Two(nums_list, target):

    try:
        mapping = {n: i for i, n in enumerate(nums_list)}

        for i, num in enumerate(nums):
            val_index = mapping.get(target - num, False)

            if val_index and val_index != i:
                return [i, val_index]
    except:
        print('incorrect input')



if __name__ == '__main__':
    print('1 --> run the twosum function; 2 --> evaluate the runtime of the solutions')

    input_list = list(map(int, input('enter the list of intergers ').split()))
    input_target = int(input())
    choice = int(input('what do you want to do ?')) #running mode

    if choice == 1:
        print(twoSum_Two(input_list, input_target))

    elif choice == 2:
        time_start_1 = time.time()
        twoSum_simple(input_list, input_target)
        duration_1 = time.time() - time_start_1

        time_start_2 = time.time()
        twoSum_Two(input_list, input_target)
        duration_2 = time.time() - time_start_2

        performance = (abs(duration_2 - duration_1)/duration_1) * 100 #performance of the second algo compare to the simple approach

        print("The second algo is {0: .2f}".format(performance))

    else:
        print("enter a valid choice")
