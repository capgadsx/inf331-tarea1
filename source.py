import logging

def compareStrings(a, b):
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.getLogger().setLevel(logging.INFO)
    logging.info('Llamada a la función compareStrings!')
    logging.info('Parametros: a => "{}" [type: {}] b=> "{}" [type: {}]'.format(a, type(a), b, type(b)))
    if type(a) != str or type(b) != str:
        raise ValueError('Tipos de entrada invalidos, esta función solo acepta dos strings como entrada.')
    print(a.encode('utf-8'))
    print(b.encode('utf-8'))
    la = len(a)
    lb = len(b)
    logging.info('Largo de a => {} largo de b => {}'.format(la, lb))
    if la > lb:
        logging.info('"A" es la cadena más larga ({} caracteres)'.format(la))
        return a
    elif lb > la:
        logging.info('"B" es la cadena más larga ({} caracteres)'.format(lb))
        return b
    else:
        logging.info('Ambas cadenas tienen el mismo largo')
        raise ValueError('Ambos parametros tienen el mismo largo, no es posible determinar cual cadena es de mayor tamaño.')

compareStrings('aaaaa', 'asd' * 10)
compareStrings('aaaaa', '\xC0')
#compareStrings(200, 30)
