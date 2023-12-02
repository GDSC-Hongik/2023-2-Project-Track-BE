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