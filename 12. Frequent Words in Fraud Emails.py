"""
Take a sample of 10 phishing e-mails and find the most common words.
"""
if __name__ == '__main__':
    with open("Assets\\fraudulent_emails.txt") as spam:
        fraud_data = spam.read().lower()
    t_list = [",", ".", "\\", "/", "?", "!", "-", "+", "_", "=",
              "\n", '"', '@', "$", "%", "*", "(", ")"]

    wrd_lst = ['your', 'that', 'will', 'were', 'with', 'this',
               'then', 'their', 'some', 'into', 'here', 'have',
               'from', 'also', 'after', 'which', 'move']

    for i in t_list:
        fraud_data = fraud_data.replace(i, "")

    frd_list = fraud_data.split()
    for i in fraud_data.split():
        if i in wrd_lst or len(i) < 4:
            frd_list.remove(i)

    frd_dct = {}

    for i in frd_list:
        if i in frd_dct:
            frd_dct[i] += 1
        else:
            frd_dct[i] = 1

    frd = {}

    for i in frd_dct:
        if frd_dct[i] > 10:
            frd[i] = frd_dct[i]

    print(sorted(frd.keys()))
