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

# 중복값 제거

```
SELECT DISTINCT(gender)
  FROM member
```

```
SELECT DISTINCT(SUBSTRING(address, 1, 2))
  FROM member
```

substring 을 이용해 column에 연산을 수행하고, 그 결과값에 대해 다시 중복값 제거를 수행할 수 있다.

# Group By

```
select gender, count(*), avg(height), min(weight)
  from member
 group by gender;
```

특정 column의 값 종류(distinct)로 묶은 그룹들을 생성한다.  
집계함수(count, min, avg, ...) 는 각 그룹마다 나눠서 실행된다.

```
SELECT
  SUBSTRING(address, 1, 2) as region,
  count(*)
  FROM member
 GROUP BY SUBSTRING(address, 1, 2)
```

그루핑할 컬럼은 가공된 값이어도 된다.

```
SELECT
  SUBSTRING(address, 1, 2) as region,
  gender,
  count(*)
  FROM member
 GROUP BY SUBSTRING(address, 1, 2), gender
```

그루핑 기준은 여러개가 될 수 있다.  
위와 같이 쓰면, 주소의 앞 2자리가 같으면서 같은 성별인 사람들끼리 그룹이 지어진다.

```
SELECT
  SUBSTRING(address, 1, 2) as region,
  gender,
  count(*)
  FROM member
 GROUP BY SUBSTRING(address, 1, 2), gender
HAVING region = '서울' and gender = 'm'
```

이렇게 `HAVING` 구문을 이용하면, 그루핑된 그룹들 중 조건에 맞는 그룹만 고를 수 있다.

```
SELECT
  SUBSTRING(address, 1, 2) as region,
  gender,
  count(*)
  FROM member
 GROUP BY SUBSTRING(address, 1, 2), gender
 ORDER BY region, gender
```

생성된 그룹에 대해서 아래와 같이 정렬도 할 수 있다.

# Join

# Sub Query
- 평균값을 기준으로 쿼리 날리기
  ```
  SELECT i.id, i.name, AVG(star) AS avg_star
    FROM item AS i LEFT OUTER JOIN review AS r
      ON r.item_id = i.id
  GROUP BY i.id, i.name
  HAVING avg_star < (SELECT AVG(star) FROM review)
  ORDER BY avg_star DESC
  ```

  쿼리 안에 또 쿼리가 들어있는 구조다.   
  이때, 반드시 ( )로 서브 쿼리를 감싸주어야 함.

- SELECT 절에서 서브쿼리 사용하기
  ```
  SELECT
         id,
         name,
         price,
         (SELECT MAX(price) FROM item) AS max_price
    FROM item
  ```

  이렇게 하면, max(price) 값을 column에 추가한다.   
  모든 row에서 같은 값으로 보인다.

- WHERE 절에서 서브쿼리 사용하기
  ```
  SELECT
         id,
         name,
         price,
         (SELECT MAX(price) FROM item) AS max_price
    FROM item
   WHERE price > (SELECT AVG(price) FROM item)
  ```
  평균 가격보다 큰 가격을 가진 값들을 선택

  ```
  SELECT id, name, price
    FROM item
   WHERE price = (SELECT MAX(price) FROM item)
  ```
  가장 비싼 항목의 정보 출력

- 서브쿼리가 여러개의 값을 반환하는 경우
  ```
    SELECT *
      FROM item
     WHERE id IN (
      SELECT item_id
        FROM review
       GROUP BY item_id
      HAVING COUNT(*) >= 3
     )
  ```
  리뷰 테이블에서 item_id 가 같은 것끼리 그룹을 지어주고, 각 그룹에 대해 그룹 사이즈가 3이상 (즉, 리뷰가 3개 이상 존재하는 상품들)인 아이템의 id 를 반환하는 쿼리를 작성한다.   
  이 쿼리 결과로 여러 아이디들이 나올 수 있는데, 그 아이디 리스트에 포함된 id만 골라서 select 하는 코드다.

  지금은 IN 을 이용하였지만, ANY (그 중에 하나 이상에 대해 만족) 또는 ALL (모두에 대해 만족) 조건을 사용할 수도 있다.

- 서브쿼리 결과 자체를 새로운 테이블로 보고 FROM 절에 사용하는 경우
  ```
  SELECT AVG(review_count)
    FROM (
      SELECT SUBSTRING(address, 1, 2) AS region, COUNT(*) AS review_count
        FROM review AS r LEFT OUTER JOIN member AS m
          ON r.mem_id = m.id
       GROUP BY SUBSTRING(address, 1, 2)
      HAVING region IS NOT NULL
         AND region != '안드'
    ) AS review_count_summary;
  ```

 서브쿼리로 생성한 테이블을 유도된 테이블(derived table) 이라고 하는데, 반드시 이 테이블에는 alias를 붙여줘야 한다.