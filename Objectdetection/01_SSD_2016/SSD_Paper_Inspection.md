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
        - (출처) https://ctkim.tistory.com/79

### * 설명 분석

> Both Fast and Faster RCNN use input images whose minimum dimension is 600. The two SSD models have exactly the same settings except that they have different input sizes (300 × 300 vs. 512 × 512). It is obvious that larger input size leads to better results, and more data always helps. Data: “07”: VOC2007 trainval, “07+12”: union of VOC2007 and VOC2012 trainval. “07+12+COCO”: first train on COCO trainval35k then finetune on 07+12.

* 'Table 1. PASCAL VOC2007 test detection results.'에 대한 설명으로
    + (1) Fast R-CNN 과 Faster R-CNN 둘 다 최소 600 치수(?)의 input이미지들을 사용한다.(이미지 사이즈가 600 x 600 으로 추정된다.)
    + (2) 2개의 SSD 모델은 input 사이즈들을 제외하고 정확히 같은 세팅값으로 설정되어있다.
        - (예) SSD300 = 300 x 300 input 이미지를 사용한다.
    + (3) Data 열의
        - (3-1) "07"은 "VOC2007 trainval 데이터셋"을 의미한다.
        - (3-2) "07 + 12"는 "VOC2007과 VOC2012 통합 trainval 데이터셋"을 의미한다.
        - (3-3) "07 + 12 + COCO"는 "먼저 COCO trainval135k 데이터셋으로 학습을 진행한 후 '07 + 12'(3-2)로 fine_tune(미세 조정)을 진행한 것이다.
        - (출처) https://rain-bow.tistory.com/entry/Object-Detection-Object-Detection-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-Implementation 
    + (4) input 크기가 클수록 더 좋은 결과를 내는 것, 그리고 데이터가 더 많을 수록 항상 도움이 된다는 것이 명백해졌다.

    + (?) 치수-dimension

### * 종합 분석

> * 해당 표는 SSD의 훈련 성능에 대한 표이다. 그리고 Fast R-CNN, Faster R-CNN과 비교했을 때, 더 좋은 성능을 내는 것을 확인할 수 있다.
> * SSD-300과 SSD-512를 data: 07 별로 비교했을 때, SSD-300의 mAP는 68.0, SSD-512의 mAP는 71.6 이고, data: 07+12 별로 비교했을 때, SSD-300의 mAP는 74.1, SSD-512의 mAP는 76.8 등 input 이미지의 크기가 클수록 더 좋은 결과를 도출해냄을 알 수 있다.
> * 표 전반적으로 어떤 모델이든 상관없이 살펴 보았을 때, data: 07과 data: 07+12를 비교해보면, mAP의 값들이 07+12 일 경우가 더 높음을 알 수 있다. 즉, input 데이터의 개수가 많을 수록 성능이 향상됨을 알 수 있다.

### [ 3 ] Fig. 3. Visualization of performance for SSD 512 on animals, vehicles, and furniture from VOC2007 test using [19]

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/Fig03_Visual_performance.JPG "Fig. 3. Visualization of performance for SSD 512 on animals, vehicles, and furniture from VOC2007 test using")

### * 시각 자료 분석

* [19] 참고 문헌을 이용한 VOC2007 테스트에서 사용된 SSD 512 모델의 성능 도표들로서
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

> The top row shows the cumulative fraction of detections that are correct (Cor) or false positive due to poor localization (Loc), confusion with similar categories (Sim), with others (Oth), or with background (BG). The bottom row shows the distribution of top-ranked false positive types.

* [19] 참고 문헌을 이용한 VOC2007 테스트에서 사용된 SSD 512 모델의 성능 도표들에 대한 설명으로
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

### [ 4 ] Fig. 4. Sensitivity and impact of different object characteristics on VOC2007 test set using [19]

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/Fig04_Sensitivity.JPG "Fig. 4. Sensitivity and impact of different object characteristics on VOC2007 test set using")

### * 시각 자료 분석

* [19]참고 문헌을 이용한 VOC2007 테스트에서 다른 객체 특성의 민감도와 영향에 대해 나타낸 도표들로
    + (1) 좌측 열에는 각 범주별 BBox 영역의 설정 정도를 나타낸다.
        - (1-1) y축이 0 부터 1까지 인것으로 보아, 정량적 비교를 위해 연산을 거친 수치들로 추측해 볼 수 있다.
        - (1-2) x축은 XS, S, M, L, XL 순으로 크기 단위를 나타내고 있다. 아마도, SSD 구조 상 여러 단위, 종횡비, 크기의 박스들을 이용하기 때문으로 보인다.
        - (1-3) 문제는, BBOX area가 '박스 뭉치의 크기'를 의미하는 것인지, '단일 기본 박스 크기'를 의미하는 것인지 아직 분간이 안된다는 것이다.
    + (2) 우측 열에는 각 범주별 종횡비를 나타낸다.
        - (2-1) y축이 좌측열과 똑같은 구성으로 확인된다.
        - (2-2) x축은 XT, T, M, WX, W 순으로 종횡비 단위를 나타내고 있다.

### * 설명 분석

> The plot on the left shows the effects of BBox Area per category, and the right plot shows the effect of Aspect Ratio.

* [19] 참고 문헌을 이용한 VOC2007 테스트에서 다른 객체 특성의 민감도와 영향에 대한 설명으로
    + (1) 좌측 열의 도표는 범주 별 BBox 영역의 영향을 보여준다.
    + (2) 우측열의 도표는 범주 별 종횡비의 영향을 보여준다.

### * 종합 분석

> * 좌측열은 범주별 BBox 영역 크기의 영향을, 우측열은 범주별 종횡비 단위의 영향을 보여준다.
> * 대부분 영역 크기와 종횡비 단위가 커질수록 1에 가까워지는 것을 확인할 수 있다. 그리고, 실선의 기울기 또한 낮아지기 시작한다.
>> * 이 기울기를 제목의 민감도로 추정했을 경우, 사이즈 혹은 종횡비가 커질 수록 민감도는 떨어진다고 해석해 볼 여지가 있다.
> * 범주 chair의 경우 영역 크기 L, 종횡비 단위 WX부터 급격하게 하향하는 것을 볼 수있다. 심지어는 SSD512 종횡비에서 0.54로 시작하던 실선이 0.42까지 추락하는 것을 확인할 수 있다.
>> * 민감도에 대한 추측에 따르면, 영역 크기 L, 종횡비 단위 M 혹은 WX부터 민감도가 급격히 줄어드는 것으로 확인된다. 개인적인 추측으로는 범주 table과 혼동하는 문제가 발생한 것이 아닌가 싶다.

### [ 5 ] Table 2. Effects of various design choices and components on SSD performance

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/Table02_Effects.JPG "Table 2. Effects of various design choices and components on SSD performance")

### 참고

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/Fig01_SSD_framework.JPG "Fig. 1. SSD framework")

### * 시각 자료 분석

* 다양한 SSD 모델 디자인과 컴포넌트 선택의 SSD 성능에 대한 영향 표로
    + (1) 첫 번째 행은 "더 많은 데이터 증가를 행할 것인가?" 라는 조건이고, 첫 번째 열에서는 선택하지 않았다.
        - (1-1) 데이터 증가(data augmentation)은 하나의 이미지 데이터를 확대, 축소, 회전, 일그러뜨리기 등 변형 작업을 통해 이미지 데이터들을 증가 시키는 방법이다.
    + (2) 두 번째 행은 "{1/2, 2} 박스를 포함하는가?" 라는 조건이다.
     두 번째 열에서 선택하지 않았다.
        - (2-1) {1/2, 2}는 기본 박스의 사이즈에 대한 옵션으로 추정된다. 즉, 해당 행을 사용하지 않는다면, 기본 박스의 1/2배 크기와 2배 크기의 박스들은 사용되지 않는 것으로 추측된다.
    + (3) 세 번째 행은 "{1/3, 3} 박스를 포함하는가?" 라는 조건이다.
    두 번째 열과 세 번째 열에서 선택하지 않았다.
        - (3-1) (2)에서와 마찬가지의 메커니즘을 가지는 것으로 추측된다.
    + (4) 네 번째 행은 "구멍 뚫린 구조(?)를 사용하는가?" 라는 조건으로,
    네 번째 열에서 선택하지 않았다.
    
    + (?) 구멍 뚫린 구조-atrous
        - A trous(프랑스어): 구멍이 있는; Atrous Convolution: 구멍이 있는 합성곱
        - 일반적인 convolution 사이에 공간을 넣어서 구멍이 뚤린 듯한 구조이다.
        - 같은 연산량으로 더 큰 특징을 잡아낼 수 있다. 
        - (출처) https://medium.com/hyunjulie/2%ED%8E%B8-%EB%91%90-%EC%A0%91%EA%B7%BC%EC%9D%98-%EC%A0%91%EC%A0%90-deeplab-v3-ef7316d4209d

### * 설명 분석

* 설명 없음. 본문 분석에서 참고될 예정.

### * 종합 분석

> * 데이터 증가(data augmentation)을 진행하지 않은 SSD 모델은 mAP가 65.5로 가장 낮은 수치를 기록했다. 그에 비해, 데이터 증가를 선택한 모델들은 mAP가 70 이상으로 성능이 월등히 높아졌음을 알 수 있다.
>> * 즉, 데이터 증가는 매우 효율 적인 학습 방법이라 생각할 수 있다.
> * {1/2, 2}와 {1/3, 3} 박스들을 선택하지 않은 두 번째 열과, 모두 선택한 다섯 번째 열을 비교해 보았을 때, mAP가 각각 71.6, 74.3으로 기록된다.
>> * 따라서, 필터링을 진행할 박스들의 사이즈가 다양할 수록 효율이 증가함을 알 수 있다.
> * {1/2, 2}, {1/3, 3} 박스들을 선택하지 않은 두 번째 열과, {1/2, 2} 박스 사용 만을 선택한 세 번째 열을 비교해 보았을 때, mAP가 각각 71.6, 73.7이다.
>> * 이는 검출용 박스(기본 박스)들의 사이즈를 조금이라도 더 다양하게 할 수록 효율이 증가함을 알 수 있다.
> * atrous 합성곱을 허용하지 않는 네 번째 열과, 허용하는 다섯 번째 열을 비교해 보았을 때, mAP가 각각 74.4, 74.3 이다.
>> * mAP의 값이 크게 차이가 나지 않고, 되려 atrous를 사용했을 때 mAP가 0.1 줄어드는 것으로 효율이 떨어진다.
>> * atrous 방법을 사용하는 것이 옳지 않는 방법인 것은 아니나 상황에 따라 사용을 고려하는 것이 좋을 것으로 추측된다.
>> * 개인적으로 이러한 문제의 원인에 대해, 이미지 데이터 내 빈 공간 삽입을 통해 특성 추출을 극대화 하는 atrous 기법의 특징과 학습용 이미지 데이터에 GT 박스를 씌우고, 이 GT박스와 박스 뭉치들을 비교하는 SSD 학습 방식이 서로 시너지를 일으키지 못하거나 상충하는 것으로 추측하고 있다.

### [ 6 ] Table 3. Effects of multiple layers

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/Table03_Effects.JPG "Table 3. Effects of multiple layers")

### 참고

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/model_structure.JPG "Model Structures")

### * 시각 자료 분석

* 다중 계층의 영향에 대한 표로 Fig 2. 모델 구조와 비교해 보는 것을 권장한다.
    + (1) 첫 번째 열은 conv4_3 으로 기반 네트워크(백본 네트워크; VGG-16) 내에 포함된 합성곱 층이다.
        - (1-1) 마지막 행에서 선택되지 않았다.
    + (2) 두 번째 열은 conv7 로 기반 네트워크가 끝나고 나서 두 번째로 적용되는 계층이다. 
        - (2-1) 모든 행에서 체택되었다.
    + (3) 세 번째 열은 conv8_2 로 Fig 2.의 중간 쯤에 위치하는 계층이다.
        - (3-1) 다섯 번째 행, 마지막 행에서 제외되었다.
    + (4) 네 번째 열은 conv9_2 로 conv_8_2 바로 뒤에 위치하는 계층이다.
        - (4-1) 첫 번째 부터 세 번째 행까지 체택되어있다.
    + (5) 다섯 번째 열은 conv10_2 로 첫 번째, 두 번째 열에서 체택되었다.
    + (6) 여섯 번째 열은 conv11_2 로 가장 마지막 합성곱 계층이다.
        - (6-1) 첫 번째 행에서만 체택되었다.
    + (7) 일곱 번째 열은 BBox 사용 여부에 따른 mAP 값을 나타낸다.
        - (7-1) 대부분 Yes 열의 mAP값이 No 열의 mAP 값보다 큰 것으로 나타난다.
    + (8) 마지막 열 # Boxes 열은 만들어진 Box들의 개수를 의미한다.
        - (8-1) 인식된 객체들의 박스 수를 의미하는 것으로 추정된다.

### * 설명 분석

* 설명 없음. 본문 분석에서 참고될 예정.

### * 종합 분석

> * BBox를 사용한다는 전제하에, 모든 특성 맵(conv)들을 선택한 첫 번째 행은 74.3 의 mAP를 출력하였다. 그리고, 다음 행을 지날 수록 남아있는 가장 작은 특성 맵들을 제외해가며 출련된 mAP를 비교해보면 지속적으로 줄어듬을 알 수 있다. 이에 대해 두 가지 추측을 할 수 있었다.
>> * 우선, 가장 작은 특성 맵부터 제외를 한다는 의미는 세부적인 요소(특성)들을 학습하는 것을 포기한다는 의미로 받아들였다. 즉, 뭉뜽그려서 학습할 수록 효율이 떨어지는 것으로 추정한다.
>> * 또한, 첫 번째 행과 두 번째 행을 비교해 보았을 때, 되려 0.3 mAP가 증가하는 것을 볼 수 있는데, 이는 너무 작은 특성 맵, 즉, 너무 작은 검출용 박스(기본 박스)가 오히려 학습을 방해하는 것으로 추측할 수 있다. 과유불급이라는 의미이다.
> * conv6, conv7 은 같은 크기의 특성맵이고, conv8_2 부터는 절반 정도씩 특성 맵의 크기가 작아지기 시작한다. 표의 4행과 5행을 비교해 보았을 때, 5행에서는 conv8_2 를 선택하지 않았다. 이에 대한 결과로, conv8_2를 체택한 4행의 mAP는 70.7, 69.2이고, 체택하지 않은 5행의 mAP는 64.2, 64.4로 나타났다.
>> * 이 두 행의 비교에서 추정해 볼 수 있는 것으로 "다양한 크기의 검출용 박스와 특성 맵이 있어야 학습 효율이 좋아진다는 것."이다.
>> * 그 근거로, 4행에서 BBox를 사용할 때와 사용하지 않을 때를 비교하면, BBox를 사용할 때가 근소하지만 더 높은 효율을 내는 반면, conv8_2를 체택하지 않은 5행에서는 BBox를 사용하지 않을 때가 사용했을 때의 효율을 근소하지만 앞지르게 된다.
> * 마지막으로, 기반 네트워크에 포함된 conv4_3 체택 유무에 대해 5행과 마지막 행을 비교하는데, 당연히 conv4_3을 체택한 5행의 mAP가 높게 나온다. 두 행 모두 BBox를 사용하지 않은 경우의 mAP가 사용한 경우의 mAP를 앞지르는데, 하지만 5행은 0.2 mAP 정도만 차이가 생긴 반면, 6행은 2.4 mAP 정도로 매우 큰 차이가 발생한다.
>> * 이에 대해, "완전히 이미지 학습을 끝내고 나서 박스 비교를 할 것"이냐, "이미지 학습 도중에도 초벌 구이마냥 박스 비교를 조금씩이라도 진행 할 것"이냐에 대한 실험으로 받아들였다.
>> * 결론적으로, 기반 네트워크에 박스 비교를 하는 특성맵을 삽입하는 것이 더 좋은 SSD 모델을 만드는 것이라고 생각하고 있다.

### [ 7 ] Table 4. PASCAL VOC2012 test detection results

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/Table04_PASCAL_VOC2012.JPG "Table 4. PASCAL VOC2012 test detection results")

[ 2 ] Table 1. 은 분석 진행에 혼동 될 가능성이 있어 삽입하지 않았다.

### * 시각 자료 분석

* 해당 표는 PASCAL VOC2012 테스트 결과에 대한 표로 '[ 2 ] Table 1. PASCAL VOC2007 test detection results' 와 비슷한 구성을 가진다.
    + (1) 차이점으로 + 가 아닌 ++ 로 기재되었다는 것이다. 따로 의미가 있는 것으로 추정된다.
    + (2) [ 2 ]와 달리 sofa 외의 범주들에서 SSD-512 가 가장 높은 mAP를 나타내고 있다. 

### * 설명 분석

> Fast and Faster R-CNN use images with minimum dimension 600, while the image size for YOLO is 448 × 448. data: “07++12”: union of VOC2007 trainval and test and VOC2012 trainval. “07++12+COCO”: first train on COCO trainval35k then fine-tune on 07++12.

* PASCAL VOC2012 테스트 결과 표에 대한 설명으로
    + (1) Fast R-CNN, Faster R-CNN, YOLO 모두 [ 2 ]에서와 마찬가지인 전제를 가지고 있다.
    + (2) data 열의 '07++12' 는 'VOC2007 trainval과 test' 데이터셋과 'VOC2012 trainval' 데이터셋을 통합한 것이다.
    + (3) data 열의 '07++12+COCO' 는 먼저 COCO trainval135k 데이터셋으로 훈련한 후 '07++12' 데이터셋으로 미세 조정을 시행한 것이다.

### * 종합 분석

> * 결론적으로 '++'는 VOC2007의 trainval, test 데이터셋 모두와 VOC2012의 trainval 데이터셋을 통합한 데이터셋 사용을 의미한다.
> * [ 2 ] 와 비슷한 분석을 도출하지만, sofa 범주에서만 SSD-300이 우세했다.

### [ 8 ] Table 5. COCO test-dev2015 detection results

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/Table05_COCO.JPG "Table 5. COCO test-dev2015 detection results")

### * 시각 자료 분석

* COCO test-dev2015 결과에 대한 표로
    + (1) Fast R-CNN, Faster R-CNN, ION[21], SSD300, SSD512 에 대한 학습 결과들이 정리되어있다.
    + (2) Fast R-CNN, Faster R-CNN은 대부분 같은 데이터셋으로 학습한 내용이 정리되어있다.
    + (3) ION(Inside-Outside_Net)은 2015년 12월 발표된 모델로 당장 분석할 수 없으므로 비교만 할 것이다.
        - (참고) Inside-Outside Net: Detecting Objects in Context with Skip Pooling and Recurrent Neural Networks
    + (4) SSD-300, SSD-512는 Fast, Faster R-CNN, ION과 다르게 trainval135k가 사용되었다.
    + (5) mAP의 '0.5', '0.75', '0.5:0.95' 열의 의미를 가늠하기는 어렵지만, "[ 2 ] Table 1. 을 분석할 때 사용된 'Precision'과 'Recall'에 대한 표현"이거나 TP, FP 등등에 대한 표현일 가능성이 있다.

### * 설명 분석

* 설명 없음. 본문 분석에서 참고될 예정.

### * 종합 분석

> * 정확한 분석은 어렵다. 하지만, SSD-512 의 학습 결과가 가장 월등한 것만은 확실하다.
> * Faster R-CNN [22] 행의 결과와 ION, SSD-300 행의 결과들을 비교해 보았을 때, Faster R-CNN의 수치가 나머지 둘을 압도한다. 이 점을 주의깊게 고려해 본문 분석에 참고해야 한다.
> * ION과 SSD-300은 꽤 비슷한 결과를 도출한다. 이 점 또한 본문 분석에서 참고해야 한다.

### [ 9 ] Table 6. Results on Pascal VOC2007 test

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/Table06_Result_VOC2007.JPG "Table 6. Results on Pascal VOC2007 test")

### * 시각 자료 분석

* Pascal VOC2007 테스트 결과에 대한 표로
    + (1) Faster R-CNN, YOLO, Fast YOLO, SSD-300, SSD-512 순으로 정리된 표이다.
        - (1-1) Faster R-CNN이 (VGG16), (ZF)로 나뉘는 것을 확인할 수 있다. VGG16 또한 모델(네트워크)이었으므로 ZF 또한 모델인 것으로 추정된다.
    + (2) FPS 열이 존재한다. 이를 통해, 영상 데이터 학습에 대한 결과인 것으로 추정하고 있다.
        - (2-1) 참고문헌 [2], [5] 등을 통해 실시간 detection에 대한 논문임을 확인할 수 있었다.
        - (2-2) 정확한 의미는 아직 알 수 없지만, Faster R-CNN의 FPS는 매우 낮고, SSD-300, YOLO는 양호한 수준이며, 의외로 SSD-512의 FPS 수치가 낮은 편이다. 그리고 Fast YOLO는 위험할 수준으로 높다.
    + (3) Test batch size 열이 존재한다. batch size는 한번에 학습할 데이터의 양인데, 문제는 데이터 양의 기준이 한 프레임인지, 서로 다른 영상인지는 구분이 가지 않는다.
    + (4) # Boxes 열이 존재한다. 이는 인식된 객체 박스들의 개수를 의미한다.
        - (4-1) SSD-512 를 통해 검출된 박스들의 개수가 다른 모델들에 비해 압도적으로 많은 것을 확인할 수 있다.

### * 설명 분석

> SSD300 is the only real-time detection method that can achieve above 70 % mAP. By using a larger input image, SSD512 outperforms all methods on accuracy while maintaining a close to real-time speed. Using a test batch size of 8 improves the speed further.

* Pascal VOC2007 테스트 결과에 대한 표에 대한 설명으로
    + (1) SSD-300은 실시간 detection에서 mAP 70% 이상을 달성할 수 있다.
    + (2) 더 큰 크기의 input 이미지를 사용하는 SSD-512는 실시간 속도와 근접하게 유지하면서 정확도 면에서 모든 방법(모델)들을 능가한다.
    + (3) 8 batch 크기를 사용함으로써 속도가 훨씬 개선되었다.

### * 종합 분석

> * SSD 또한 실시간 detection에 사용할 수 있음을 알게 되었다.
> * SSD512의 FPS는 19, 22 등이고 SSD300, YOLO 등이 45에서 59의 값을 도출했는데도 설명에서는 SSD512가 실시간 속도와 근접하게 유지하고 있다고 묘사했다.
>> * FPS 열의 의미가 '실시간과의 차이'를 나타내는 것이라면, 'delta FPS'라는 의미라면 FPS 열의 값이 낮을 수록 학습 속도가 빠른 것으로 생각할 수 있다.
>> * 하지만, 형평성을 위해 'Test batch size' 열의 값이 1인 행들을 조사했을 때, 가장 낮은 FPS를 기록 값은 7로 Faster R-CNN(VGG16) 이었다. 반면, SSD-512의 FPS 값은 19 였다. 이는 Faster R-CNN(ZF)와 비슷한 수치이다. 어쩌면, FPS 값은 실제 FPS 수치이고, 실시간이라는 기준을 24프레임으로 잡았을 가능성이 있다.
>>> * 영화, 애니메이션 등 영상 매체의 전통적인 프레임 수는 24 프레임으로 유명하다.
> * Faster R-CNN(ZF) 에서 ZF 는 ZFNet 을 의미한다.
>> * AlexNet에 이어 ILSVRC 2013에서 우승을 차지한 모델이다.
>> * ZFNet의 핵심은 구조 그 자체보다 CNN을 가시화 하여, CNN의 중간과정들을 출력해 사람의 눈으로 보고 개선 방향을 파악할 방법을 만들어 냈다는 것에 있다.
>> * (출처) https://m.blog.naver.com/laonple/221218707503
> * SSD-300과 SSD-512의 Box 수는 각각 8732, 24564로 SSD-512 에서 검출된 박스 수가 SSD-300 에서 검출된 박스 수보다 3배 가량 높다.
> * SSD-300, SSD-512의 batch size가 1이었을 때는 FPS가 각각 46, 19 였지만, Batch size를 8로 증가시키고나서 비교하니 FPS가 각각 59, 22로 확실하게 증가했다. 이로서 설명 분석에서 언급되었던 batch 크기와 속도에 대한 설명을 직접 확인해볼 수 있었다.

### [ 10 ] Fig. 5. Detection examples on COCO test-dev with SSD512 model

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/Fig05_example_COCO.JPG "Fig. 5. Detection examples on COCO test-dev with SSD512 model")

### * 시각 자료 분석

* SSD-512 모델을 사용한 COCO test-dev 에 대한 detection 예시들로
    + (1) 다양한 객체들이 박스쳐지는 것을 볼 수 있다.

### * 설명 분석

> We show detections with scores higher than 0.6. Each color corresponds to an object category.

*SSD-512 모델을 사용한 COCO test-dev 에 대한 detection 예시들에 대한 설명으로
    (1) 0.6 보다 더 큰 점수를 detection 한 것들을 보여주고 있다.
    (2) 박스들 각각의 색상은 객체 범주에 대응한다.

### * 종합 분석

> * COCO test의 객체 범주가 몇개인지는 모르겠으나 [ 2 ]와 [ 7 ]의 표들을 고려해보았을 때 20개의 범주 + etc 로 정해져 있을 것으로 추정하고 있다.
> * 말, 개, 의자, 탁자 등등 [ 2 ], [ 7 ] 표에 포함되어 있는 범주들도 확인된다.
> * 설명 분석에서 0.6 보다 더큰 점수를 detection한 예시들이라고 언급되었다. 따라서, 60% 이상의 확신이 있는 객체들만 detection 했다는 것이다.

다음은 본문 분석이다.

----

본문의 길이는 매우 길기 때문에, 분석 내용을 요약 정리하고, 꼭 필요하거나 매우 중요한 내용의 구절의 경우에만 포함하기로 하였다.

## 3. 본문 분석

## [ 0 ] 개요

### * 본문 해석

개요의 문장들을 해석해 정리하였다.

* (1) 본문은 '단일' 신층 신경망을 사용해 이미지 내 객체들을 detect하는(인식하는) 방법(모델)을 제공(제시)한다.
* (2) SSD로 명명된 이 방법은 BBox의 출력 공간을 특성 맵 위치별 크기와 다양한 종횡비의 박스 뭉치들(기본 박스들)로 세분화한다.
* (3) 예측을 할 때, 네트워크(신경망)은 기본 박스 당 박스 내부의 객체 범주들 각각의 영향력(존재)을 나타내는 점수를 책정한다. 그리고, 객체의 형태에 더 맞추기 위해 박스를 조정한다. 추가적으로, 네트워크는 자연스럽게 다양한 크기의 객체들을 다루기 위해, 서로 다른 해상도의 특성맵 여러개로부터 도출된 예측값과 결합한다.
* (4) SSD는 '객체 제안 등을 요구하는 방법들'과 비교해 간단하다. 왜냐하면, SSD는 '제안 생성'과 '후속 픽셀 사용', '리샘플링 단계' 등을 완벽히 제거하고, 단일 네트워크에서 모든 연산을 캡슐화 하기 때문이다.
* (5) (4)의 특성은 SSD가 학습하는데 쉽게 해주고 '인식 구성(?)'이 필요한 시스템에 직관적으로 융합하게 한다.
* (6) PASCAL VOC, COCO, ILSVRC 데이터 셋등을 이용한 연구결과들은 '학습과 추정(에측) 모두를 통일된 framework로 제공하는 SSD'가 '추가적인 객체 제안 단계를 활용하는 방법들'에 비해 훨씬 더 빠르고, 경쟁력 있는 정확도를 가진다는 것을 입증했다.
* (7) 입력 크기가 300 x 300 일때, Nvidia Titan X를 이용한 SSD는 VOC2007 테스트에서 59 FPS로 74.3%의 mAP를 달성했다. 그리고, 입력 크기가 512 x 512 일때, SSD는 76.9%의 mAP를 달성하면서 최신 Faster R-CNN 모델과 비교해 압도적인 성능을 보여주었다. 다른 단일 단계 방법들과 비교했을 때, SSD는 더 작은 입력 이미지 크기에서도 더 나은 정확도를 보여주었다.
* (8) 코드는 여기서 확인이 가능하다. https://github.com/weiliu89/caffe/tree/ssd

### * Figure 분석과 비교

요약 분석과 비교했을 때
* (참고 1) ![Alt text](/Objectdetection/01_SSD_2016/rsc/image/model_structure.JPG "Model Structures")
* (참고 2) ![Alt text](/Objectdetection/01_SSD_2016/rsc/image/Fig01_SSD_framework.JPG "Fig. 1. SSD framework")
* (1) 요약 분석 (2)와 (3)은 '1. 모델 구조 확인의 [ 1 ] Fig. 2.' 와 '2. 여타 Fig 분석의 [ 1 ] Fig. 1.' 과 대조가 가능하다.
    + (1-1) 요약 분석 (2)의 " BBox의 출력 공간을 특성 맵 위치별 크기와 다양한 종횡비의 박스 뭉치들로 세분화한다.'에서
        - (1-1-1) '특성 맵 위치별 크기'는 (참고 1)의 설명과 conv8_2, conv9_2, ... 등 기반 네트워크 뒤에 추가되는 특성 맵들과, (참고 2)의 설명과 (b) 8 x 8 feature map, (c) 4 x 4 feature 맵 등과 대조해 볼 수 있다.
        - (1-1-2) '다양한 종횡비의 박스 뭉치들'은 당장 (참고 2)의 (b)와 (c) 내의 박스 뭉치들의 크기가 서로 다른 것, 박스 뭉치를 구성하는 박스들의 종횡비가 서로 다른 것 등과 대조해 볼 수 있다.
    + (1-2) 요약 분석 (3)의 "예측할 때, 네트워크는 기본 박스 당 박스 내부의 객체 범주들 각각의 영향력을 나타내는 점수를 책정한다. 그리고, 객체의 형태에 더 맞추기 위해 박스를 조정한다. 추가적으로, 네트워크는 자연스럽게 다양한 크기의 객체들을 다루기 위해, 서로 다른 해상도의 특성맵 여러개로부터 도출된 예측값과 결합한다."에서
        - (1-2-1) '예측할 때'는 결국 학습할 때를 나타낸다. 학습과 예측은 엄연히 다르지 않느냐라고 할 수 있지만, '객체의 형태에 더 맞추기 위해 박스를 조정한다.'라는 구절은 역전파를 의미한다. 이미 완성된 모델이라면 조정을 하지 않을 것이다.
        - (1-2-2) '박스 내부의 객체 범주들 각각의 영향력을 나타내는 점수를 책정한다.'는 (참고 2)의 (c)에서 묘사된 loc과 conf, 설명 중 (3) '형상 좌표와 활성들 예측', (4) '실측 박스와 대조', (예시) '대응시 양수, 비대응시 음수' 와 대조해 볼 수 있다.
* (2) 요약 분석 (4)는 '1. 모델 구조 확인의 [ 1 ] Fig. 2.'와 대조가 가능하다.
    + (2-1) 요약 분석 (4)의 "SSD는 '제안 생성'과 '후속 픽셀 사용', '리샘플링 단계' 등을 완벽히 제거하고, 단일 네트워크에서 모든 연산을 캡슐화 하기 때문이다."에서
        - (2-1-1) '후속 픽셀 사용' 제거, '리셈플링 단계' 제거는 (참고 1)의 기반 네트워크 뒤 추가된 특성맵들과 각 특성맵들에서 출발하는 화살표들이 최종적으로 어떤 결과를 나타내는지 묘사된 것과 대조해볼 수 있다.
* (3) 요약 분석 (6), (7)은 '2. 여타 Fig 분석의 [ 2 ] Table 1.과 [ 7 ] Table 4, [ 8 ] Table 5, [ 9 ] Table 6 과 대조해 볼 수 있다.

## [ 1 ] 소개

### * 본문 해석

소개의 문장들을 해석해 정리하였다.

* (1) 