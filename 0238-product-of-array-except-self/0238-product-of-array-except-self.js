/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
  const n = nums.length;
  const left = new Array(n);
  const right = new Array(n);
  const res = new Array(n);

  // 1. 前缀乘积
  let prefix = 1;
  for (let i = 0; i < n; i++) {
    left[i] = prefix;
    prefix *= nums[i];
  }

  // 2. 后缀乘积
  let suffix = 1;
  for (let i = n - 1; i >= 0; i--) {
    right[i] = suffix;
    suffix *= nums[i];
  }

  // 3. 结果：左右乘积相乘
  for (let i = 0; i < n; i++) {
    res[i] = left[i] * right[i];
  }

  return res;
};
