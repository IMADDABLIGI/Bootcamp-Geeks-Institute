# def check_arguments_keywordedarguments (required_arg, *args, **kwargs):
#     print(required_arg)
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)

# check_arguments_keywordedarguments("required argument")
# check_arguments_keywordedarguments("required argument", 1, 2, 'hey')
# check_arguments_keywordedarguments("required argument", 1, 2, 'hey', name="Sarah", age=24)

# def check(a, b, c):
#     print(a, b, c)

# a = [1,2,3]
# check(*a)


# # a = {'a':'Sarah', 'b': 24}
# # check(**a)


# a = {'a':'Sarah', 'b':24, 'c': 180}
# check(**a)

# def fnc(*arg):
#     print(arg[1])
#     for ar in arg:
#         ar = ar + 1
#         print(ar)
#     print(arg)

# fnc(1, 2, 3)

def fnc2(**kwarg):
    print(kwarg)

fnc2(name="Sarah", age=24, city="Casablanca")
