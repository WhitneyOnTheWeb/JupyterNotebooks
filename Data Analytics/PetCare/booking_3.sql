SELECT DATE(cc.added) AS conv_date
     , COUNT(cc.added) AS conv_total
FROM conversations_conversation AS cc
WHERE cc.added BETWEEN '2017-04-12' AND '2017-07-11'
GROUP BY DATE(cc.added)
ORDER BY DATE(cc.added) ASC
