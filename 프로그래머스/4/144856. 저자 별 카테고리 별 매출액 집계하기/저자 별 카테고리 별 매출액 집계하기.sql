-- 코드를 입력하세요
SELECT A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM((BS.SALES * B.PRICE)) AS TOTAL_SALES
FROM BOOK_SALES AS BS
JOIN BOOK AS B
ON B.BOOK_ID = BS.BOOK_ID
JOIN AUTHOR AS A
ON B.AUTHOR_ID = A.AUTHOR_ID
WHERE YEAR(BS.SALES_DATE) = 2022 AND MONTH(BS.SALES_DATE) = 1
GROUP BY A.AUTHOR_ID, B.CATEGORY
ORDER BY A.AUTHOR_ID, B.CATEGORY DESC