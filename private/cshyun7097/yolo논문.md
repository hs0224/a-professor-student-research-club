# YOLO (You Only Look Once)
## YOLO 논문 리뷰1(https://bkshin.tistory.com/entry/%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0-YOLOYou-Only-Look-Once)
### ABSTRACT
- 다른 객체 검출과는 다르게 새로운 접근 방식을 적용
- 기존의 multi-task 문제를 하나의 회귀 문제로 정의
- 이미지 전체에 대해서 하나의 신경망이 한 번의 계산만으로 bounding box와 클래스 확률(class probability)를 예측
- 객체 검출 파이프라인이 하나의 신경망으로 구성되어 있으므로 end-to-end 형식이다.
- YOLO의 통합된 모델은 굉장히 빠름

### 1. Introduction
- 기존의 검출 모델은 분류기를 재정의하여 검출기를 사용 ---> 분류: 이미지를 보고 개인지 고양이인지 판단하는 것
- 객체 탐지는 하나의 이미지에서 개는 어느 위치에 있고, 고양이는 어느 위치에 있는지에 대한 위치 정보도 판단해야 함
    ex) DPM, R-CNN
- DPM(Deformable Parts Modesl)
    - 이미지 전체를 거쳐 슬라이딩 윈도방식으로 객체 검출을 하는 모델
- R-CNN
    - 이미지 안에서 bounding box를 생성하기 위해 region proposal이라는 방법을 사용
    - bounding box에 classifier를 적용하여 분류하고 bounding box를 조정하고, 중복된 검출을 제거하고, 객체에 따라 box의 점수를 재산정하기 위해 후처리 실시
    - 복잡하기 때문에 속도가 느리며 각 절차를 독립적으로 훈련시켜야 하므로 최적화(optimization)하기가 힘듬
- YOLO(You Only Look Once)
    - 객체 검출을 하나의 회귀 문제로 보고 절차를 개선
    이미지의 픽셀로부터 bounding box의 위치, 클래스 확률을 구하기까지의 일련의 절차를 하나의 회귀 문제로 재정의
    - 이미지 내에 어떤 물체가 있고 그 물체가 어디에 있는지를 하나의 파이프라인으로 빠르게 구한다.
    - 이미지를 한 번만 보면 객체를 검출할 수 있다 하여 이름이 YOLO 임

## YOLO의 장점
- 1. 굉장히 빠르다
    - 기존의 복잡한 객체 검출 프로세스를 하나의 회귀문제로 바꾸었기 때문에 기존의 객체 검출 모델처럼 복잡한 파이프라인이 필요 없음
    - YOLO의 기본 네트워크는 Titan X GPU 에서 배치 처리 없이 1초에 45프레임을 처리하며 빠른 버전의 YOLO는 1초에 150 프레임을 처리 ==> 동영상을 실시간으로 처리 가능하다.
- 2. 예측을 할 때 이미지 전체를 본다.
    - 슬라이딩 윈도우나 region proposal 방식과 달리 YOLO는 훈련과 테스트 단계에서 이미지 전체를 본다.
    - 클래스의 모양에 대한 정보뿐만 아니라 주변 정보까지 학습하여 처리가능
    - 이미지 전체를 처리하기 때문에 background error가 이전 모델인 Fast R-CNN에 비해 훨씬 적음(대략 1/2 가량)
- 3. YOLO는 물체의 일반적인 부분을 학습한다.
    - 일반적인 부분을 학습하기 때문에 자연 이미지를 학습하여 그림 이미지로 테스트할 때, YOLO의 성능은 DPM이나 R-CNN보다 월등히 뛰어남
- 하지만 최신 객체 검출 모델에 비해 정확도가 다소 떨어진다는 단점이 있음 -> 빠르게 객체를 탐지할 수 있다는 장점과 정확도가 다소 떨어진다는 단점


### 2. Unified Detection
- YOLO는 객체 검출의 개별 요소를 단일 신경망으로 통합한 모델로 bounding box를 예측하기 위해 이미지 전체의 특징을 활용 -> 이러한 디자인 덕분에 높은 정확성을 유지하며 end-to-end 학습과 실시간 객체 검출이 가능
- 입력 이미지를 S * S 그리드로 나누고 만약 어떤 객체의 중심이 특정 그리드 셀 안에 위치한다면, 그 그리드 셀이 해당 객체를 검출해야함.
- 각각의 그리드 셀은 B개의 bounding box와 그 bounding box에 대한 confidence score를 예측
    - confidence score = bounding box가 객체를 포함한다는 것을 얼마나 믿을만한지, 그리고 예측한 bounding box가 얼마나 정확한지를 나타냄
    - Pr(Object) = IOU(truth/pred) (IOU = intersection over union -> 객체의 실제 bounding box와 예측 bounding box의 교집합) / (실제 bounding box와 예측 bounding box의 합집합)
    - Pr(object) = 1일 때가 가장 이상적
- bounding box는 5개의 예측치로 구성 -> x, y, w, h, confidence
    - (x, y) = bounding box 중심의 그리드셀 내 상대 위치 -> 0 ~ 1 사이의 값 / 만약 그리드 셀 정가운데일 경우 (0.5, 0.5)
    - (w, h) = 이미지 전체의 너비와 높이를 1이라고 했을 때, bounding box의 너비와 높이가 몇인지를 상대적인 값으로 나타낸 것 -> 0 ~ 1 사이의 값
    - confidence = confidence score
- YOLO 연구진은 파스칼 VOC라는 이미지 인식 국제대회 데이터 셋을 이용해 실험
    - S = 7, B = 2, C = 20
    - S = 7 이므로 input 이미지는 7 * 7 그리드로 나뉨
    - B = 2 이므로 하나의 그리드 셀에서 2개의 bounding box를 예측하겠다는 뜻
    - C = 20 은 총 20개의 라벨링 된 클래스가 있다는 뜻
    - -> S * S * (B * 5 + C) 텐서 생성

## 2.1 Network Design
- YOLO 모델을 하나의 CNN 구조로 디자인 -> 앞단은 컨볼루션 계층, 이어서 전결합 계층으로 구성
    - 컨볼루션 계층은 이미지로부터 특징을 추출
    - 전결합 계층은 클래스 확률과 bounding box의 좌표를 예측
- YOLO의 신경망 구조는 이미지 분류에 사용되는 GoogLeNet에서 따옴 -> GoogLeNet의 인셉션 구조 대신 YOLO는 1 * 1 축소 계층과 3 * 3 컨볼루션 게층의 결합을 사용

## 2.2 Training
- 1. 1,000개의 클래스를 갖는 ImageNet 데이터 셋으로 YOLO의 컨볼루션 계층을 사전훈련 시행
    - 사전훈련을 위해 24개의 컨볼루션 계층 중 첫 20개의 컨볼루션 계층만 사용, 이어서 전결합 계층 연결 -> 1주간 훈련
    - ==> 88%의 정확도를 기록
- YOLO 연구진은 이 모든 훈련과 추론을 위해 Darknet 프레임워크 사용
    - Darknet 프레임워크 : YOLO를 개발한 Joseph Redmon이 독자적으로 개발한 신경망 프레임워크로 신경망들을 학습하거나 실행할 수 있는 프레임워크다.
    - YOLO도 Darknet에서 학습된 모델 中 하나
- ImageNet = 분류를 위한 데이터 셋으로 사전 훈련된 분류 모델을 객체 검출 모델로 바꿔야 함
- YOLO 연구진은 20개의 컨볼루션 계층 뒤 4개의 컨볼루션 계층 및 2개의 전결합 계층을 추가하여 성능을 향상 + 이 계층의 가중치는 임의로 초기화
- 객체 검출을 위해서는 이미지 정보의 해상도가 높아야 함 -> 해상도를 224 * 224 -> 448 * 448로 증가
- 이 신경망의 최종 OUTPUT = 클래스 확률 + bounding box 위치정보(너비, 높이, 중심좌표)
- YOLO 신경망의 마지막 계층에는 선형 활성화 함수를 적용하고 나머지 모든 계층에서는 leaky ReLU를 적용
    - ReLU는 0이하의 값은 모두 0인데 비해 leaky ReLU는 0 이하의 값도 작은 음수 값을 갖는다.
- YOLO의 loss = SSE를 기반으로 하기 때문에 최종 Output의 SSE를 최적화 해야 한다
    - SSE를 사용한 이유 : 최적화하기 쉽기 때문이지만 YOLO의 최종 목적인 mAP(평균 정확도)를 높이는 것과 완벽하게 일치하지는 않음
- YOLO의 loss
    - localization loss : bounding box의 위치를 얼마나 잘 예측했는지에 대한 loss
    - classification loss : 클래스를 얼마나 잘 예측했는지에 대한 loss
    - 이 두 손실의 가중치를 동일하게 두고 학습하는 것은 좋은 방법이 아니지만 SSE를 최적화하는 방식은 이 두 loss의 가중치를 동일하게 취급
- 문제
    - 이미지 내 대부분의 그리드 셀에는 객체가 없음 -> 배경 영역이 전경 영역보다 더 크기 때문
        - 그리드 셀에 객체가 없다면 confidence score = 0 이다.
        - 따라서 대부분의 그리드 셀의 confidence score = 0이 되도록 학습할 수 밖에 없는데 이는 모델의 불균형을 초래
    - 이를 개선하기 위해 객체가 존재하는 bounding box 좌표에 대한 loss의 가중치를 증가시키고, 객체가 존재하지 않는 bounding box의 confidence loss에 대한 가중치는 감소
    - 이를 위해 두 파라미터를 사용
        - 入_coord = 5, 入_noobj = 0.5로 가중치
    - bounding box의 너비와 높이에 square root를 취해준 값을 loss function으로 사용
- 과적합을 막기 위해 드롭아웃과 data augmentation을 적용

## 2.3 Inference
- 추론 단계에서도 훈련 단계와 마찬가지로 테스트 이미지로부터 객체를 검출하는 데에는 하나의 신경망 계산만 하면 됨.
- 파스칼VOC 데이터 셋에 대해서 YOLO는 한 이미지 당 98개의 bounding box를 예측해주고, 그 bounding box마다 클래스 확률을 구해준다.
    - YOLO는 테스트 단계에서 굉장히 빠름 -> R-CNN 등과 다르게 하나의 신경망 계산만 필요하기 때문
### YOLO의 그리드 디자인의 단점
- 하나의 객체를 여러 그리드 셀이 동시에 검출하는 경우가 있다
    - 객체의 크기가 크거나 객체가 그리드 셀 경계에 인접해 있는 경우, 그 객체애 대한 bounding box가 여러개 생길 수 있음
    - => 하나의 그리드 셀이 아닌 여러 그리드셀에서 해당 객체에 대한 bounding box를 예측할 수 있다
- 이러한 문제를 다중 검출 문제라고 하며 이 문제는 비 최대 억제라는 방법을 통해 개선할 수 있음 -> mAP를 2~2%가량 향상

## 2.4 Limitations of YOLO
- YOLO는 하나의 그리드 셀마다 두 개의 bounding box를 예측 + 하나의 그리드 셀마다 오직 하나의 객체만 검출 => 공간적 제약을 야기
    - 공간적 제약 : 하나의 그리드 셀은 오직 하나의 객체만 검출하므로 하나의 그리드 셀에 두 개 이상의 객체가 붙어있다면 이를 잘 검출하지 못하는 문제
- 데이터로부터 bounding box를 예측하는 것을 학습하기 때문에 훈련 단계에서 학습하지 못했던 새로운 종횡비를 마주하면 고전함
- YOLO모델은 큰 bounding box와 작은 bounding box의 loss에 대해 동일한 가중치를 둔다는 단점 존재
    - 큰 bounding box는 위치가 약간 달라져도 비교적 성능에 별 영향을 주지 않지만 크기가 작은 bounding box는 위치가 조금만 달라져도 성능에 큰 영향을 줌
    - 큰 bounding box에 비해 작은 bounding box가 위치 변화에 따른 IOU 변화가 더 심하기 때문 = localization 문제
