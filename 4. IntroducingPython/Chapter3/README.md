# 3. 파이 채우기: 리스트(list), 튜플(tuple), 딕셔너리(dictionary), 셋(set)
* 자료구조 data structure
## 3.1. 리스트와 튜플
* 튜플(tuple): 불변(mmutable) -> 항목에 할당하면 바꿀 수 없다. 
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
* list\[index\]
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
* list\[index\] = element1
* 인덱스 번호로 리스트의 요소를 바꾼다.
* 인덱스 번호가 리스트에서 유효한 위치여야 한다. 
* 문자열은 이러한 방식으로 변경할 수 없다. 
```
>>> sur_name = ['kim', 'park', 'lee']
>>> sur_name[2] = 'choi'
>>> sur_name
['kim', 'park', 'choi']
```
### 3.2.6. 슬라이스로 요소 추출하기
* list\[idx1: idx2: step\]
* 슬라이스를 사용해서 리스트의 서브시퀀스를 추출
* 스텝을 사용할 수 있음
* 리스트 순서 뒤바꾸기는 \[::-1\]
```
>>> sur_name
['kim', 'park', 'lee']
>>> sur_name[::-1]
['choi', 'park', 'kim']
```
### 3.2.7. 리스트의 끝에 요소 추가하기: append()
* list.append(element)
```
>>> sur_name.append('lee')
>>> sur_name
['kim', 'park', 'choi', 'lee']
```
### 3.2.8. 리스트 병합하기: extend() 또는 +=
* list.extend(element)
* list += element
* .extend()와 += 는 둘 다 두 리스트를 병합하는 역할을 한다. 
* .append()는 요소를 병합하는 것이 하니라 하나의 리스트로 추가시킨다. 
```
>>> sur_name = ['kim', 'park', 'choi', 'lee']
>>> other = ['ahn', 'cho']
>>> sur_name.extend(other)
>>> sur_name
['kim', 'park', 'choi', 'lee', 'ahn', 'cho']

>>> sur_name = ['kim', 'park', 'choi', 'lee']
>>> other = ['ahn', 'cho']
>>> sur_name.append(other)
>>> sur_name
['kim', 'park', 'choi', 'lee', ['ahn', 'cho']]
```
### 3.2.9. 인덱스와 insert()로 요소 추가하기
* list.insert(idx, element)
* .append()는 리스트의 끝에 요소를 추가한다. 
* .insert() 함수는 원하는 위치에 요소를 추가할 수 있다. 
* 리스트 길이보다 더 긴 인덱스를 설정할 경우, append()와 같은 역할을 한다. 
```
>>> sur_name = ['kim', 'ahn', 'park', 'choi']
>>> sur_name.insert(1, 'hong')
>>> sur_name
['kim', 'hong', 'ahn', 'park', 'choi']

>>> sur_name.insert(10, ['oh', 'han'])
>>> sur_name
['kim', 'hong', 'ahn', 'park', 'choi', ['oh', 'han']]
```
### 3.2.10. 인덱스로 요소 삭제하기: del
* del list\[idx\]
* 인덱스 번호를 사용하여 특정 요소를 삭제
* 제거된 요소 이후의 요소들이 한칸씩 앞으로 당겨짐
* ```del```은 리스트 함수가 아니라 파이썬 구문이다. 
* list.del()을 사용할 수 없다. 
* 할당(=)의 반대개념
```
>>> del sur_name[-1]
>>> sur_name 
['kim', 'hong', 'ahn', 'park', 'choi']
```
### 3.2.11. 값으로 요소 삭제하기: remove()
* list.remove(element)
* 리스트에서 삭제할 항목의 위치를 모르는 경우, 요소를 이용하여 삭제
```
>>> names = ['kim', 'park', 'lee']
>>> names.remove('park')
>>> names
['kim', 'lee']
```
### 3.2.12. 인덱스로 요소를 얻은 후 삭제하기: pop()
* pop()은 리스트에서 항목을 가져오는 동시에 그 항목을 삭제한다.
* pop()은 맨 마지막 요소를 반환하고 삭제한다. 
* pop(0)은 리스트의 맨 첫 요소를 반환하고 삭제한다. 
* pop(n)은 리스트늬 (n-1)번째 요소를 반환하고 삭제한다. 
```
>>> names = ['kim', 'park', 'lee', 'hong']
>>> names.pop()
>>> names
['kim', 'park', 'lee']

>>> names.pop(1)
>>> names
['kim', 'lee']
```

* LIFO(Last In First Out)-> Stack -> append() & pop()
* FIFO(First In First Out) -> Queue -> append() & pop(0)

### 3.2.13. 값으로 요소의 인덱스 찾기: index()
### 3.2.14. 존재여부 확인하기: in
### 3.2.15. 값 세기: count()
### 3.2.16. 문자열로 변환하기: join()
### 3.2.17. 정렬하기: sort()
### 3.2.18. 요소의 개수 얻기: len()
### 3.2.19. 할당:= , 복사: copy()

## 3.3. 튜플
* 임의적인 항복의 시퀀스
* 리스트는 가변, 튜플은 불변 = 튜플을 정의한 이후에는 추가, 삭제, 수정을 할 수 없음
### 3.3.1. 튜플 생성하기: ()
### 3.3.2. 튜플과 리스트

## 3.4. 딕셔너리
### 3.4.1. 딕셔너리 생성하기: {}
### 3.4.2. 딕셔너리로 변환하기: dict()
### 3.4.3. 항목 추가/변경하기 : [key]
### 3.4.4. 딕셔너리 결합하기: update()
### 3.4.5. 키와 del로 항목 삭제하기
### 3.4.6. 모든 항목 삭제하기: clear()
### 3.4.7. in으로 키 멤버십 테스트하기
### 3.4.8. 항목 얻기: [key]
### 3.4.9. 모든 키 얻기: keys()
### 3.4.10. 모든 값 얻기: values()
### 3.4.11. 모든 쌍의 키-값 얻기: items()
### 3.4.12. 할당: =, 복사: copy()

## 3.5. 셋
### 3.5.1. 셋 생성하기: set()
### 3.5.2. 데이터 타입 변환하기: set()
### 3.5.3. in으로 값 멤버십 테스트하기
### 3.5.4. 콤비네이션과 연산자

## 3.6. 자료구조 비교하기

## 3.7. 자료구조를 더 
