Windows 환경에서 1sec Live Stream 확인을 위함

## NOTICE
- test.py는 samples 폴더에 있는 output.pcap의 패킷 갯수 상관없이 추론 진행
- 1 패킷 샘플이면, 그냥 추론결과 출력
- 여러 패킷 샘플이면, 모든 패킷 추론결과에서 다수결 투표로 출력
- 오직 이 git만 들어갈 수 있게 폴더 새로 만들어서 하는 거 추천

## 구성
- models: 학습된 모델 저장할 폴더
   - 0720_with_outlier_1.pth: 0720 sample 사용한 Acc 92.5% 모델
   - 0810_test.pth: 0810 sample 사용한 Acc 79% 모델
   - 0810_test_1.pth: 0810 sample 사용한 Acc 90% 모델
- samples: 추론할 샘플 저장할 폴더
- test.py: 라이브스트림 테스트용

## 순서
  1. 폴더 하나 만들고 폴더 안에서 우클릭-git bash
  
  2. git clone https://github.com/ChoiSeu/Test4Windows.git

  3. samples 폴더에 통신 코드 넣고 output.pcap으로 생성되게 하기

  4. test 코드에서 28번째 줄, 사용할 모델로 수정

  5. 라이브 스트림 테스트 진행
