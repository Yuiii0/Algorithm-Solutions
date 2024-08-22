def solution(wallpaper):
    files_pos=set()
    for idx,file in enumerate(wallpaper):
        file_idx=file.find('#')
        if file_idx!=-1:
            files_pos.add((idx,file_idx))
            files_pos.add((idx,file.rfind('#')))


    x_values=[x for x,y in files_pos]
    y_values=[y for x,y in files_pos]


    return [min(x_values),min(y_values),max(x_values)+1,max(y_values)+1]


