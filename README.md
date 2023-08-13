Offline data 테스트용

## NOTICE
 : test_1packet.py는 1packet캡처된 샘플용
   test_more.py는 2packet 이상 캡처된 샘플용
   오직 이 git만 들어갈 수 있게 폴더 새로 만들어서 하는 거 추천

## 구성
- models
   - 0720_with_outlier_1.pth: 0720 sample 사용한 Acc 92.5% 모델
   - 0810_test.pth: 0810 sample 사용한 Acc 79% 모델
   - 0810_test_1.pth: 0810 sample 사용한 Acc 90% 모델
- samples: 그냥 측정했던 sample들
- test_1packet.py: 1 packet sample 테스트 용
- test_more.py: 2 packet 이상 캡처된 sample 테스트 용

## 순서
  1. 폴더 하나 만들고 git clone https://github.com/ChoiSeu/Test4Windows.git

  2. samples 폴더에 원하는 샘플, models에 원하는 모델 넣기

  3. 캡처한 packet 수에 맞는 test 코드 선택 후, sample 날짜 수정 및 모델 수정

  4. python3 <사용할 test 코드명> <test할 동작명>
