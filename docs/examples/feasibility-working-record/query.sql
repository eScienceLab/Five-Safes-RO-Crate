-- Illustrative feasibility query for the Five Safes RO-Crate examples.
SELECT COUNT(DISTINCT person_id) AS cohort_size
FROM condition_occurrence
WHERE condition_concept_id = 201826;
