SELECT MAX(NOx), Location, DATE(`Date Time`)
FROM readings
INNER JOIN stations
ON readings.SiteID = stations.SiteID
WHERE DATE(`Date Time`) BETWEEN '2019-01-01' AND '2019-12-31';