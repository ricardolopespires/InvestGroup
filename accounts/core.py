






def idade(nascimento):
    from datetime import date
    current_date = date.today()
    data_actual = current_date.year
    idade = data_actual - nascimento   
    return idade