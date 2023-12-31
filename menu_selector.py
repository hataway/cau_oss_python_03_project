import file_manager
import parking_spot_manager

def start_process(path):
    str_list = file_manager.read_file(path) #path 경로로 파일을 읽어와 리스트 생성
    spots = parking_spot_manager.str_list_to_class_list(str_list)
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1: # 전체 목록 출력
            parking_spot_manager.print_spots(spots)
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1: # name으로 필터링
                keyword = input('type name:')
                spots = parking_spot_manager.filter_by_name(spots, keyword)
            elif select == 2: # city로 필터링
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword)
            elif select == 3: # district로 필터링
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword)
            elif select == 4: # ptype으로 필터링
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword)
            elif select == 5: # locations으로 필터링
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                keyword = (min_lat,max_lat,min_lon,max_lon)
                spots = parking_spot_manager.filter_by_location(spots, keyword)
            else:
                print("invalid input")
        elif select == 3: # keyword로 sorted
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                spots = parking_spot_manager.sort_by_keyword(spots, keyword)
            else: print("invalid input")
        elif select == 4: # Exit를 출력하고 종료
            print("Exit") 
            break
        else:
            print("invalid input")