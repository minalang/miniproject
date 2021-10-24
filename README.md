# 한국외대 인공지능 페스티벌: 제철재료, 조리법, 요리 난이도 기반 비건레시피 추천 서비스

### 01 데이터 크롤링
-> 해먹남녀, 인스타, 만개의 레시피, 유튜브, 블로그에서 ‘비건’, ‘채식’을 키워드로 레시피 데이터를 크롤링한 코드입니다.

### 02 데이터 전처리
-> 불필요한 재료 단위 전처리 및 레시피 제목 전처리, 부재료와 주재료 분류, 단계별로 레시피 나누기, 육류 제거 등을 진행하였습니다.

### 03 조리법 분류
-> 만개의 레시피에서 조리방법과 레시피를 매칭시킨 데이터를 크롤링하여 레시피를 분석하여 조리방법을 예측하는 모델을 만들었습니다.  
-> 끓이기, 볶기, 찌기, 튀기기, 굽기, 기타 총 6가지의 조리방법 각각에서 특징적인 단어를 잡아내는 함수를 만들고, 그 함수를 통해 분석한 값을 기준으로 조리방법을 분류합니다.  
-> XGboost, 나이브베이즈와 같은 여러 모델 시도한 결과 랜덤포레스트 모델이 가장 높은 정확도(약 79%)%를 보여 해당 모델로 저희가 구축한 비건 레시피 조리방법을 분류했습니다.  

### 04 난이도 분류
-> 쓰인 재료의 종류에 따라 어려운 재료와 쉬운 재료가 쓰인 재료 점수를 매기고, 레시피에 쓰인 동사의 갯수(레시피 형태소 분석 Utagger)로 
절차의 복잡도를 계산하였습니다.  
-> 이후 엑셀로 분포를 살펴 레시피 별 난이도를 라벨링 하였습니다.    

### 05 계절, 재료, 난이도, 조리법 검색
-> '계절매칭' 파일은 저희가 구축한 비건레시피 데이터 재료를 제철에 따라 분류하고 검색하는 코드입니다.  
-> '유사재료검색'은 원하는 재료를 검색하면 유사한 재료가 쓰인 레시피를 보여주는 코드입니다.  
-> <b>code_all_model</b> 파일에서 저희가 전처리하고 조리법 및 난이도를 라벨링한 최종 데이터를 계절/재료/난이도/조리법을 
기준으로 원하는 레시피를 검색하는 코드 흐름을 한 번에 보실 수 있습니다.  

### 06 백엔드 및 프론트엔드
-> 웹사이트 구현 코드입니다.    
-> 각 페이지마다 사용자로부터 검색 키워드를 받아오면 구축한 DB에서 데이터를 검색하고 받아와 웹사이트에 구현합니다.  

## 07 구현 화면
![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F3rQlc%2FbtriFtDPzcV%2FYgKVKHd7Vi31l9P4fmKm6K%2Fimg.jpg)
![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdxmZ8L%2FbtriJuvrpE9%2FHYxfVKwAVV5bEhQNAZg1F1%2Fimg.jpg)
![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbDZSSv%2FbtriAyGApv3%2FFGOyoZkbVnagXodQETPKUK%2Fimg.jpg)
