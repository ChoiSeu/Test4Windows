Windows 환경에서 1sec Live Stream 확인을 위함

### NOTICE
 : test_1packet.py는 1packet캡처된 샘플용
   test_more.py는 2packet 이상 캡처된 샘플용
   오직 이 git만 들어갈 수 있게 폴더 새로 만들어서 하는 거 추천

### 구성


### 순서
# 1. git clone https://github.com/ChoiSeu/Test4Windows.git

# 2. model

# 3. 'a' 누르면 수정 모드
=> ADDRESS랑 FILE 부분 맞게 수정
=> ADDRESS: 연결할 ip주소
=> FILE: 주고받을 파일 이름(원래는 입력받게 해놨는데 미리 정하게 해놓음. default는 output.pcap)

# 4. esc 누르고 ':wq' 하면 저장하고 종료

# 5. make clean

# 6. make run

## +) 추론하는 샘플은 /samples에 있는 test_sample로 고정되어있음
##    터미널에서 예측결과가 출력되면서 소켓통신이 되는지만 확인하면 됨

