/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let last_non_zero = 0;
    for (let i =0;i<nums.length;i++){
        if (nums[i] != 0){
            let temp = nums[last_non_zero];
            nums[last_non_zero] = nums[i];
            nums[i] = temp;
            last_non_zero++;

        }
    }

    
};