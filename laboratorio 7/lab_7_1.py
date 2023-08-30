persona = {
 'first_name': 'Edem',
 'last_name': 'Terraza',
 'age': 31,
 'country': 'Peru',
 'is_married': True, # 
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
}
if 'skills' in persona:
    skills_list = persona['skills']
    if len(skills_list) >= 3:
        middle_skill = skills_list[len(skills_list) // 2]
        print("Habilidad del medio:", middle_skill)

# b) Comprobar si la clave 'skills' existe y si contiene la habilidad 'Python'
if 'skills' in persona:
    python_skill_present = 'Python' in persona['skills']
    print("¿Tiene habilidad de Python?", python_skill_present)

# c) Determinar el título basado en las habilidades de la persona
if 'skills' in persona:
    skills = persona['skills']
    if skills == ['JavaScript', 'React']:
        print("Él es un desarrollador frontend")
    elif set(skills) == {'Node', 'Python', 'MongoDB'}:
        print("Él es un desarrollador backend")
    elif set(skills) == {'React', 'Node', 'MongoDB'}:
        print("Él es un desarrollador fullstack")
    else:
        print("Título desconocido")