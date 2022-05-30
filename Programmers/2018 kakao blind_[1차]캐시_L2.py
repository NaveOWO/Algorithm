def solution(cacheSize, cities):
    cache = []
    runTime = 0

    if cacheSize == 0:
        return len(cities) * 5
    else:
        for i in range(len(cities)):
            cities[i] = cities[i].lower()
        for city in cities:
            if city not in cache:
                if len(cache) < cacheSize:
                    cache.append(city)
                else:
                    cache.pop(0)
                    cache.append(city)
                runTime += 5
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                runTime += 1

    return runTime