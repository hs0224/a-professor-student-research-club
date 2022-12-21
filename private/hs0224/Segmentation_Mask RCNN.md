# Segmentation - Mask RCNN
- Object Detection과 Segmentation

<br/>


- Segemtation --> 쉽게말하면 분할
    - Semantic Segmentation
        - 동일 클래스는 같은 색으로 분할
    - Instatnce Segmentation
        - 각각 개별 obj를 masking으로 구분
        - 동일 클래스도 다른 객체이기 때문에 다른 색으로 분할

<br/>

## Semantic Segmentation 개요
- Pixel Wise classification
    - 이미지의 개별 Pixel별 Classification
- Semantic Segmentation Encoder-Decoder Model (**재창조 재해석**)
    - **FCN, Segnet, U-NET, Dilated FCN**
    - Convolution layers (Encoder)
        - 차원축소
        - 점점 추상화 시킴
        - 위치적인 정보는 깨지지만 또는 사이즈는 줄지만, 원본이미지의 핵심적인 정보는 응축이됨
    - Deconvolution layers (Decoder)
        - 압축이된 추상적인 정보를 가지고 원본이미지와 유사하게 사이즈를 늘려나가면서 거기에 숨겨진 Hidden 패턴을 찾음
            - 원본이미지에서는 찾을 수 없었던 패턴들 찾음
            - 다시 복원하면서 필요한 정보를 학습
        - 원본이미지를 똑같이 복사하는게 아님
        - 이렇게 학습된 정보를 기반으로 Segmentation수행


<br/>
<br/>

## FCN (Fully Convolutional Network for Semantic Segmentation)

### Fully Connected Layer vs Fully Convolutional layer?
 

<br/>
<br/>

## Mask RCNN
- Faster RCNN 과 FCN 기법 개선 및 결합
    - ROI-Align
    - Bounding box Regression + Classification + Binary Mask Prediction
    - Resnet + Feature Pyramid Network
    - 비교적 빠른 Detection 시간과 높은 정확도
    - 직관적이고 상대적으로 쉬운 구현 

<br/>

### Segmentation에서 ROI Pooling 문제점

- RPN에서 추천한 영역인 ROI 영역(3x3)을 2x2 ROI (Max) Pooling 할때 3x3을 2x2로 바꿔야하는데 이때 잘려나가는 부분이 생김
    - 균등한 영역이 안댐 --> 정확한 영역을 측정하는데 문제가 생김

### Bilinear Interpolation을 이용한 ROI-Align
- 그리드를 정수로 맞추려고 하지말고(딱자르지말고) 가상의 소수점까지 생각해보자
- ROI를 소수점 그대로 매핑하고 ROI의 개별 Grid에 4개의 Point를 균등하게 배열
- 개별 Point에서 가장 가까운 feature map Grid를 고려하면서 포인트를 Weighted Sum으로 계산
- 계산된 포인트를 기반으로 Max Pooling 수행
