## 7/29(목) algorithm 스터디 - 문자열 조작
### 1. 유효한 팰린드롬
 - 문자랑 숫자만 다 붙여진 문자열로 변형
 ~~~python
     if not(c.isalpha() or c.isdigit()) : # 숫자나 문자가 아니라면
        new_str = new_str.replace(c, "") # c 값을 공백으로 바꾸기
 ~~~
 - 맨앞, 맨뒤부터 하나씩 옮기면서 비교 -> 반복횟수
 ~~~python
    repeat = len(new_str)//2

    for i in range(repeat):
        if new_str[i] is not new_str[len(new_str)-1-i]:
            return False
~~~

 ##### 느낀점.
 1. 맨앞, 맨뒤에서 시작해서 하나씩 줄여가며 비교하는 패턴
 2. isalpha()는 진짜 알파벳만 인식 -> , ; ! 등은 인식안함
 3. 문제에 조건이 많을 때는 하나씩 지워가면서 조건을 다 담았는지 체크할 필요있음 -> ex) 대소문자 구분 x

### 2. 문자열 뒤집기 
 - swap
 ~~~python
    s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i] # a, b = b , a
  ~~~

##### 느낀점.
1. python은 참조를 하기때문에 swap형식이 다름 ( c와 같이 메모리에 공간을 차지하고 값을 갖는게 아님 , 값을 참조할 뿐 )
2. 맨앞, 맨뒤에서 시작해서 하나씩 줄여가는 패턴 

### 3.로그 파일 재정렬 
- 식별자와 분리한 뒤에 문자열로 숫자와 문자인 로그를 구분
~~~python
   for i in logs : # logs를 숫자, 문자 로그로 나누기
        sep = i.find(" ") # 식별자 분리

        if i[sep+1:].replace(" ", "").isalpha(): # 식별자 분리 후 뒤가 문자일때
            let.append(i)
        else:                                    # 숫자일때
            dig.append(i)
~~~
- 문자로그들끼리 정렬 -> 다중기준정렬
~~~
    let = sorted(let, key=lambda let : (let[let.find(" ")+1:], let[:let.find(" ")])) # 정렬 다중조건
~~~
##### 느낀점.
1. 다중조건정렬 : key = lambda list : (조건1, 조건2)
2. 리스트합치기 : list1 + list2 (cf. list1.append(list2) : list2가 통채로 원소로 들어감)
3. 리스트빼기(-) 제공 x
4. ab cd 이렇게 공백이 껴있으면 isalpha()에서 False 나옴

### 4. 가장 흔한 단어 
- 소문자로 바꾸고 알파벳, 숫자 빼고 모두 " " 대체  -> ""대체하면 떨어진것 붙음 (b,c)
~~~python
    paragraph = paragraph.lower()  # 소문자로 바꾸기
    for i in paragraph:
        if not (i.isalpha() or i.isspace()):
            paragraph = paragraph.replace(i, " ")
~~~
- 공백 단위로 단어 나누고 banned는 제거 (이때 공백이 두개이상인 것들은 " "으로 들어갔기때문에 banned에 " "추가)
~~~python
    word_list = paragraph.split(" ")  # 공백으로 단어 나누기
    banned.append("") # banned에 "" 추가
    word_list = [i for i in word_list if i not in banned]  # 금지된 용어들 제거
~~~
- collections.Count()로 빈도수 세기 
~~~python
    count_dict = collections.Counter(word_list)  # 빈도수로 나타내기
    letter, count = count_dict.most_common(1)[0]  # 그것 중 가장 빈도수 높은 것
~~~

##### 느낀점.
1. list1 에서 list2 제거 : list1 = [i for i in list1 if i not in list2] 
2. split을 여러개 기준으로 하고싶다면 나머지를 대표 기준으로 replace한 후에 대표 기준으로 split
3. "  "을 " "로 split 하면 " " 생김 
4. collections.Counter() -> dict이 collections.Counter클래스에 쌓여나옴
5. most_common(n)하면 튜플의 리스트로 반환

### 5. 그룹 애너램
- 리스트 내포
~~~python
    for i in range(len(keys)):
        gruop = [ strs[j] for j in range(len(sorted_list)) if sorted_list[j] == keys[i]] # key의 원소와 같은 것들끼리 group화 하기
        result.append(gruop)
~~~

##### 느낀점.
1. idea : 결국 같은 문자, 숫자들로 이뤄진 배열 -> 정렬하면 같아짐
2. 문자열 정렬  : "".join(sorted(list(str), reverse= False)) -> 리스트로 고치고 정렬후 다시 문자열로 
3. keys() : list가 class로 쌓여서 객체로 나옴 -> 변환필요 
4. 리스트내포 : [i  반복문(i)   조건문(i)]
