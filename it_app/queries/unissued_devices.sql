SELECT Device.* from Device
WHERE
Device.device_id NOT IN
(

	SELECT Device.device_id 
	FROM
	Device join issued_to ON Device.device_id=issued_to.device_id



);
