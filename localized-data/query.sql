-- Explore locales data from python locale module

-- total 580 entries
select count(*) from locales;

-- total 156 country
select count(distinct country) from locales;

-- total 203 languages
select count(distinct lang) from locales;

-- total 46 encoding is used
select count(distinct encoding) from locales;

-- total 4 scripts
select count(distinct script) from locales;

-- List of unique scripts
-- devanagari
-- iqtelif
-- latin
-- valencia
select distinct script total_script from locales where script is not null order by script;

-- Language that has no country mapped?, eg: eo, ia
select * from locales where country is null;

-- Bad and inefficient query to get total country count
select count(*) OVER () as total from locales group by country LIMIT 1;

-- Top 5 countries with most languages
-- IN,50
-- US,27
-- ZA,21
-- NO,16
-- ES,16
select country, count(lang) lang_count from locales group by country order by lang_count desc limit 5;

-- Top 5 languages that used by the most countries
-- en,44
-- sr,26
-- es,24
-- ar,22
-- zh,13
select lang, count(country) country_count from locales group by lang order by country_count desc limit 5;

-- Top 5 most used encodings
-- UTF-8,191
-- ISO8859-1,190
-- ISO8859-2,40
-- ISO8859-6,20
-- ISO8859-15,16
select encoding, count(encoding) encoding_count from locales group by encoding order by encoding_count desc limit 5;

-- List of locale country full names
select distinct a.country, b.name
    from locales a left join c_countries b on a.country = b.code
    where b.name is not null
    order by a.country;

-- List of locale lang full names
select distinct a.lang, b.name
    from locales a left join c_languages b on a.lang = b.code
    where b.name is not null
    order by a.lang;

