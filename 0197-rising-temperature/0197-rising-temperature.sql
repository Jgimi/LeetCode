# Write your MySQL query statement below
select wt.id from Weather wy, Weather wt where  datediff(wt.recordDate,wy.recordDate)=1 and wt.temperature>wy.temperature