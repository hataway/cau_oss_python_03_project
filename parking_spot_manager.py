class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    def __init__(self, name, city, district, ptype, longitude, latitude): # __item 필드 생성을 위한 생성자
        self.__item = {'name': name, 'city': city, 'district': district, 'ptype': ptype, 'longitude': longitude, 'latitude': latitude}
        
    def get(self, keword = 'name') : # get 메소드, 기본인수는 'name'
        return self.__item[keword]


def str_list_to_class_list (str_list):
    class_list = []; # parking_spot 클래스를 담을 새로운 리스트
    
    for item in str_list:
        arr = item.split(',') # ',' 단위로 쪼개서 저장
        class_list.append(parking_spot(arr[1], arr[2], arr[3], arr[4], arr[5], arr[6])) # arr[0]은 순번이라 arr[1]부터 저장

    return class_list
    
def print_spots(spots) :
    print("---print elements({})---".format(len(spots))) # 총 길이 출력
    for parking_spots in spots :
        print(parking_spots)

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)