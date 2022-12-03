## R-CNN (Regions with CNN)

- Region Propsal 방식에 기반한 Object Detection
- 딥러닝을 최초로 Object Detection에 도입

<br/>

- Stage 1 : Region Proposal
- Stage 2 : CNN Detection

<br/>

- RCNN 모델의 Classification Dense layer로 인해 이미지 크기가 동일 해야 해서, 2000개 Region Proposal로 예측된 영역의 이미지 사이즈를 동일하게 가짐

- 이미지 크기를 같게 하기위해 2K의 Region 영역 Proposal에 Image crop와 Warp 적용

<br/>

> 특이한점 : FC Layer 다음 Softmax가 아닌 SVM를 사용

<br/>


### **R-CNN 개요 정리**
1. Input image
2. Extract region proposals (~2K) -> warped region
3. Compute CNN features
4. Classify regions


<br/>
<br/>

## RCNN Training - Classification
- 원본 이미지에 Selective Search 적용
- Annotation 파일을 바탕으로 GT 적용

<br/>

1. PASCAL VOC/ImageNet 으로 Feature Extractor Pre-train시킴
2. Gorund Truth와 SS Predicted 된 영역 IOU가 0.5이상인 경우만 해당 클래스로 나머지는 Background로 fine-tuning
3. Ground Truth로만 학습하되 0.3 IOU 이하는 Backgroud로 설정 0.3 이상이지만 GT가 아닌 경우는 무시

## Bounding Box Regression
- SS Predicted 된 영역의 중심 좌표와 Ground Truth의 중심좌표간 거리가 최소가 되도록 만들어줘야함

<br/>

### R-CNN 장단점
- 동시대의 다른 알고리즘 대비 매우 높은 Detection 정확도
- 너무 느린 Detection시간과 복잡한 아키텍처 및 학습 프로세스
    - 1장의 이미지를 Object Detection 하는데 약 50초 소요
    - 각기 따로 노는 구성 요소
        - Selective search, CNN Feature Extractor, SVM과 Bounding box regressor로 구성되어 복잡한 프로세스를 거쳐 학습 및 Object Detection이 되야함

<br/>
<br/>

## RCNN 수행 시간 개선 방안 문제점
- CNN은 서로 다른 사이즈 Image를 수용하지 않음
    - why? Flatten FC Input의 크기가 고정이 되어야 하기 때문

> **개선방안 :** 서로 다른 크기를 가진 Region Proposal 이미지를 SPP Net의 고정된 크기 Vector로 변환하여 제공


### SPP(Spatial pyramid Pooling)
- CNN Image classification에서 서로 다른 이미지의 크기를 고정된 크기로 변환하는 기법

### SPM(Spatial Pyramid Matching) 
- 공간 정보를 가지고 매칭 (위치 정보 생성)
> 서로 다른 크기의 Feature Map을 균일한 크기의 Vector로 표현할 수 있게됨

<br/>

### R-CNN과 SPP-Net 비교
- R-CNN : 이미지 한 개에 2k번 CNN을 통과해야 함
- SPP-Net : 이미지 한 개는 한번만 CNN을 통과하면 됨

- 성능적인 측면에서도 수행 시간이 SPP-Net가 월등히 높아짐

<br/>
<br/>

## Fast RCNN
- 기존에 SPP-Net 에서 사용했던 SPP Layer를 ROI Pooling Layer로 교체
- 기존 RCNN, SPP-Net에서 사용되었던 SVM을 Softmax로 변환
- Multi-task loss 함수로 Classification과 Regression을 함께 최적화 할 수 있게됨

<br/>
<br/>

## Faster RCNN 
- 비로소 Obj Detection 구성요소가 모두 딥러닝을 사용 (완전하게 딥러닝기반 학습)
- Faster RCNN = **RPN**(Region Proposal Network) + Fast RCNN
- Selective Search를 Region Proposal Network 구조로 변경
    - GPU 사용으로 빠른 학습 Inference
    - End to End Network 학습

- Anchor Box : Object가 있는지 없는지의 후보 Box 선택하는 방식
    - Anchor box는 총 9개로 구성 (3개의 서로 다른 크기, 3개의 서로다른 ratio로 구성)
    - Anchor Box는 Feature map에서 매핑이 되는 것임
    - 각각 grid cell별 전부다 Anchor Box를 구함
        - Feature map size가 50x38이라면 총 grid locations는 1900개
        - 1900개 point에 대해서 9개의 Anchor Box를 그리면 17100개
        - 기존 Selective Search ROI는 2000개 Box에서 찾았다면 Anchor Box는 17100개에서 Obj가 있을만한 위치를 찾음

- Positive Anchor Box, Negative Anchor box로 분류
    - IOU가 가장 높은 Anchor는 Positive
    - IOU가 0.7이상이면 Positive
    - IOU가 0.3보다 낮으면 Negative
    - IOU가 0.3 ~ 0.7 사이면 학습대상에서 제외

<br/>

- Achor box를 Reference로 해서 Bounding Box Regression 수행  
    - 예측 bounding Box와 Positive anchor box와의 좌표 차이는 Ground Truth와 Positive anchor box와의 좌표 차이와 최대한 동일하게 될 수 있도록 regression학습



