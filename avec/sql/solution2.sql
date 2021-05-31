--JOIN PARA CAPTURAR CHALLENGE ID NAS TABELAS SUBMISSIONS E CHALLENGES, 
--JOIN PARA LEVE DE DIFICULDADE NA TABELA CHALLENGES E DIFFICULTY
--JOIN PARA RESULTADO FINAL NA TABELA HACKERS AGRUPADOR PO DIFICULDADE

SELECT h.hacker_id, h.name
    FROM submissions s
    JOIN challenges c
        ON s.challenge_id = c.challenge_id
    JOIN difficulty d
        ON c.difficulty_level = d.difficulty_level 
    JOIN hackers h
        ON s.hacker_id = h.hacker_id
    WHERE s.score = d.score 
        AND c.difficulty_level = d.difficulty_level
    GROUP BY h.hacker_id
        HAVING COUNT(s.hacker_id) > 1
    ORDER BY COUNT(s.hacker_id) DESC, s.hacker_id ASC