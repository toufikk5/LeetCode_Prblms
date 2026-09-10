/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let n = nums.length;
    let expected_sum = n*(n+1)/2;
    let actual_sum=0;
    for (let num of nums){
         actual_sum += num
    }
return expected_sum-actual_sum

    
};