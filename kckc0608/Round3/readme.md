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