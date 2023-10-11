SELECT a.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE),2) AS SCORE
FROM REST_INFO a
    RIGHT OUTER JOIN REST_REVIEW b
    ON a.REST_ID = b.REST_ID
WHERE ADDRESS LIKE "서울%"
GROUP BY REST_ID
ORDER BY SCORE DESC, FAVORITES DESC

# SELECT *
# # FROM REST_INFO
# FROM REST_REVIEW
# WHERE REST_ID ="00001"
# # WHERE ADDRESS LIKE "서울%"
# # 1 2 3 4 5 8