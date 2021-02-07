blocks = [
    {  # 1 0 4
        'gym': False,
        'school': True,
        'store': False
    },
    {  # 0 1 3
        'gym': True,
        'school': False,
        'store': False
    },
    {  # 0 0 2
        'gym': True,
        'school': True,
        'store': False
    },
    {  # 1 0 1
        'gym': False,
        'school': True,
        'store': False
    },
    {  # 2 0 0
        'gym': False,
        'school': True,
        'store': True
    },
]
requirements = ['gym', 'school', 'store']


# Helper function to find the distance between a block and a requirement
# Eg: for 'store' in first block it will return 4 and for 'gym' in first block it will return 1
def find_distance(req, blocks, pos):
    dist = 0
    if pos == 0:
        for i in range(1, len(blocks)):
            if req in blocks[i].keys() and blocks[i][req] is True:
                dist = i
                break
    elif pos == len(blocks) - 1:
        for i in range(len(blocks)-1, -1, -1):
            if req in blocks[i].keys() and blocks[i][req] is True:
                dist = i
                break
    else:
        temp = []
        for i in range(pos+1, len(blocks)):
            if req in blocks[i].keys() and blocks[i][req] is True:
                temp.append(i-pos)
                break
        for i in range(pos-1, -1, -1):
            if req in blocks[i].keys() and blocks[i][req] is True:
                temp.append(pos-i)
                break
        if len(temp) > 1:
            dist = min(temp)
        elif len(temp) == 1:
            dist = temp[0]
        else:
            dist = 10000000000  # Consider it infinity, if there is no required building in block

    return dist


# Main function which will return the result
def find_apartment(blocks, requirements):
    block_dist = []
    for i in range(len(blocks)):
        block_dist.append([])
        for key, value in blocks[i].items():
            if value is True and key in requirements:
                block_dist[i].append(0)
            else:
                if key in requirements:
                    dist = find_distance(key, blocks, i)
                    block_dist[i].append(dist)

    help_list = []
    for i in block_dist:
        help_list.append(max(i))

    min_dist = min(help_list)
    return help_list.index(min_dist)  # Returning the index from blocks list


print(find_apartment(blocks, requirements))





