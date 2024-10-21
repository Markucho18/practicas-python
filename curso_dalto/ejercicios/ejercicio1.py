curso_dalto = 1.5

curso_dalto_crudo = 3.5

curso_minimo = 2.5

curso_promedio = 4

curso_promedio_crudo = 5

curso_maximo = 7

diferencia_dalto_min = 100 - (curso_dalto / curso_minimo * 100)

print(f"El curso de Dalto dura {diferencia_dalto_min}% menos que el minimo de los otros")

diferencia_dalto_pro = 100 - (curso_dalto / curso_promedio * 100)

print(f"El curso de Dalto dura {diferencia_dalto_pro}% menos que el promedio de los otros")

diferencia_dalto_max = 100 - (curso_dalto / curso_maximo * 100)
#REDUCIR LOS DECIMALES (* 1000 / 10 ES LO MISMO QUE * 100)
diferencia_dalto_max = 100 - (curso_dalto * 1000 // curso_maximo / 10)

print(f"El curso de Dalto dura {diferencia_dalto_max}% menos que el maximo de los otros")
print("----------------------------------------")

diferencia_crudo_promedio = 100 - (curso_promedio * 1000 // curso_promedio_crudo / 10)

print(f"En un curso promedio se reduce un {diferencia_crudo_promedio}% del crudo")

diferencia_crudo_dalto = 100 - (curso_dalto * 1000 // curso_dalto_crudo / 10)

print(f"En un curso de dalto se reduce un {diferencia_crudo_dalto}% del crudo")
print("----------------------------------------")

#TODOO ESTA MAAAAAAAAAL
""" diez_horas_dalto_en_promedio = 10 + (diferencia_dalto_pro / 100 * 10)

print(f"10 horas de un curso de Dalto son {diez_horas_dalto_en_promedio} horas de un curso promedio")

diez_horas_promedio_en_dalto = 10 - (diferencia_dalto_pro / 100 * 10)

print(f"10 horas de un curso promedio son {diez_horas_promedio_en_dalto} horas de un curso de Dalto") """