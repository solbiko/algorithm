-- 코드를 입력하세요
SELECT * 
from PLACES 
where HOST_ID in
(     
    SELECT HOST_ID FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(ID) >= 2
)