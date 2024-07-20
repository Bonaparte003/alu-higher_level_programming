-- ORDERS THE CITIES OF CALIFORNIA BY ID
SELECT `id`, `name`
 FROM `cities`
WHERE `state_id` IN
	(
		SELECT `id`
		FROM `states`
		WHERE `name` = "california"
	)
ORDER BY `id`
