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

def filter_by_name(spots, name) : # name 키워드로 필터링
    return [spot for spot in spots if name in spot.get('name')]

def filter_by_city(spots, city) : # city 키워드로 필터링
    return [spot for spot in spots if city in spot.get('city')]

def filter_by_district(spots, district) : #district 키워드로 필터링
    return [spot for spot in spots if district in spot.get('district')]

def filter_by_ptype(spots, ptype) : #ptype 키워드로 필터링
    return [spot for spot in spots if ptype in spot.get('ptype')]

def filter_by_location(spots, locations) : #locations 키워드로 필터링
    min_lat, max_lat, min_long, max_long = locations
    return [spot for spot in spots if min_lat < float(spot.get('latitude')) < max_lat and min_long < float(spot.get('longitude')) < max_long] # 대소비교를 위해 float로 형변환

def sort_by_keyword(spots, keyword) : #keyword로 sort, sorted와 lambda 활용
    return sorted(spots, key=lambda spot: spot.get(keyword))

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