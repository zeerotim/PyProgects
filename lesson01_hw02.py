# Звдвние 2. Форматирвоание


seconds_in = int(input("Укажите количество секунд: "))
minutes = seconds_in//60
seconds = seconds_in - minutes*60
hours = minutes//60
minutes = minutes-hours*60

max_width = 2
print(f"Введенное количество секунд соотвествует {hours:0{max_width}}:{minutes:0{max_width}}:{seconds:0{max_width}}")


