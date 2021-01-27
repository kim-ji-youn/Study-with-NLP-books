## 1. 전처리
### 1. 코퍼스란?
* **코퍼스Corpus**: 말뭉치, 여러 단어로 이루어진 문장
* **코퍼스 종류**
  * 단일 언어 코퍼스 monolingual corpus: 하나의 언어로 구성된 코퍼스
  * 이중 언어 코퍼스 bilingual corpus: 두 개의 언어로 구성된 코퍼스
  * 다중 언어 코퍼스 multilingual corpus: 두 개 이상의 언어로 구성된 코퍼스
  * 병렬 코퍼스 parallel corpus: 언어 간에 쌍으로 구성된 코퍼스
   ex) 나는 학생입니다 - I'm a student
  
### 2. 전처리 과정 개요
  1) 코퍼스 수집
  2) 정제
  3) 문장 단위 분절
  4) 분절
  5) 병렬 코퍼스 정렬
  6) 서브워드 분절
  
## 2. 코퍼스 수집
 * 크롤링 활용
   * Selenium 패키지 활용
   * BeautifulSoup 패키지 활용

### 1. 단일 언어 코퍼스 수집
### 2. 다중 언어 코퍼스 수집

## 3. 정제 normalization
### 1. [전각문자] 제거
* 전각문자를 반각문자로 변환해주는 작업이 필요
  * 전각문자: double byte 
  * 반각문자: single byte
  * 변환하는 방법: 유니코드를 활용 --> [참고]

[전각문자]: https://ko.wikipedia.org/wiki/%EC%A0%84%EA%B0%81_%EB%AC%B8%EC%9E%90%EC%99%80_%EB%B0%98%EA%B0%81_%EB%AC%B8%EC%9E%90
[참고]: https://namu.wiki/w/%EC%A0%84%EA%B0%81%EA%B3%BC%20%EB%B0%98%EA%B0%81#s-5



