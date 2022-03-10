phrase = input('Type a phrase: ').strip().upper().split()
at = ''.join(phrase)
iv = at[::-1]
'''iv = ''
for lg in range(len(at) -1, -1, - 1):
    iv+=at[lg]'''
print(f'The inverse of {at} is {iv}')
if at == iv:
    print('This phrase is a palindrome')
else:
    print('This phrase is not a palindrome')