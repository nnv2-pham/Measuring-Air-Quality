SELECT Location, AVG(`PM2.5`), AVG(`VPM2.5`)
FROM readings
INNER JOIN stations
ON readings.SiteID = stations.SiteID
WHERE DATE(`Date Time`) BETWEEN '2019-01-01' AND '2019-12-31'
	  OR TIME (`Date Time`) LIKE '%08:00%'
GROUP BY Location; 