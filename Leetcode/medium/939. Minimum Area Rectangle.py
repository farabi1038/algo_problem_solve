class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        points.sort()
        map_dict ={}
        min_value= float('inf')
        y_pair={}
        for point in points:
            if point[0] not in map_dict:
                map_dict[point[0]]=[point[1]]
            else:
                map_dict[point[0]].append(point[1])   
        for key, value in map_dict.items():
            value.sort()
            for i in range(len(value)):
                for j in range(i+1, len(value)):
                    temp_pair =(value[i],value[j])
                    if temp_pair in y_pair:
                        prev_x = y_pair[temp_pair]
                        area= (key-prev_x)*(temp_pair[1] - temp_pair[0])
                        min_value =min(area,min_value)

            
                    y_pair[temp_pair]=key
        return min_value if min_value !=float('inf') else 0    