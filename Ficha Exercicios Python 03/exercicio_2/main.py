import analise_pasta as analyse


def main():
    path = analyse.pede_pasta()
    dic_info = analyse.faz_calculos(path)
    analyse.guarda_resultados(path, dic_info)
    analyse.faz_grafico_queijos(dic_info)
    analyse.faz_grafico_barras(dic_info)


if __name__ == '__main__':
    main()