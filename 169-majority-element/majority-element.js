/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let count = {};

    for (let num of nums){
        count[num] = (count[num] || 0) + 1;
    }
    let max_count =0;
    let result = 0;
    for (let key in count){
        if (count[key] > max_count ){
            max_count = count[key];
            result = key;
        }

    }
    return Number(result);

    


    
};