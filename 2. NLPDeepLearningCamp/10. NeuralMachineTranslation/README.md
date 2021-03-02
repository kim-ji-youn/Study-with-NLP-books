## 1. 기계번역
### 1. 번역의 목표
어떤 언어 *f*의 문장이 주어졌을 때, 가능한 *e* 언어의 번역 문장 중에서 최대 확률을 갖는 $$\hat{a}$$를 찾아내는 것

### 2. 기계번역의 역사
* **규칙 기반 기계번역(RBMT, Rule Base Machine Translation)**: 주어진 문장의 구조를 분석, 그 분석에 따라 규칙을 세우고 분류를 나누어 정해진 규칙에 따라 번역
* **통계 기반 기계번역(SMT, Statistical Machine Translation)**: 대량의 양방향 코퍼스에서 통계를 얻어내 번역 시스템을 구성


## 2. seq2seq
### 1. 구조 소개
* 인코더(encoder)
* 디코더(decoder)
* 생성자(generator)
