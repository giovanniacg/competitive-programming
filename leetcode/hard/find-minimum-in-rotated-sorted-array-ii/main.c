// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/

int findMin(int* nums, int numsSize) {
    int min = nums[0];

    for (int i = 0; i < numsSize; i++){
        if (nums[i] < min)
            min = nums[i];
        if (i > 0 && nums[i] < nums[i-1])
            break;
    }

    return min;
}