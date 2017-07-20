 3
create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------


-- #1 The names of all "toy" and "mini" dogs.
SELECT name FROM dogs AS d, sizes AS s 
	WHERE d.height > s.min AND d.height <= s.max
	AND s.size in ('mini', 'toy') 
	ORDER BY d.name asc;


-- Expected output:
--   abraham
--   eisenhower
--   fillmore
--   grover
--   herbert

-- Create a table dog_sizes for later use in #3
CREATE TABLE dog_sizes AS
	SELECT d.name, s.size FROM dogs AS d, sizes AS s 
	WHERE d.height > s.min AND d.height <= s.max;

--expected:
-- name	size
-- abraham	toy
-- barack	standard
-- clinton	standard
-- delano	standard
-- eisenhower	mini
-- fillmore	mini
-- grover	toy
-- herbert	mini

--#2 All dogs with parents ordered by decreasing height of their parent

SELECT p.child from parents as p
JOIN dogs as d
ON d.name = p.parent 
ORDER BY d.height desc;
-- Expected output:
--   herbert
--   fillmore
--   abraham
--   delano
--   grover
--   barack
--   clinton

-- Sentences about siblings that are the same size
WITH siblings(sib1, sib2)
AS (
  select p1.child as sib1, p2.child as sib2
  FROM parents AS p1
  JOIN parents AS p2
  ON p1.parent = p2.parent
  WHERE sib1 < sib2
  )


-- Expected output:
--   barack and clinton are standard siblings
--   abraham and grover are toy siblings

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
select "REPLACE THIS LINE WITH YOUR SOLUTION";
-- Expected output:
--   abraham, delano, clinton, barack|171
--   grover, delano, clinton, barack|173
--   herbert, delano, clinton, barack|176
--   fillmore, delano, clinton, barack|177
--   eisenhower, delano, clinton, barack|180

-- All non-parent relations ordered by height difference
select "REPLACE THIS LINE WITH YOUR SOLUTION";
-- Expected output:
--   fillmore|barack
--   eisenhower|barack
--   fillmore|clinton
--   eisenhower|clinton
--   eisenhower|delano
--   abraham|eisenhower
--   grover|eisenhower
--   herbert|eisenhower
--   herbert|fillmore
--   fillmore|herbert
--   eisenhower|herbert
--   eisenhower|grover
--   eisenhower|abraham
--   delano|eisenhower
--   clinton|eisenhower
--   clinton|fillmore
--   barack|eisenhower
--   barack|fillmore


