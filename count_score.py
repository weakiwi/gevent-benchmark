

def parse_file():
    result = []
    with open("compare_result") as file:
        lines = file.readlines()
        for i in lines:
            if "result_standard" in i:
                result.append(i.strip().split())
    
    return result