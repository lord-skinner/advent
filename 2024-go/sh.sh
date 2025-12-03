export SESSION='53616c7465645f5fb77b78cecb5ed8402d3713d4bbb2d258c2f6500946d0d935ea9bc2de2e35a2c0b55a7c3da3651f87df61671c583004b3eb8e6816cf0331d9'

export DAY='3'
curl -H "Cookie: session=$SESSION" https://adventofcode.com/2022/day/$DAY/input -o ./day0$DAY/input.txt
