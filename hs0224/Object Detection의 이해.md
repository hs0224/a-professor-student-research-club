## Localization / Detection / Segmentation
- 공통적인 문제 Object(s)의 위치를 찾아내는 것

<br/>

|방법|설명|
|---|---|
|`Localization`|단 하나의 Object 위치를 Bounding Box로 지정하여 찾음|
|`Object Detection`|여러 개의 Object들에 대한 위치를 Bounding BOx로 지정하여 찾음|
|`Segmentation`|Detection보다 더 발전된 형태로 Pixel 레벨 Detection 수행|

- `Localization/Detection`
    - 해당 Object의 위치를 Bounding box로 찾고
    - Bounding Box내의 오브젝트를 판별
> `Bounding box regression`(box의 좌표값 예측) 문제와  
> `Classification` (분류) 두개의 문제가 합쳐져 있음

<br/>

- **One-stage-detector** 
    - Detect를 바로 적용
    - YOLO, SDD, Retina-Net, EfficientDet 등
- **Two-stage-detector** : 
    - Object가 있을만한 위치를 먼저 참조해서 만들어 놓는것 
    - RCNN, SPPNet, Fast RCNN, Faster RCNN 등
    - Inference하는데 속도가 느려서 실시간 적용이 어려움

<br/>
<br/>

## Object Detection의 주요 구성 요소
- 영역 추정 : Region Proposal
    - Object가 있을만한 위치에 대해서 힌트를 주는 것
- Detection을 위한 Deep Learning 네트워크 구성
    - Feature Extraction & FPN & Network Prediction (Classification & Regression)
- Detection을 구성하는 기타 요소
    - IOU, NMS, mAP, Anchor box

<br/>

## Object Detection의 난제
- Classification & Regression을 동시에 해결해야함 
    - loss 함수 설정이 어려움 (둘다 최적화가 되어야하기 때문)
- 다양한 크기와 유형의 오브젝트가 섞여 있음
- 중요한 Detect 시간 
    - CCTV와 같이 실시간 영상 기반에서 Detect해야 하는 요구사항이 증가함
- 명확하지 않은 이미지 
    - 전체 이미지에서 Detect할 오브젝트가 차지하는 비중은 얼마안댐 (배경이 대부분..) 
- 데이터 세트의 부족
    - 일일이 annotation을 만들어야함 (Bounding Box...)
    - 훈련 데이터 세트를 생성하기가 상대적으로 어려움

<br/>

## Object Localization 개요
- 하나의 이미지에서 하나의 Object 찾기

### 구조
- 원본 이미지 -> Featrue Extrator(Backbone) -> Feature Map -> FC Layer(Dense) -> **Soft max Class**  
- Annotation 파일 (Bounding box에 대한 좌표정보가 있음) -> **Bounding Box Regression**
> 여러 이미지와 Bounding box 좌표로 학습

<br/>

## Object Detection
- 두개 이상의 Object 찾기
- 이미지의 어느 위치에서 Oject를 찾아야 하는가?
- Bounding box만으로 모델에 넣어서는 inference가 어려움
    - 비슷한 Oject들이 하나의 Feature map에서 여러개 있기 때문
> Object가 있을만한 위치를 먼저 찾는게 중요 (region proposal)  
`이미지에서 Detect하려는 Obejct가 어느에 위치에 있는지 찾는게 첫번째 문제`

<br/>

## 이미지의 어느 위치에서 Object를 찾아야 하는가?
- Sliding Window 방식 : **Obj가 있을만한 위치를 무작정 찾는 방법**
    - 다양한 형태의 Window를 각각 sliding 시키는 방식
    - Window Scale은 고정하고 scale을 변경한 여러 이미지를 사용 (이미지 사이즈를 변경하는 방식)
        - 이미지를 너무 줄이게되면 Window 안에 너무 많은 obj가 포함되서 Detect하기 어려워지는 문제가 생김
- Region Proposal(영역 추정) 방식 : **Object가 있을만한 후보 영역을 찾는 방법**
    - 대표적으로 Selective Search가 있음
 

<br/>
<br/>

### Object Detection 성능 평가 Metric - IoU
- IoU : Intersection over Union
    - 모델이 예측한 결과와 실측 Box가 얼마나 정확하게 겹치는가를 나타내는 지표
    > 1에 가까울수록 object를 잘 Detect함

<br/>

### NMS (Non Max Suppression)
- Object Detection 알고리즘은 Object가 있을 만한 위치에 많은 Detection을 수행하는 경향이 강함
- NMS는 Detected 된 Object의 Bounding box중에 **비슷한 위치에 있는 box를 제거하고 가장 적합한 box를 선택**하는 기법


**NMS 수행 로직**
- Detected 된 bounding box 별로 특정 Confidence threshold 이하 bounding box는 먼저 제거 
> Confidence score 가 낮다는건 있을 만한 위치가 아니라는 것

- 가장 높은 Confidence score를 가진 box 순으로 내림차순으로 정렬하고 아래 로직을 모든 box에 순차적으로 적용
> 가장 높은 신뢰점수를 갖는 box와 많이 겹치면 가장 높은거 뺴고 다제거
