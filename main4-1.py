import qrcode # 01. 라이브러리를 불러옵니다.

qr_data = 'www.naver.com' #qr_data 변수에 'www.naver.com' 문자열을 바인딩한다.
qr_img = qrcode.make(qr_data) #qrcode.make로 이미지를 만들어 qr_img 변수에 바인딩한다.

save_path = '4. QR코드 생성기\\' + qr_data + '.png' #save_path변수에 저장될 경로를 바인딩한다. [4. QR코드 생성기] 폴더의 www.naver.com.png 로 저장됩니다.
qr_img.save(save_path) #이미지를 저장한다.