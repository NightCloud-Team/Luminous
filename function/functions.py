def remove_duplicates_but_keep_specific(lst, keep_list):
    result = []
    seen = set()
    
    for item in lst:
        # 如果该元素在需要保留的列表中，直接添加
        if item in keep_list:
            result.append(item)
        # 如果该元素不在需要保留的列表中，并且它还没被添加到结果中
        elif item not in seen:
            result.append(item)
            seen.add(item)
    
    return result