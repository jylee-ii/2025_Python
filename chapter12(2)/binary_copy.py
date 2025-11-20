source_file=input("원본 파일 이름을 입력하시오: ")
destination_file=input('복사 파일 이름을 입력하시오: ')

with open(source_file,'rb') as source:
    with open(destination_file,'wb') as destination:
        while True:
            chunk = source.read(16)
            if not chunk:
                break
            
            print(f"복사중 데이터(16 bytes): {chunk}")

            destination.write(chunk)

print(f"\n{source_file}를 복사하여 {destination_file}로 저장했습니다.")