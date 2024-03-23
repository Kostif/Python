def fun():
    print('FUNC() in one.py')

print('TOPLEVELINONE.py')

if __name__ == '__main__':
    print('ONE.PY is being run directly!')
else:
    print('One.PY has been imported')