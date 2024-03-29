SELECT USER_ID, NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD a
JOIN USED_GOODS_USER b
ON a.WRITER_ID = b.USER_ID
WHERE a.STATUS = "DONE"
GROUP BY USER_ID
HAVING SUM(PRICE) >= 700000
ORDER BY 3