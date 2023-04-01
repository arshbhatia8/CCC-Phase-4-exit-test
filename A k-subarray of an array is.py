def kSub(k, nums):
    # Write your code here
    
    
    
    # Initialize frequency array with count of 0 remainder as 1
    freq = [1] + [0] * k
    prefix_sum = 0
    count = 0
    
    for num in nums:
        # Calculate prefix sum
        prefix_sum += num
        
        # Calculate remainder
        remainder = prefix_sum % k
        
        # Update frequency array
        count += freq[remainder]
        freq[remainder] += 1
    
    return count
