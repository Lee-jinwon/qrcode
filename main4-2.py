import qrcode

file_path = r'4. QR코드 생성기\qr코드모음.txt' # [4. QR코드 생성기] 폴더에 [qr코드모음.txt] 파일을 읽는다. 
with open(file_path, 'rt', encoding='UTF8') as f : # f.readlines()로 파일을 읽어 줄 별로 리스트의 값의 형태로 내어준다. read_lines에는 줄별로 읽힌 값이 리스트 형태로 바인딩 된다.
    read_lines = f.readlines()
    
    for line in read_lines: # 여러 개의 값을 읽기 위하여 for문을 사용하여 값을 읽는다.
        line = line.strip() # line.strip()은 줄 마지막에 줄바꿈 문자를 삭제한다.
        print(line) # 값을 출력한다.