# SSD 논문 분석

담당: 김민기

----

## 0. 개요

### [ 1 ] 논문 분석 규칙

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

### [ 2 ] 논문 분석 순서

* (1) 논문의 figure를 분석한다.   
    + (1-1) figure 중 '모델의 구조'를 분석한다.   
    + (1-2) 여타 figure들을 분석한다.   

* (2) 논문의 구성 순서대로 분석한다.   

----

## 1. 모델 구조 확인

----

### [ 1 ] Fig 2. single shot detection 모델의 비교 SSD vs YOLO [5].

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/model_structure.JPG "Model Structures")

#### * 시각 자료 분석

* 좌측 기준으로 순서대로 진행해보면
    + (1) input 이미지   
    + (2) 'VGG-16 모델'과 5개의 풀링 계층   
    + (3) 여러 사이즈의 합성곱 계층들   
        - (3-1) 화살표; 분류기(합성곱 연산)
    + (4) 탐지 결과: 클래스 당 8732 오브젝트 탐지 (?)   
    + (5) Non-Maximum Suppression (?)등을 나타냄을 알수 있다. 그리고, YOLO는 분석에서 제외했다.

    + (?) 클래스 당 8732 오브젝트 탐지 - 8732 per Class, Non-Maximum Suppression

#### * 설명 분석

> Fig. 2. A comparison between two single shot detection models: SSD and YOLO [5]. Our SSD model adds several feature layers to the end of a base network, which predict the offsets to default boxes of different scales and aspect ratios and their associated confidences. SSD with a 300 × 300 input size significantly outperforms its 448 × 448 YOLO counterpart in accuracy on VOC2007 test while also improving the speed.

* '모델 구조' 시각 자료에 대한 설명으로
    + (1) SSD 모델은 '기반 네트워크'의 끝에 '여러 특성 계층들'을 추가했다.
    + (2) 이 특성 계층들은 "서로 다른 '크기', '종횡비' 그리고 '활성'의 '기본 박스들(?)'에 대한 '위치 좌표(?)'를 예측한다.
    + (3) SSD는 300 x 300 의 input size를 받는다.   

* 이후 내용은 YOLO와 비교하는 내용이다.   

    + (?) 기본 박스들-default boxes, 위치 좌표-offset

#### * 종합 분석

> * SSD는 '기본 네트워크'에 여러 특성 게층들을 추가했다고 언급되었다. 모델 시각 자료를 확인해 보았을 때, 'VGG-16'을 사용했음을 알 수 있는데, 이 VGG-16 모델이 기본 네트워크가 되는 것으로 추정된다.
> * 또한, VGG-16 모델 이후에 여러 '합성곱 계층들'이 보이는데, 이 계층들이 설명 분석에서 언급된 '특성 계층들'로 '기본 박스들'에 대한 위치 좌표를 예측하는 역할을 하는 것으로 추정된다.

----

## 2. 여타 figure들 분석

----

### [1] Fig. 1. SSD framework

![Alt text](/Objectdetection/01_SSD_2016/rsc/image/Fig01_SSD_framework.JPG "Fig. 1. SSD framework")

#### * 시각 자료 분석

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

#### * 설명 분석

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

#### * 종합 분석

> * SSD는 학습을 위해 2가지 요소가 필요하다. 하나는 '이미지'이고, 다른 하나는 이미지 내에 탐지를 목표로 하는 객체들을 둘러싸는 '박스'들이다. 이 박스들은 '실측 박스'라고 부르기로 했다.
> * 객체를 탐지하는 데에 또 다른 박스 종류가 필요하다. 이는 '박스 뭉치'로 여러개의 다양한 크기, 종횡비, 활성값들을 가지는 기본(점선) 박스들로 이루어져 있다.
> * 객체를 탐지하는 데에 필요한 또 다른 요소는 '추가 특성 계층들'로 8x8, 4x4등 여러 단위의 특성 계층들이 추가된다.
> * 위에서 분석한 모델 구조와 Fig. 1.의 시각 자료를 바탕으로 고려해보았을 때, 여러 박스 뭉치들은 "추가된 특성 계층들 각각에 여러개가 존재"하는 것으로 추정된다. 즉, VGG-16 이후의 "특성 계층들의 크기와 단위가 다양한 것은 이러한 박스 뭉치들 자체의 크기와 단위도 다양하게 하기 위함"이라 추정된다.

----
