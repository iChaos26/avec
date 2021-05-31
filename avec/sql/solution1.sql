
'Write a query to print total number of unique hackers who made at least 1 
submission each day (starting on the first day of the contest), 
and find the hacker_id and name of the hacker who made maximum number of submissions each day. 
If more than one such hacker has a maximum number of submissions, print the lowest hacker_id. 
The query should print this information for each day of the contest, sorted by the date.'


select submission_date , -- Campo1
    -- INICIO CAMPO 2
    -- 
    (
        SELECT 
            COUNT(distinct hacker_id)
        FROM 
            Submissions s2  
        WHERE 
            s2.submission_date = s1.submission_date 
        AND 
       
            (
                SELECT COUNT(
                    distinct s3.submission_date
                ) 
                FROM 
                    Submissions s3 WHERE s3.hacker_id = s2.hacker_id 
                    -- CALCULO NO INTERVALO DE DATA CAPTURADA X INICIO DOS DESAFIOS
                     AND s3.submission_date < s1.submission_date
                 ) = dateDIFF(s1.submission_date , '2016-03-01')) , 
    --FINAL CAMPO 2
    --INICIO CAMPO 3
    -- SELECT DESC DOS HACKERS ATIVOS
                (
                    SELECT 
                        hacker_id  
                    FROM 
                        submissions s2 
                    WHERE
                        s2.submission_date = s1.submission_date 
                    GROUP BY 
                        hacker_id 
                    ORDER BY 
                        count(submission_id) desc ,
                        hacker_id 
                    LIMIT 1) as actives,
    --FINAL CAMPO 3                
    --INICIO CAMPO 4
        (
            SELECT
                name 
            FROM 
                hackers 
            WHERE
                hacker_id = actives)
    --FINAL CAMPO 4
FROM -- critério FROM principal
(
    SELECT 
        distinct submission_date 
    FROM 
        submissions) s1
    GROUP BY
     submission_date