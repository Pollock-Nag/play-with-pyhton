given=[[1,3],[2,6],[5,10],[15,18]] #[[1,3],[2,6],[8,10],[15,18]]
ans = []
given.sort()
for i in range(len(given)):
    if ans == []:
        ans.append(given[i])
    else:

        latestStart = given[i][0]
        latestEnd = given[i][1]

        lastEnd = ans[-1][1]

        if lastEnd >= latestStart:
            ans[-1][1] = max(latestEnd, lastEnd)
        else:
            ans.append(given[i])
print(ans)