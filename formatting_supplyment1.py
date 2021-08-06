with open('supplement_1.txt', 'r') as f:
    s = f.readlines()

with open('formated_supplyment_1.txt', 'w') as f:

    is_header = True

    for i in range(len(s)):

        if '% polar' in s[i]:
            is_header = False
            s[i] = s[i].strip().removeprefix('% ')
            s[i] += "comment1 comment2 \n"

        if is_header:
            continue

        if '---' in s[i]:
            continue

        if i == len(s) - 1:
            out = s[i].replace('%', '')
            f.write(out)
            continue

        count_cor = len(s[i].split('%'))
        count_next = len(s[i+1].split('%'))

        if count_cor == 3 and count_next == 1:
            # remove \n
            out = s[i].replace('%', '').strip() + ' '
        elif(count_cor == 1):
            out = s[i].replace('%', '').replace(' ', '_')
        else:
            out = s[i].replace('%', '')

        # out = f'{count} {s[i]}'

        f.write(out)
