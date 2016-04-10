# Find suspicious transactions
# A transaction is suspicious if:
# 1) amount > 3000
# 2) two transactions from the same person at different locations within 1 hour
# sort the result by time of transaction and for case 2, use the first transaction's time for sorting


class Transaction:
    def __init__(self, name, amount, location, time):
        self.name = name
        self.amount = amount
        self.location = location
        self.time = time


def getSuspiciousList(transactions):
    import operator
    t_name = {}
    res = {}
    for t in transactions:
        name, amount, location, time = t.split("|")
        amount = float(amount)
        time = int(time)

        upsert(t_name, name, Transaction(name, amount, location, time))
        if amount > 3000:
            add_to_fraud(name, res, time)

    for name in t_name:
        trancs = t_name[name]
        trancs.sort(key=lambda x: x.time)
        if len(trancs) > 1:
            for i in range(1, len(trancs)):
                if trancs[i].time - trancs[i - 1].time < 60 and trancs[i].location != trancs[i - 1].location:
                    add_to_fraud(name, res, trancs[i - 1].time)
                    break

    time_sorted = sorted(res.items(), key=operator.itemgetter(1))
    final_res = []
    for name, time in time_sorted:
        final_res.append(name);
    return final_res


def add_to_fraud(name, res, time):
    if name in res:
        if res[name] > time:
            res[name] = time
    else:
        res[name] = time


def upsert(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]


def main():
    res = getSuspiciousList(
            ["Shilpa|500|California|63", "Tom|25|New York|615", "Krasi|9000|California|1230", "Tom|25|New York|1235",
             "Tom|25|New York|1238", "Shilpa|50|Michigan|1300", "Matt|90000|Georgia|1305", "Jay|100000|Virginia|1310",
             "Krasi|49|Florida|1320", "Krasi|83|California|1325", "Shilpa|50|California|1350"])
    print res


if __name__ == '__main__':
    main()
