import argparse


def _get_function_args(function):
    args_name = function.__code__.co_varnames[:function.__code__.co_argcount]
    defaults = [] if function.__defaults__ is None else function.__defaults__
    types = function.__annotations__
    doc = '' if function.__doc__ is None else function.__doc__

    args = {name: {} for name in args_name}

    for default, name in zip(defaults, args_name[-len(defaults):]):
        args[name]['default'] = default

    for name in types:
        args[name]['type'] = types[name]

    # Parse the docstring
    doc = doc.split('\n')
    for arg_doc in doc:
        arg_doc = arg_doc.strip()
        arg = arg_doc.split(':')[0]
        if arg in args:
            args[arg]['help'] = arg_doc.split(':')[-1].strip()

    for arg in args:
        if 'help' not in args[arg]:
            args[arg]['help'] = ''

    return args


def console(function):
    all_models = cmdargs.all_models

    function_name = function.__name__
    description = (
        None if function.__doc__ is None
        else function.__doc__.split('Args:')[0].strip()
    )
    args = _get_function_args(function)

    if len(all_models) and (function_name == 'main' or 'main' in all_models):
        raise Exception("You can't decorate main and others functions")

    if function_name in all_models:
        raise Exception("This function name has already been decorated")

    all_models[function_name] = function

    if function_name == 'main':
        parser = cmdargs.arg_parser

    else:
        if not hasattr(cmdargs, 'subparsers'):
            cmdargs.subparsers = cmdargs.arg_parser.add_subparsers(dest='_mod')

        parser = cmdargs.subparsers.add_parser(
            function_name,
            description=description
        )

    optionnals = [n for n in args if 'default' in args[n]]
    requireds = [n for n in args if 'default' not in args[n]]

    for arg in sorted(requireds):
        parser.add_argument(
            '-' + arg[0], '--' + arg,
            **args[arg],
            metavar='',
            required=True
        )

    for arg in sorted(optionnals):
        args[arg]['help'] = '(%s) ' % args[arg]['default'] + args[arg]['help']
        parser.add_argument(
            '-' + arg[0], '--' + arg,
            **args[arg],
            metavar='',
            required=False
        )

    parser._optionals.title = 'Arguments'
    parser._positionals.title = 'Modes'

    return function


def parse_args():
    arg_parser = cmdargs.arg_parser
    all_models = cmdargs.all_models

    args = vars(arg_parser.parse_args())
    if len(all_models) == 1 and 'main' in all_models:
        all_models['main'](**args)

    elif '_mod' in args and args['_mod'] in all_models:
        model = args['_mod']
        del args['_mod']
        all_models[model](**args)

    else:
        arg_parser.print_help()


def cmdargs():
    if hasattr(cmdargs, 'inited'):
        return
    cmdargs.inited = True
    cmdargs.all_models = {}
    arg_parser = argparse.ArgumentParser()
    arg_parser._positionals.title = 'Modes'
    arg_parser._optionals.title = 'Optional arguments'
    cmdargs.arg_parser = arg_parser


cmdargs()
