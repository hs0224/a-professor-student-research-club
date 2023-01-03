## Object Detection Network 구조 개요 및 FPS, Resolution과 성능 상관 관계

<br/>

- 구조
1. Feature Extractor Network
    - VGG, RESNET, INCEPTION 등
    - 보통 ImageNet 데이터 세트 기반으로 Pretrained됨
    > CNN Network 뺵본이라 부름
2. Object Detection Network
    - 보통 Pascal VOC/MC-COCO 데이터 세트 기반으로 Pretrained됨
    > FCN Bounding Box 예측 수행
3. Region Proposal 


<br/>

- Image Resolution, FPS, Detection 성능 상관 관계
    - 높은 Image Resolution일수록 Detection 성능이 좋은 반면 FPS 는 떨어짐
    - FPS가 빨라야 하는 요구사항일 수록 Detection 성능이 떨어짐

