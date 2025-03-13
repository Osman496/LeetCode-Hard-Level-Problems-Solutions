def median(nums1, nums2):
    """
    Function to find the median of two sorted arrays.

    Approach:
    1. Merge the two arrays into one.
    2. Sort the merged array.
    3. If the length of the merged array is even:
       - The median is the average of the two middle elements.
    4. If the length of the merged array is odd:
       - The median is the middle element.

    Time Complexity: O((n + m) log (n + m)), where n and m are the lengths of nums1 and nums2.
    Space Complexity: O(n + m), due to the merged and sorted array.
    """
    
    # Step 1: Merge the two arrays
    nums1.extend(nums2)
    
    # Step 2: Sort the merged array
    nums1.sort()
    
    # Step 3: Calculate the median
    if len(nums1) % 2 == 0:
        # If the length is even, return the average of the two middle elements
        return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
    else:
        # If the length is odd, return the middle element
        return nums1[len(nums1) // 2]


# Test cases
print(median([1, 3], [2]))  # Output: 2.0
print(median([1, 2], [3, 4]))  # Output: 2.5


# Step-by-Step Explanation
# 1. Merge the Two Arrays:
# Use nums1.extend(nums2) to merge nums2 into nums1.

# Example:

# nums1 = [1, 3], nums2 = [2]

# After merging: nums1 = [1, 3, 2]

# 2. Sort the Merged Array:
# Use nums1.sort() to sort the merged array in ascending order.

# Example:

# After sorting: nums1 = [1, 2, 3]

# 3. Calculate the Median:
# Check if the length of the merged array is even or odd:

# Even Length:

# The median is the average of the two middle elements.

# Example:

# nums1 = [1, 2, 3, 4]

# Middle indices: 1 and 2 (values 2 and 3)

# Median: (2 + 3) / 2 = 2.5

# Odd Length:

# The median is the middle element.

# Example:

# nums1 = [1, 2, 3]

# Middle index: 1 (value 2)

# Median: 2

# Approach
# Merge the Arrays:

# Combine the two input arrays (nums1 and nums2) into a single array.

# Sort the Merged Array:

# Sorting ensures that the elements are in ascending order, making it easy to find the median.

# Find the Median:

# If the merged array has an even number of elements, the median is the average of the two middle elements.

# If the merged array has an odd number of elements, the median is the middle element.

# Time and Space Complexity
# Time Complexity: O((n + m) log (n + m))

# Merging the arrays takes O(n + m).

# Sorting the merged array takes O((n + m) log (n + m)).

# Space Complexity: O(n + m)

# The merged and sorted array requires additional space.