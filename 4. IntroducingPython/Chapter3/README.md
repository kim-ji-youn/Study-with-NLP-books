# 3. 파이 채우기: 리스트(list), 튜플(tuple), 딕셔너리(dictionary), 셋(set)
* 자료구조 data structure
## 3.1. 리스트와 튜플
* 튜플(tuple): 불변(ommutable) -> 항목에 할당하면 바꿀 수 없다. 
* 리스트(list): 변경 가능(mutable) -> 항목에 할당하고, 자유롭게 수정하거나 삭제할 수 있다. 
## 3.2. 리스트
### 3.2.1. 리스트 생성하기: [] 또는 list()
* 콤마(,)로 구분하고, 대괄호 ([])로 둘러쌓여 있다. 
```
>>> empty_list1 = []
>>> empty_list2 = list()
>>> weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
```
### 3.2.2. 다른 데이터 타입을 리스트로 변환하기: list()
* 문자열, 튜플 등을 리스트로 변환할 수 있다. 
* 문자열의 메소드 split()은 문자열을 리스트로 변환시켜 준다. 
```
>>>list('cat')
['c', 'a', 't']
```
### 3.2.3. \[index\]로 요소 얻기
* 인덱스 번호를 통해 하나의 특정 값을 추출할 수 있다. 
    * 0부터 시작한다. 
    * 음수의 경우 끝에서 거꾸로 값을 추출한다. (-1부터 시작)
* 인덱스 번호가 리스트의 범위를 벗어나는 경우 에러가 발생한다. 
```
>>> sur_name = ['kim', 'lee', 'park']
>>> sur_name[0]
'kim'
```
### 3.2.4. 리스트의 리스트
```
>>> small_birds = ['hummingbird', 'finch']
>>> extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
>>> carol_birds = [3, 'French hens', 2, 'tutledoves']
>>> all_birds = [small_birds, extinct_birds, carol_birds, 'macaw']
>>> all_birds
[['hummingbird', 'finch'], ['dodo', 'passenger pigeon', 'Norwegian Blue'], [3, 'French hens', 2, 'tutledoves'], 'macaw']
>>> all_birds[0][1]
'finch'
```
### 3.2.5. \[index\]로 요소 바꾸기
### 3.2.6. 슬라이스로 요소 추출하기
### 3.2.7. 리스트의 끝에 요소 추가하기: append()
### 3.2.8. 리스트 병합하기: extend() 또는 += 
### 3.2.9. 인덱스와 insert()로 요소 추가하기
### 3.2.10. 인덱스로 요소 삭제하기: del
### 3.2.11. 값으로 요소 삭제하기: remove()
### 3.2.12. 인덱스로 요소를 얻은 후 삭제하기: pop()
### 3.2.13. 값으로 요소의 인덱스 찾기: index()
### 3.2.14. 존재여부 확인하기: in
### 3.2.15. 값 세기: count()
### 3.2.16. 문자열로 변환하기: join()
### 3.2.17. 정렬하기: sort()
### 3.2.18. 요소의 개수 얻기: len()
### 3.2.19. 할당:= , 복사: copy()
