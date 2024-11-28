def read(n: int, book: [int], target: int) -> str:
    # Write your code here.
    seen = set()
    for pages in book:
        required = target - pages
        if required in seen:
            return "YES"
        seen.add(pages)
    
    return "NO"
