# SSD 논문 분석

담당: 김민기

----

## 0. 개요

## [ 1 ] 논문 분석 규칙

* (1) figure의 경우   
    + (1-1) '시각적 자료'를 분석한다.   
    + (1-2) 자료 하단의 '설명'을 분석한다.   

* (2) 참고 문헌과 비교하며 분석해야 한다.   

* (3) 분석이 이해가 가지 않는 경우   
    + (3-1) 이해가 가지 않음을 빠르게 수긍한다.   
    + (3-2) 기호를 표시한다.   
    + (3-3) 문단 끝에 기호, n 페이지-n 번째 줄 임을 표기한다.   
    + (3-3) 후에 이해가 가는 경우,   
    내용을 추가하거나 새로운 문서에서 보충 설명을 추가한다.   

## [ 2 ] 논문 분석 순서

* (1) 논문의 figure를 분석한다.   
    + (1-1) figure 중 '모델의 구조'를 분석한다.   
    + (1-2) 여타 figure들을 분석한다.   

* (2) 논문의 구성 순서대로 분석한다.   

----

## 1. 모델 구조 확인

### [ 1 ] Fig 2. single shot detection 모델의 비교 SSD vs YOLO [5].

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/model_structure.JPG "Model Structures")

### * 시각 자료 분석

* 좌측 기준으로 순서대로 진행해보면
    + (1) input 이미지   
    + (2) 'VGG-16 모델'과 5개의 풀링 계층   
    + (3) 여러 사이즈의 합성곱 계층들   
        - (3-1) 화살표; 분류기(합성곱 연산)
    + (4) 탐지 결과: 클래스 당 8732 오브젝트 탐지 (?)   
    + (5) Non-Maximum Suppression (?)등을 나타냄을 알수 있다. 그리고, YOLO는 분석에서 제외했다.

    + (?) 클래스 당 8732 오브젝트 탐지 - 8732 per Class, Non-Maximum Suppression

### * 설명 분석

> Fig. 2. A comparison between two single shot detection models: SSD and YOLO [5]. Our SSD model adds several feature layers to the end of a base network, which predict the offsets to default boxes of different scales and aspect ratios and their associated confidences. SSD with a 300 × 300 input size significantly outperforms its 448 × 448 YOLO counterpart in accuracy on VOC2007 test while also improving the speed.

* '모델 구조' 시각 자료에 대한 설명으로
    + (1) SSD 모델은 '기반 네트워크'의 끝에 '여러 특성 계층들'을 추가했다.
    + (2) 이 특성 계층들은 "서로 다른 '크기', '종횡비' 그리고 '활성'의 '기본 박스들(?)'에 대한 '위치 좌표(?)'를 예측한다.
    + (3) SSD는 300 x 300 의 input size를 받는다.   

* 이후 내용은 YOLO와 비교하는 내용이다.   

    + (?) 기본 박스들-default boxes, 위치 좌표-offset

### * 종합 분석

> * SSD는 '기본 네트워크'에 여러 특성 게층들을 추가했다고 언급되었다. 모델 시각 자료를 확인해 보았을 때, 'VGG-16'을 사용했음을 알 수 있는데, 이 VGG-16 모델이 기본 네트워크가 되는 것으로 추정된다.
> * 또한, VGG-16 모델 이후에 여러 '합성곱 계층들'이 보이는데, 이 계층들이 설명 분석에서 언급된 '특성 계층들'로 '기본 박스들'에 대한 위치 좌표를 예측하는 역할을 하는 것으로 추정된다.

----

## 2. 여타 figure들 분석

### [ 1 ] Fig. 1. SSD framework

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/Fig01_SSD_framework.JPG "Fig. 1. SSD framework")

### * 시각 자료 분석

* (a) Image with GT boxes
    + (1) 이미지에 개와 고양이가 나타나 있다.
    + (2) '개'는 '빨간색' 박스가 씌워져 있다.
    + (3) '고양이'는 '파란색' 박스가 씌워져 있다.
    
* (b) 8 x 8 feature map
    + (1) 8 x 8 특성 맵이다.
    + (2) 2 개의 '박스 뭉치'들이 존재한다.
    + (3) 박스 뭉치들은 여러 개의 '점선 박스'들로 이루어져 있다.
    + (4) 좌측 하단의 박스 뭉치 내에 '파란색' 점선 박스들이 몇개 있다.
    
* (c) 4 x 4 feature map
    + (1) 4 x 4 특성 맵이다.
    + (2) 1개의 박스 뭉치가 존재한다.
    + (3) 박스 뭉치는 여러개의 점선 박스들로 이루어져있다.
    + (4) 박스 뭉치 내에 '빨간색' 점선 박스가 존재한다.
    + (5) 수식이 보인다.
        loc : delta(cx, cy, w, h)
        conf: (c1, c2, ..., cp)

### * 설명 분석

> (a) SSD only needs an input image and ground truth boxes for each object during training. In a convolutional fashion, we evaluate a small set (e.g. 4) of default boxes of different aspect ratios at each location in several feature maps with different scales (e.g. 8×8 and 4×4 in (b) and (c)). For each default box, we predict both the shape offsets and the confidences for all object categories ((c1, c2, ··· , cp)). At training time, we first match these default boxes to the ground truth boxes. For example, we have matched two default boxes with the cat and one with the dog, which are treated as positives and the rest as negatives. The model loss is a weighted sum between localization loss (e.g. Smooth L1 [6]) and confidence loss (e.g. Softmax).

* 'Fig. 1. SSD framework'에 대한 설명으로
    + (1) '(a) Image with GT boxes' 자료의 의미는 
        - (1-1) SSD는 학습에 '이미지'와
            탐색하고자 하는 객체들에 '직접 씌운 박스'들을 
            필요로 한다.('실측 박스'라고 부르겠음)
    + (2) 합성곱 방법으로는
        - (2-1) 기본 박스들은 보통 적은 수(예, 4개 정도)의 뭉치이다. 그리고 각기 서로 다른 종횡비를 가진다.
        - (2-2) 서로 다른 크기의 특성 맵(예, (b) 8x8, (c) 4x4)내에 기본 박스들 뭉치가 존재한다.
    + (3) 각각의 기본 박스들은 '형상 좌표(?)'와 모든 객체 범주들을 위한 '활성'들(c1, c2, ... , cp) 둘 모두를 예측한다.
    + (4) 학습할 때, 먼저 이러한 기본 박스들(박스 뭉치들)을 실측 박스들과 맞춰본다.
    + (예시) 두 개의 박스 뭉치들을 하나는 고양이, 하나는 개에 맞춰보았다. '대응'되는 부분은 '양수', 대응되지 '않는' 부분은 '음수'로 취급한다.
    + (5) 모델의 손실은 '위치 손실(예, Smooth L1 [6])'과 '활성 손실(예, Softmax)' 간의 합이다.

### * 종합 분석

> * SSD는 학습을 위해 2가지 요소가 필요하다. 하나는 '이미지'이고, 다른 하나는 이미지 내에 탐지를 목표로 하는 객체들을 둘러싸는 '박스'들이다. 이 박스들은 '실측 박스'라고 부르기로 했다.
> * 객체를 탐지하는 데에 또 다른 박스 종류가 필요하다. 이는 '박스 뭉치'로 여러개의 다양한 크기, 종횡비, 활성값들을 가지는 기본(점선) 박스들로 이루어져 있다.
> * 객체를 탐지하는 데에 필요한 또 다른 요소는 '추가 특성 계층들'로 8x8, 4x4등 여러 단위의 특성 계층들이 추가된다.
> * 위에서 분석한 모델 구조와 Fig. 1.의 시각 자료를 바탕으로 고려해보았을 때, 여러 박스 뭉치들은 "추가된 특성 계층들 각각에 여러개가 존재"하는 것으로 추정된다. 즉, VGG-16 이후의 "특성 계층들의 크기와 단위가 다양한 것은 이러한 박스 뭉치들 자체의 크기와 단위도 다양하게 하기 위함"이라 추정된다.

----

### [ 2 ] Table 1. PASCAL VOC2007 test detection results

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/Table01_Pascal_VOC2007.JPG "Table 1. PASCAL VOC2007 test detection results")

### * 시각 자료 분석

* 표를 읽어보면
    + (1) Method, data, mAP, aero, bike, bird, boat, ... 등 20여 종의 데이터들이 기재되어 있음을 알 수 있다.
    + (2) Method 열에는 Fast [6], Faster [2], SSD300, SSD512 등 모델 명 등이 기재 되어 있다.
        - (2-1) 대괄호('[]')는 참고문헌 번호이다.
    + (3) data 열에는 07, 07+12, 07+12+COCO 등 조금 이해하기 난해한 데이터가 기재되어있다.
        - (3-1) 데이터셋 번호, 혹은 테스트 년도가 기재되어있는 것으로 추정된다.
    + (4) mAP 열(?)에는 십의 자리 실수들이 기재되어있다.
        - (4-1) 정확도 혹은 평가 점수 등으로 추정된다.
    + (5) aero, bike, bird, boat, ...등의 열은 데이터 범주에 대한 열로 기재된 데이터들은 해당 범주에 대한 정확도로 추정된다.

    + (?) mAP(mean Average Precision): 
        - Precision: 정확도; 검출 결과들 중 옳게 검출한 비율
            - 식: Precision = TP / (TP+FP) = TP / All Detections
            - TP(True-Positive), FP(False-Positive), 반대 개념들도 존재하며, 베이지안 추론을 검색해보기 바란다.
        - Recall: 검출율(재현율); 실제 옳게 검출된 결과들 중 옳게 예측한 비율
            - 식: Recall = TP / (TP + FN) = TP / All Ground truths
        - Precision과 Recall의 관계:
            - 일반적으로 반비례한다.
            - 'Precision-Recall 곡선'으로 한눈에 확인한다.
            - 어떤 알고리즘의 성능을 전반적으로 파악하기에는 좋으나, 다른 알고리즘과 정량적으로 비교하기에는 불편한 점이 많다.
        - AP(Average Precision): 인식 알고리즘의 성능을 하나의 값으로 표현한 것
            - 'Precision-Recall 그래프'의 아래쪽 면적(적분)으로 계산된다.
            - 컴퓨터비전 분야의 물체인식 알고리즘 성능 대부분이 AP로 평가된다.
        - mAP(mean Average Precision):
            - 물체의 클래스가 여러 개인 경우, 각 클래스당 AP를 구한 후, 총합하여 클래스의 개수로 나눈 값이다.
        - (참고) https://ctkim.tistory.com/79

### * 설명 분석

> Both Fast and Faster RCNN use input images whose minimum dimension is 600. The two SSD models have exactly the same settings except that they have different input sizes (300 × 300 vs. 512 × 512). It is obvious that larger input size leads to better results, and more data always helps. Data: “07”: VOC2007 trainval, “07+12”: union of VOC2007 and VOC2012 trainval. “07+12+COCO”: first train on COCO trainval35k then finetune on 07+12.

* 'Table 1. PASCAL VOC2007 test detection results.'에 대한 설명으로
    + (1) Fast R-CNN 과 Faster R-CNN 둘 다 최소 600 치수(?)의 input이미지들을 사용한다.(이미지 사이즈가 600 x 600 으로 추정된다.)
    + (2) 2개의 SSD 모델은 input 사이즈들을 제외하고 정확히 같은 세팅값으로 설정되어있다.
        - (예) SSD300 = 300 x 300 input 이미지를 사용한다.
    + (3) Data 열의
        - (3-1) "07"은 "VOC2007 trainval 데이터 셋"을 의미한다.
        - (3-2) "07 + 12"는 "VOC2007과 VOC2012 통합 trainval 데이터셋"을 의미한다.
        - (3-3) "07 + 12 + COCO"는 "먼저 COCO trainval135k 데이터셋으로 학습을 진행한 후 '07 + 12'(3-2)로 fine_tune(미세 조정)을 진행한 것이다.
        - (참고) https://rain-bow.tistory.com/entry/Object-Detection-Object-Detection-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-Implementation 
    + (4) input 크기가 클수록 더 좋은 결과를 내는 것, 그리고 데이터가 더 많을 수록 항상 도움이 된다는 것이 명백해졌다.

    + (?) 치수-dimension

### * 종합 분석

> * 해당 표는 SSD의 훈련 성능에 대한 표이다. 그리고 Fast R-CNN, Faster R-CNN과 비교했을 때, 더 좋은 성능을 내는 것을 확인할 수 있다.
> * SSD-300과 SSD-512를 data: 07 별로 비교했을 때, SSD-300의 mAP는 68.0, SSD-512의 mAP는 71.6 이고, data: 07+12 별로 비교했을 때, SSD-300의 mAP는 74.1, SSD-512의 mAP는 76.8 등 input 이미지의 크기가 클수록 더 좋은 결과를 도출해냄을 알 수 있다.
> * 표 전반적으로 어떤 모델이든 상관없이 살펴 보았을 때, data: 07과 data: 07+12를 비교해보면, mAP의 값들이 07+12 일 경우가 더 높음을 알 수 있다. 즉, input 데이터의 개수가 많을 수록 성능이 향상됨을 알 수 있다.

### [ 3 ] Fig. 3. Visualization of performance for SSD 512 on animals, vehicles, and furniture from VOC2007 test using[19]

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/Fig03_Visual_performance.JPG "Fig. 3. Visualization of performance for SSD 512 on animals, vehicles, and furniture from VOC2007 test using")

### * 시각 자료 분석

* VOC2007 테스트에서 사용된 SSD 512 모델의 성능 도표들로서
    + (1) animals, vehicles, furniture 범주들에 대한 성능 도표로 확인된다.
    + (2) 성능 도표들 중 첫번 째 행을 분석해 보았을 때,
        - (2-1) 도표의 x축은 '총 인식된 object들의 수(?)'를 나타내는 것으로 추정할 수 있다. '(x 357)', '(x 415)' 등으로 적힌 것으로 보아 357개, 415개의 객체들이 인식된 것으로 보인다.
        - (2-2) 도표의 y축은 '각 유형별 퍼센트(?)'를 나타내는 것으로 추정할 수 있다. 퍼센트임으로 0 에서 100까지의 수치가 기입되어 있다.
        - (2-3) 전반적으로 빨간색 실선과 점선이 가파르게 상승하는 형태로 보인다. 점선은 예상한 성능의 향상 정도를, 실선은 실제로 측정된 성능의 향상 정도를 보여주는 것으로 추정된다.
        - (2-4) 아직 정확한 의미를 알 수 없지만, 도표 우하단의 Cor, Loc, Sim, Oth, BG 등 도표 내 면적의 색에 대한 설명이 나타나있다.
    + (3) 성능 도표들 중 두번 째 행을 분석해 보았을 때,
        - (3-1) 도표의 x축은 '총 FP 수치'로 25 부터 3200까지 나타내었음을 알 수 있다.
        - (3-2) 도표의 y축은 '각 유형별 퍼센트(?)'를 나타내는 것으로 추정된다. 0에서 100까지의 수치가 나타나있다.
        - (3-3) 이번 도표들 또한 Loc, Sim, Oth, BG 등 아직 알 수 없는 의미의 면적과 그에 대한 색을 나타낸다.

    + (?) 총 인식된 object들의 수-total detections, 각 유형별 퍼센트-percentage of each type

### * 설명 분석

* VOC2007 테스트에서 사용된 SSD 512 모델의 성능 도표들에 대한 설명으로
    + (1) 첫 행은 인식들의 여러 부분들을 통합해 나타낸다.
        - (1-1) Cor: 올바른 인식
        - (1-2) Loc: 약한(박한) 지역화로 인한 FP(?)
        - (1-3) Sim: 비슷한 범주들과 혼동한 정도
        - (1-4) Oth: 다른 것들과 혼동한 정도
        - (1-5) BG: 배경과 혼동한 정도
    + (2) 둘째 행은 가장 높게 측정된 FP 유형들을 분류해 나타낸다.

### * 종합 분석

> * 해당 도표들은 VOC2007 테스트에서 사용되었음을 상기해야한다. VOC2007 데이터셋들은 총 20종의 범주를 제공한다. 따라서,
>> + 'animals 범주'는 bird, cat, cow, dog, horse, person, sheep 등 7개의 범주들을 내포하고 있다.
>> + 또한, 'vehicles 범주'는 aero, bike, boat, bus, car, mbike, train 등 7개의 범주들을 내포하고 있다.
>> + 마지막으로, 'furniture 범주'는 bottle, chair, table, plant, sofa, tv 등 6개의 범주들을 내포하고 있음을 기억해야한다.
> * animals 열 마지막 행 도표를 보았을 때, Loc과 Sim의 면적이 매우 큰 것으로 보아 비슷한 범주들(bird, cat, cow, ...)과 많이 혼동했고 약한 지역화 문제가 크게 발생했음을 알 수 있다.
> * vehicles 열 마지막 행 도표를 보았을 때, Loc 면적이 매우 큰 것을 볼 수 있다. 이는, 약한 범주화 문제가 제일 크게 발생한 경우이다.
> * furniture 열의 마지막 행 도표를 보았을 때, 각 유형별 범주들이 비슷한 면적을 가지는 것을 보인다. 어쩌면, FP의 정도가 가장 골고루 나타나는 것으로 보인다.
> * 세 열을 좌측부터 순서대로 보았을 때, 총 인식 수를 고려하고 보아도, furniture의 FP 면적이 제일 크게 나타나는 것을 볼 수 있다. 또한, 세 도표들 중 빨간 실선이 가장 완만하게 상승한다.
> * 아직, 도표들에 대한 의미를 이해하기는 어려우므로 본문을 읽기 전까지는 어떻게 구성되어있는지만 기억하도록 하자.