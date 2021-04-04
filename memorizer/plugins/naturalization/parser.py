

def parse_easytrangers(filename):
    res = {}
    with open(filename, "r") as fd:
        data = fd.read()
        qas = data.split("\n\n")
        qas = [e.strip() for e in qas]
        for qa in qas:
            try:
                question, answer = qa.split("\n", 1)
                question = question.strip()
                answer = answer.strip()
                res[question] = answer
            except Exception:
                print("Unvalid format: ", qa)
        return res
