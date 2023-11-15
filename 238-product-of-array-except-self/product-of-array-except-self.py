class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product_of_non_zeros = 1
        for num in nums:
            if num != 0:
                product_of_non_zeros *= num
            else:
                zero_count += 1
                
        answer = []
        for num in nums:
            if zero_count > 1:
                # If more than one zero, all products will be zero
                answer.append(0)
            elif zero_count == 1:
            # If exactly one zero, only the position with zero will have non-zero product
                if num == 0:
                    answer.append(product_of_non_zeros)
                else:
                    answer.append(0)
            else:
            # If no zeros, divide the total product by the current element
                answer.append(product_of_non_zeros // num)

        return answer


        
        