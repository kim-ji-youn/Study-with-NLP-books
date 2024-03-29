## 6. 텍스트 유사성을 위한 군집화

* **유사성(=유사도, 닮음, similarity)**: 비슷한 문서끼리 함께 그룹화, 그 결과로 형성된 그룹을 통해 전반적인 주제, 토픽 및 말뭉치 내부 패턴을 광범위하게 알 수 있음

### 6.1. 텍스트에 대한 비지도 학습
* **비지도 학습**
    * 탐색적 텍스트 분석에서 유용
    * 텍스트에 레이블이 부착되지 않은 상태에서 활용 가능
* **군집화(clustering) 알고리즘**
    * 목표: 레이블이 지정되지 않은 데이터의 잠재 구조나 테마를 발견
    * 데이터 종류: 단일 문서 또는 발화(utterance)
    * 데이터 특징/자질: 토큰, 어휘, 구조, 메타데이터
    * 군집화 방법:
        * 거리 계량(distance metrix)
        * 계층 군집화
            * 토픽 모델링(gensim)
            * 행렬 인수분해(matrix factorization)
            * 잠재 디리클레 할당(LDA, Latent Dirichlet Allocation)


### 6.2. 문자 유사성에 의한 군집화
*내가 필요했던게 이거잖아*

**근접도(closeness)**: 유사성 측정 기준

1. 문자열 정합(string matching, 문자열 일치)
    - 편집 거리(edit distance)
        - 레벤슈타인(Levenstein)
        - 스미스-워터만(Smith-Waterman)
        - 아핀(Affine)
    - 정렬(alignment)
        - 자로-윈클러(Jaro-Winkler)
        - 소프트 TFIDF(soft-TFIDF)
        - 몬지-엘칸(Monge-Elkan)
    - 음운(phonetic)
        - 사운덱스(Soundex)
        - 변환(translation)
2. 거리 계량(distance metrics)
    - 유클리드(Euclidean)
    - 맨해튼(Matnhatten)
    - 민코프스키(Minkowski)
    - 텍스트 분석학(Text Analytics)
        - 자카드(Jaccard)
        - TF-IDF
        - 코사인 유사도(cosine similarity)   
3. 상대적 정합(relation matching, 상대적 일치)
    - 집합 기반
        - 다이스(Dice)
        - 타니모토(Tanimoto)/자카드(Jaccard)
        - 공통 이웃(common neighbor)
        - 아다르 가중(Adar weighted)
     - 총계(aggregate, 총량)
        - 평균값(average values)
        - 최댓값/최솟값(max/min values)
        - 중간값(mediances, 중위수)
        - 빈도(frequency) 또는 최빈값(mode)
4. 그 밖의 정합(other matching)
    - 수치 거리(numeric distance)
    - 부울 상등(boolean equality)
    - 퍼지 정합(fuzzy matching, 퍼지 매칭)
    - 영역 특정(domain specific)
    - 가제트(gazettes)
         - 어휘 정합(lexical matching)
         - 개체명 인식(named entity recognition)

#### 6.2.1. 거리계량
* 유클리드 거리(Euclidean distance): 두 지점 사이의 거리가 대각선으로 표시되는 직석
* 맨해튼 거리(Manhattan distance): 두 지점 사이의 거리를 좌표 사이의 계단 모양 경로로 표시하여, 직각 좌표(cartesian coordinates)의 절대 차를 합한 것과 비슷
* 민코프스키 거리(Minkowski distance): 유클리드 거리와 맨해튼 거리를 일반화한 것. 정규화된 벡터 공간에서 두 점 사이의 거리를 정의
--> 말뭉치의 어휘가 늘어날수록 해당 말뭉치의 차원이 늘어나고, 어휘의 분산도 균일해짐

* 마할라노비스 거리(Mahalanobis distance): 특정 지점이 점의 분포로부터 얼마나 많은 표준 편차를 벗어났는지 측정할 수 있게 다차원으로 일반화한 계량
* 자카드 거리(Jaccard distance)
* 편집 거리(Edit distance)
#### 6.2.2. 부분 군집화
#### 6.2.3. 위계적 군집화

### 6.3. 문서 토픽 모델링
#### 6.3.1. 잠재 디리클레 할당
#### 6.3.2. 잠재 의미 분석
#### 6.3.3. 음이 아닌 행렬 인수분해
