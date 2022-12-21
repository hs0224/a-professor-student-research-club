## Object Detection과 Segmentation을 위한 주요 Dataset

<br/>

- PASCAL VOC
    - XML Format
    - 20개의 오브젝트 카테고리
- MS COCO
    - json Format
    - 80개의 오브젝트 카테고리
- Google Open Images
    - csv Format
    - 600개의 오브젝트 카테고리

> **많은 Detection과 Segmentation딥러닝 패키지가 위 Dataset들을 기반으로 Pretrained 되어 배포**


<br/>
<br/>

### PASCAL VOC
[PASCAL VOC 2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/)
- Classification/Detection : 20 classes
- Segmentation : Image, Objects, Class
- Action, classfication : 10 action classes + "other"
- Person Layout : Image, Person Layout

### Annotation 이란?
- 이미지의 Detection 정보를 별도의 설명 파일로 제공되는 것
- Annotation은 Object의 Bounding Box 위치나 Object 이름등을 특정 포맷으로 제공

<br/>
<br/>

### MS-COCO Dataset 소개
[COCO Dataset](https://cocodataset.org/#home)
- 80개 Object Category
- 300K의  Image들과 1.5 Million 개의 object들
- (하나의 image에 평균 5개의 Object들로 구성)
- Tensorflow Object Detection API 및 많은 오픈 소스 계열의 주요 패키지들은 COCO Dataset으로 Pretrained된 모델을 제공함

