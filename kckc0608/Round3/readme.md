# select

- 테이블의 모든 컬럼 값 출력
  ```
  select * from copang_main.member;
  ```
- 테이블의 특정 컬럼 값 출력
  ```(SQL)
  select email, age, address from member;
  ```

# where

- 특정 조건에 맞는 데이터만 고르기

  ```
  select * from member where email = 'codeit@naver.com'
  ```

- 구간 데이터 조회

  나이가 20살 이상

  ```
  SELECT *
    FROM member
   WHERE age >= 20;
  ```

  30대인 사람

  ```
  SELECT *
    FROM member
   WHERE age BETWEEN 30 AND 39;
  ```

  30대가 아닌사람

  ```
  SELECT *
    FROM member
   WHERE age NOT BETWEEN 30 AND 39;
  ```

  2019년 이후에 가입한 사람

  ```
  SELECT *
    FROM member
   WHERE sign_up_day > '2019-01-01';
  ```

  2018년에 가입한 사람

  ```
  SELECT *
    FROM member
   WHERE sign_up_day BETWEEN '2018-01-01' AND '2018-12-31';
  ```

- 문자열 패턴 조건

  주소의 값이 '서울'로 시작하는 문자열

  ```
  SELECT *
    FROM member
  WHERE address LIKE '서울%';
  ```

  주소의 값에 '고양'로 포함되는 문자열

  ```
  SELECT *
    FROM member
  WHERE address LIKE '%고양%';
  ```

- 여러 조건 걸기

  ```
  SELECT *
    FROM member
   WHERE address LIKE '서울%'
     AND gender = 'm'
     AND age between 25 and 29;
  ```

  ```
  SELECT *
    FROM member
   WHERE MONTH(sign_up_day) BETWEEN 3 AND 5
      OR MONTH(sign_up_day) BETWEEN 9 AND 11;
  ```

  ```
  SELECT *
    FROM member
   WHERE MONTH(sign_up_day) BETWEEN 3 AND 5
      OR MONTH(sign_up_day) BETWEEN 9 AND 11;
  ```

  ```
  SELECT *
    FROM member
   WHERE (gender = 'm' AND height >= 180)
      OR (gender = 'f' AND height >= 170)
  ```

# Order By

```
select *
  from member
  order by height;
```

기본적으로 오름차순 정렬을 수행

```
select *
  from member
  order by height desc;
```

내림차순 정렬 시 desc 키워드 추가

```
select *
  from member
  where gender = 'm'
    and weight >= 70
  order by height desc;
```

조건을 걸은 결과에 정렬을 적용하려면 where 이후에 order by 사용

```
select *
  from member
  order by year(sign_up_day) desc,  email asc;
```

정렬시 정렬 조건을 여러개 둘 수 있다.  
 먼저 쓴 값을 기준으로 정렬하고, 그 값이 같으면 뒤의 기준으로 정렬한다.

- 데이터 일부만 보여주기

  ```
  select *
    from member
   order by sign_up_day desc
   limit 10;
  ```

  정렬 후 10개 보여주기

  ```
  select *
    from member
   order by sign_up_day desc
   limit 8, 2;
  ```

  정렬 후 인덱스 8부터 2개 보여주기  
   즉, 9번재 10번째 보여주기

# COUNT, MAX, MIN, AVG

```
SELECT COUNT(email)
  FROM member;
```

email 행에 들어있는 데이터의 개수를 세서 보여준다.  
이때 NULL 의 경우는 count 하지 않는 것에 유의한다.

```
SELECT COUNT(*)
  FROM member;
```

어떤 column 을 골라서 셀지 결정하기 애매하면 그냥 통으로 테이블의 모든 column 에 대해 실행할 수 있다.

```
SELECT MAX(column)
  FROM table;
```

column 의 데이터들 중 최댓값

```
SELECT MIN(column)
  FROM table;
```

column 의 데이터들 중 최솟값

```
SELECT AVG(column)
  FROM table;
```

column 의 데이터들의 평균. 이때 NULL은 제외한다.

# IS NULL / IS NOT NULL

```
SELECT *
  FROM member
 WHERE address IS NULL
```

데이터가 NULL 인 row 만 조회  
'= NULL' 로 쓸 수 없다. NULL 은 비교할 수 있는 값이 아니기 때문이다.

```
SELECT *
  FROM member
 WHERE address IS NOT NULL
```

데이터가 NULL 이 아닌 ROW 만 조회

# COALESCE

NULL 데이터를 원하는 방식으로 출력하는 함수다.

```
SELECT coalesce(height, '####')
  FROM member;
```

이 쿼리를 실행하면 Null 값은 모두 #### 으로 보인다.  
첫번째 인자에는 column 이름을, 2번째 인자에는 Null 값을 표현할 문자열을 넘긴다.

# Column 조작하기

- column 간 산술 연산

  ```
  SELECT weight/((height/100)*(height/100))
    FROM member
  ```

  BMI 구하기  
  height와 weight 중 하나라도 Null이 있으면 결과 값도 Null 이다.

- Column 명 바꾸기 (Alias)

  ```
  SELECT weight/((height/100)*(height/100)) AS BMI
    FROM member
  ```

  ```
  SELECT weight/((height/100)*(height/100)) BMI
    FROM member
  ```

  `AS`를 붙이지 않고 그냥 한칸 띄우고 써도 된다.

- CONCAT 함수와 같이 사용하기

  ```
  SELECT CONCAT(height, 'cm', ', ', weight, 'kg') AS 'height and wieght'
    FROM member
  ```

- CASE 문을 사용해서 값을 조건 기준으로 통일해서 표시하기
  ```
  SELECT
    email,
    CONCAT(height, 'cm', ', ', weight, 'kg') AS 'height and wieght',
    weight / ((height / 100) * (height / 100)) AS BMI,
  CASE
      WHEN weight IS NULL OR height is NULL THEN 'dont know'
      WHEN weight / ((height / 100) * (height / 100)) >= 25 THEN 'high!!'
      WHEN weight / ((height / 100) * (height / 100)) >= 18.5 AND weight / ((height / 100) * (height / 100)) < 25 THEN 'good'
      ELSE 'low!!'
  END as bmi_check
    FROM member
  ORDER BY bmi_check asc
  ```
