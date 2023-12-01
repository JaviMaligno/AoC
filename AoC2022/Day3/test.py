from C3 import compute_priority, compute_group_priority, priorities

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
with open(r'Day3\test.txt') as f:
    text  = f.read()
    priority = compute_priority(text)
    print(priority == 157)
    group_priority = compute_group_priority(text)
    print(group_priority == 70)



