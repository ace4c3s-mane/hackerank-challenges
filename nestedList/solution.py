if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        
    if 2 <= len(records) <= 5:
        scores = sorted({score for name, score in records})
        second = scores[1]
        
        second_lowest_name = [name for name, value in records if value == second]
        second_lowest_name.sort()
        
        for name in second_lowest_name:
            print(name)


