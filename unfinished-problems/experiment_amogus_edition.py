'''
# oops forgot to flush
IQ = -100
feedback = input()
k = int(feedback)
print(18, flush=True)
i = 1
while "DEFEAT" not in feedback and "REPORTS" not in feedback:
    print(1, flush=True)
    print(i, flush=True)
    feedback = input()
    i += 1
'''

