# DNN(Deep Neural Network)
모델 내 은닉층을 많이 늘려서 학습의 결과를 향상시키는 방법

# CNN(Convolutional Neural Network)
DNN에서 이미지나 영상과 같은 데이터를 처리할 때 발생하는 문제점들을 보완한 방법
데이터에서 직접 학습하고 패턴을 사용해 이미지를 분류한다. 특징을 수동으로 추출할 필요가 없다.

# R-CNN
CNN을 Object Detection 분야에 최초로 적용시킨 모델

<img src="https://seongkyun.github.io/assets/post_img/papers/2019-01-06-Object_detection/fig2.PNG" width="70%" height="50%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img>

모든 Proposal에 대해 CNN을 거쳐야 하므로 연산량이 매우 많은 단점이 존재

# Fast R-CNN
모든 Proposal이 네트워크를 거쳐야 하는 R-CNN의 병목(bottleneck)구조의 단점을 개선하고자 제안 된 방식

<img src="https://seongkyun.github.io/assets/post_img/papers/2019-01-06-Object_detection/fig3.PNG" width="70%" height="50%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img>

Proposal들이 CNN을 거치는것이 아니라 전체 이미지에 대해 CNN을 한번 거친 후 출력 된 특징 맵(Feature map)단에서 객체 탐지를 수행

+ Fast R-CNN에서 Region Proposal을 CNN Network가 아닌 Selective search 외부 알고리즘으로 수행하여 병목현상 발생

# Faster R-CNN
Region Proposal을 RPN이라는 네트워크를 이용하여 수행(병목현상 해소)

<img src="https://seongkyun.github.io/assets/post_img/papers/2019-01-06-Object_detection/fig5.PNG" width="70%" height="50%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img>

CNN을 통과한 Feature map에서 슬라이딩 윈도우를 이용해 각 지점(anchor)마다 가능한 바운딩 박스의 좌표와 그 점수를 계산하고
2:1, 1:1, 1:2의 종횡비(Aspect ratio)로 객체를 탐색

---------------------------------------

## R-CNN 계열 구조 비교
<img src="https://seongkyun.github.io/assets/post_img/papers/2019-01-06-Object_detection/fig7.PNG" width="70%" height="50%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img>

## R-CNN 계열 성능 비교
<img src="https://seongkyun.github.io/assets/post_img/papers/2019-01-06-Object_detection/fig7-1.PNG" width="70%" height="50%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img>

---------------------------------------

# G-RCNN
G-RCNN은 잘 알려진 Fast RCNN 및 Faster RCNN의 개선된 버전으로 Deep Convolutional Neural Network에 고유한 Granulation 개념을 통합하여 RoI를 추출합니다.
시공간 정보로 세분화하면 감독되지 않은 모드에서 RoI(객체 영역)를 보다 정확하게 추출할 수 있습니다.

## Fast, Faster RCNN 와비교
RoI를 정의할 때 모든 기능 값 대신 풀링 기능 맵 위에 과립(클러스터)들이 정의된다.
전체가 아닌 훈련 중 긍정적인 RoI만 사용한다.
정적인 이미지가 아닌 비디오를 직접 입력한다.
객체 분류를 수행하기 위해 전체 기능 맵 대신 RoI의 개체만 분류한다.(실시간 탐지 속도와 정확도가 향상)


## MCD-SORT
널리 사용되는 Deep SORT의 고급 형식으로 MCD-SORT에서 객체와 궤적의 연관성 검색을 동일한 범주 내로 제한한다.(다중 클래스 추적의 성능이 향상) 


</br>
</br>
</br>

+ Pooling - CNN의 문제점 중 하나를 교정해주는 작업(이미지를 5배씩이 아닌 1개의 이미지에 1개의 출력을 만들면서 동시에 기존 이미지에 Padding 없이 Filter만 적용해서 크기를 줄이는 방법)
+ Granulation 개념 - 입자 또는 괄비을 형성하는 것
+ 복수 개의 컨볼루션 층이 존재하는 신경망을 심층 합성곱 신경망(DCNN: Deep convolutional neural network)
+ 관심 영역(ROI: Region of interest)
