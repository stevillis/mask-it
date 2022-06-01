from mask_it import MaskIt

if __name__ == '__main__':
    value = '46983241061'  # CPF
    pattern = '###.###.###-##'
    print(MaskIt(value, pattern).mask())

    value = '16972121000135'  # CNPJ
    pattern = '##.###.###/####-##'
    print(MaskIt(value, pattern).mask())

    value = '83088961497'  # PIS/PASEP
    pattern = '###.#####.##-#'
    print(MaskIt(value, pattern).mask())
