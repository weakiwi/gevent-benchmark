

def parse_file():
    result = []
    with open("compare_result") as file:
        lines = file.readlines()
        for i in lines:
            if "result_standard" in i:
                result.append(i.strip().split())
    
    return result


def score(result):
    def get_score(line):
        score = line[-1]
        return int(score.replace('(', '').replace(')', '').replace('%', ''))

    def get_name(line):
        return line[0]
    final_score = 0
    weight = 1
    for line in result:
        if "mean" not in line[1].lower():
            continue
        name = get_name(line).lower()
        tmp_score = get_score(line)
        if "hub" in name:
            weight = 32
        elif "local" in name:
            weight = 17
        elif "switch" in name:
            weight = 32
        elif "socket" in name:
            weight = 17
        elif "attr" in name:
            weight = 4
        else:
            weight = 1
        final_score =  final_score + tmp_score * weight
        print("%s %s" % (name, str(tmp_score * weight)))
    return final_score

if __name__ == "__main__":
    lines = parse_file()
    final_score = score(lines)
    print("===============")
    print("final_score: %s" % str(final_score))