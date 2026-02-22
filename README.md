# 2026 Winter Games Day 17: Closing Day

Given a 2D array of medal winners, return a medal count for each country as a CSV string.

    In the given array, each sub-array represents a single event: [gold_winner, silver_winner, bronze_winner]

    The returned CSV string should have the following format, with the first line being headers:

Country,Gold,Silver,Bronze,Total
country_name,gold_count,silver_count,bronze_count,total_medals

    Separate new lines with the new line character ("\n").
    Do not include spaces around commas or at the end of lines.
    Sort the returned CSV by gold medal count, highest first. If two countries have the same gold medal count, sort the tied ones alphabetically.

For example, given:

```
[
  ["USA", "CAN", "NOR"],
  ["NOR", "USA", "CAN"],
  ["USA", "NOR", "SWE"]
]
```

Return:

```
"Country,Gold,Silver,Bronze,Total\nUSA,2,1,0,3\nNOR,1,1,1,3\nCAN,0,1,1,2\nSWE,0,0,1,1"
```

Which looks like this when printed:

```
Country,Gold,Silver,Bronze,Total
USA,2,1,0,3
NOR,1,1,1,3
CAN,0,1,1,2
SWE,0,0,1,1
```
