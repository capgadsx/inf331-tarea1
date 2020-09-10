import logging

def compareStrings(a, b):
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    log = logging.getLogger('compareStrings')
    fh = logging.FileHandler('compareStrings.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))
    log.addHandler(fh)
    log.setLevel(logging.INFO)
    log.info('Llamada a la función compareStrings!')
    log.info('Parametros: a => "{}" [type: {}] b=> "{}" [type: {}]'.format(a, type(a), b, type(b)))
    if type(a) != str or type(b) != str:
        raise ValueError('Tipos de entrada invalidos, esta función solo acepta dos strings como entrada.')
    la = len(a)
    lb = len(b)
    log.info('Largo de a => {} largo de b => {}'.format(la, lb))
    if la > lb:
        log.info('"A" es la cadena más larga ({} caracteres)'.format(la))
        return a
    elif lb > la:
        log.info('"B" es la cadena más larga ({} caracteres)'.format(lb))
        return b
    else:
        log.info('Ambas cadenas tienen el mismo largo')
        raise ValueError('Ambos parametros tienen el mismo largo, no es posible determinar cual cadena es de mayor tamaño.')
