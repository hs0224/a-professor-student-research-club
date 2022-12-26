# YOLO (You Only Look Once)
## YOLO 논문 리뷰1(https://bkshin.tistory.com/entry/%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0-YOLOYou-Only-Look-Once)
### ABSTRACT
- 다른 객체 검출과는 다르게 새로운 접근 방식을 적용
- 기존의 multi-task 문제를 하나의 회귀 문제로 정의
- 이미지 전체에 대해서 하나의 신경망이 한 번의 계산만으로 bounding box와 클래스 확률(class probability)를 예측
- 객체 검출 파이프라인이 하나의 신경망으로 구성되어 있으므로 end-to-end 형식이다.
- YOLO의 통합된 모델은 굉장히 빠름