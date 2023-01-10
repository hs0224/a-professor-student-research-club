# mmtracking
https://github.com/open-mmlab/mmtracking

## 설치
https://mmtracking.readthedocs.io/en/latest/install.html#installation

사용 환경 - GPU RTX 2060、CUDA v10.1

홈페이지에 명시된 설치방법을 사용했는데 오류가 많이떴다 ex) dll load fail, fileno 등등

다른 방법으로 설치했다.

아나콘다 프롬프트에서

    # 가상환경 생성
    conda create -n open-mmlab python3.7 -y
    conda activate open-mmlab
    
    # CUDA 버전에 맞게 설치
    conda install pytorch==1.6.0 torchvision==0.7.0 cudatoolkit=10.1 -c pytorch -y
    
    # mmcv-full 설치
    pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu101/torch1.6.0/index.html
    
    # mmdetection 설치 - mmtracking은 mmdetection을 기반이기 때문에 설치 필요
    pip install mmdet
    
    # mmtracking 설치
    pip install mmtrack
    
    # 모델 활용을 위해 mmtracking파일 복제
    git clone https://github.com/open-mmlab/mmtracking.git
    
    # 파이썬 opencv2 설치
    pip install opencv-python
    
와 같은 순서로 설치하니 오류 없음
