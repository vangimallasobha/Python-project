use ig_clone;
show tables;
-- 1. Create an ER diagram or draw a schema for the given database.
/* An ER diagram is a visual representation of the database schema that depicts the entities, attributes, and relationships between entities in a database system. 
It helps to provide a clear and concise overview of the database structure and the connections between different elements.
The ER diagram provides a visual representation of the database structure, making it easier for developers, designers, and stakeholders to understand the relationships between different entities. It is a valuable tool during the database design phase and helps ensure the correct implementation of the database schema. Additionally, it aids in communication and documentation, 
as it presents a clear picture of how the data is organized and connected in the system.*/
-- We want to reward the user who has been around the longest, Find the 5 oldest users.
select * from users;
select * from users order by created_at  limit 5;
--  To target inactive users in an email ad campaign, find the users who have never posted a photo.
select * from users;
select * from photos;
select * from users u left join photos p on u.id=p.user_id
where p.user_id is null;
-- or
select * from users where id not in (select user_id from photos );
-- or
select * from users
where not exists(select 1 from photos where users.id=photos.user_id);

-- Suppose you are running a contest to find out who got the most likes on a photo. Find out who won?
select * from users;
select * from photos;
select * from likes;
select username,photos.user_id,count(likes.user_id) total  from photos inner join likes on photos.user_id=likes.user_id inner join users on users.id=likes.user_id
group by photos.user_id
order by total desc
limit 1;

-- The investors want to know how many times does the average user post.
SELECT AVG(post_count) AS average_posts
FROM (
    SELECT u.id, u.username, COUNT(p.user_id) AS post_count
    FROM users u
    LEFT JOIN photos p ON u.id = p.user_id
    GROUP BY u.id, u.username
) user_posts;

SELECT AVG(post_count) AS average_posts
FROM (SELECT user_id, COUNT(*) AS post_count FROM photos GROUP BY user_id) AS UserPosts;


-- A brand wants to know which hashtag to use on a post, and find the top 5 most used hashtags.
select * from photo_tags;
select * from tags;

select t.tag_name,count(*) as t from photo_tags p
join tags t on t.id=p.tag_id
group by t.tag_name
order by t desc
limit 5;

WITH top_tags AS (
    SELECT t.tag_name, COUNT(*) AS tag_count
    FROM photo_tags p
    JOIN tags t ON t.id = p.tag_id
    GROUP BY t.tag_name
    ORDER BY tag_count DESC
    LIMIT 5
)
SELECT * FROM top_tags;


-- To find out if there are bots, find users who have liked every single photo on the site.
select * from likes;
select * from photos;

SELECT u.username
FROM users u
JOIN photos p ON u.id = p.user_id
LEFT JOIN likes l ON p.user_id = l.user_id
GROUP BY u.id, u.username
HAVING COUNT(l.user_id) = COUNT(p.user_id);

select user_id from likes group by user_id  having count(*) =(select count(*) from photos);
-- Find the users who have created instagramid in may and select top 5 newest joinees from it?
select * from users;
SELECT *
FROM users
WHERE MONTH(created_at) = 5
ORDER BY created_at DESC
LIMIT 5;

-- Can you help me find the users whose name starts with c and ends with any number and have posted the photos as well as liked the photos?
SELECT DISTINCT U.*
FROM Users U
JOIN Photos P ON U.id = P.user_id
JOIN Likes L ON U.id = L.user_id
WHERE U.username LIKE 'C%[0-9]';

SELECT DISTINCT U.*
FROM Users U
WHERE U.username REGEXP '^C.*[0-9]$'
AND U.id IN (SELECT DISTINCT user_id FROM Photos)
AND U.id IN (SELECT DISTINCT user_id FROM Likes);


-- Demonstrate the top 30 usernames to the company who have posted photos in the range of 3 to 5.
SELECT U.username
FROM Users U
JOIN Photos P ON U.id = P.user_id
GROUP BY U.username
HAVING COUNT(P.id) BETWEEN 3 AND 5
LIMIT 30;




