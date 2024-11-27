from typing import List
from collections import defaultdict

def getFrequencies(v: List[int]) -> List[int]: 
    # Write your code here
    freq_map = defaultdict(int)

    for num in v:
        freq_map[num] += 1

        max_freq = -1
        min_freq = float('inf')
        max_freq_element = None
        min_freq_element = None

    for num,freq in freq_map.items():
        if freq > max_freq:
            max_freq = freq
            max_freq_element = num
        elif freq == max_freq:
            max_freq_element = min(max_freq_element,num)
            
        if freq < min_freq:
            min_freq = freq
            min_freq_element = num
        elif freq == min_freq:
            min_freq_element = min(min_freq_element,num)

    return[max_freq_element,min_freq_element]

    
